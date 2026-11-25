"""
Generates a formatted multi-sheet Excel Store Audit Report (.xlsx)
including Stock Overview (MMBE style), Reorder Action List, and Movement Ledger (MB51 style).
"""

import os
import pandas as pd
from inventory_engine import run_inventory_audit


def export_store_excel_report(master_csv: str, movements_csv: str, output_xlsx: str) -> None:
    stock_df = run_inventory_audit(master_csv, movements_csv)
    moves_df = pd.read_csv(movements_csv)
    reorder_df = stock_df[stock_df["reorder_status"] != "OK"]

    with pd.ExcelWriter(output_xlsx, engine="openpyxl") as writer:
        stock_df.to_excel(writer, sheet_name="MMBE_Stock_Overview", index=False)
        reorder_df.to_excel(writer, sheet_name="PR_Reorder_Alerts", index=False)
        moves_df.to_excel(writer, sheet_name="MB51_Movement_Log", index=False)

    print(f"Store Audit Excel Report successfully exported to: {output_xlsx}")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    master_path = os.path.join(base_dir, "data", "spare_parts_master.csv")
    moves_path = os.path.join(base_dir, "data", "stock_movements_log.csv")
    output_file = os.path.join(base_dir, "Zawar_Store_Audit_Report.xlsx")

    export_store_excel_report(master_path, moves_path, output_file)
  
