"""
SAP-Style Inventory & Reorder Engine for HEMM and Drilling Spare Parts.
Computes closing stock from opening balances + GRN receipts - Workshop Issues,
flags reorder alerts, and checks FIFO shelf-life aging.
"""

import os
import pandas as pd


def run_inventory_audit(master_csv: str, movements_csv: str, reference_date: str = "2026-11-25") -> pd.DataFrame:
    master_df = pd.read_csv(master_csv)
    moves_df = pd.read_csv(movements_csv)

    # Aggregate GRN (Inward) and Goods Issue (Outward) quantities
    grn_totals = (
        moves_df[moves_df["movement_type"] == "GRN_IN"]
        .groupby("material_code")["quantity"]
        .sum()
        .rename("total_grn_in")
    )
    issue_totals = (
        moves_df[moves_df["movement_type"] == "ISSUE_OUT"]
        .groupby("material_code")["quantity"]
        .sum()
        .rename("total_issued_out")
    )

    df = master_df.merge(grn_totals, on="material_code", how="left").merge(
        issue_totals, on="material_code", how="left"
    )
    df["total_grn_in"] = df["total_grn_in"].fillna(0).astype(int)
    df["total_issued_out"] = df["total_issued_out"].fillna(0).astype(int)

    # Calculate Closing Stock and Stock Valuation
    df["closing_stock"] = df["opening_stock"] + df["total_grn_in"] - df["total_issued_out"]
    df["stock_value_inr"] = df["closing_stock"] * df["unit_price_inr"]

    # Reorder Alert Check
    df["reorder_status"] = df.apply(
        lambda row: "REORDER REQUIRED (Raise PR)" if row["closing_stock"] <= row["reorder_level"] else "OK",
        axis=1,
    )

    # FIFO Shelf-Life Aging Check
    ref_dt = pd.to_datetime(reference_date)
    df["received_date"] = pd.to_datetime(df["received_date"])
    df["age_days"] = (ref_dt - df["received_date"]).dt.days
    df["remaining_shelf_days"] = df["shelf_life_days"] - df["age_days"]
    df["fifo_alert"] = df["remaining_shelf_days"].apply(
        lambda d: "URGENT FIFO ISSUE (<30 Days)" if d <= 30 else "Normal"
    )

    return df


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    master_path = os.path.join(base_dir, "data", "spare_parts_master.csv")
    moves_path = os.path.join(base_dir, "data", "stock_movements_log.csv")

    report_df = run_inventory_audit(master_path, moves_path)

    print("=== HEMM & DRILLING STORE CLOSING STOCK SUMMARY ===")
    cols = ["material_code", "part_description", "bin_location", "closing_stock", "reorder_status", "fifo_alert"]
    print(report_df[cols].to_string(index=False))
    print(f"\nTotal Store Valuation: INR {report_df['stock_value_inr'].sum():,.2f}")
  
