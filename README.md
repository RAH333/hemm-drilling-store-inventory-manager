# hemm-drilling-store-inventory-manager
Mechanical Spare Parts Warehouse Management &amp; Inventory Automation System for HEMM and Exploration Drilling Operations (SAP MM style GRN/Issue tracking, ABC-VED analysis, FIFO shelf-life alerts, and Excel reporting).

# HEMM & Exploration Drilling Spare Parts Store Management System

A practical warehouse and inventory control toolkit built for mining and heavy infrastructure sites. Designed around **Mechanical Engineering spare-parts taxonomy** and **SAP MM (Materials Management)** workflows (`MIGO`, `MMBE`, `MB51`).

## Key Store Operations Covered
1. **Material Master & Bin Location Tracking (`data/spare_parts_master.csv`):** Catalogs HEMM (Excavator, Dumper, Loader) and Exploration Drilling (NQ/HQ Drill Rods, Diamond Core Bits, Hydraulic Seal Kits) parts with OEM part numbers and rack/bin codes.
2. **GRN & Goods Issue Ledger (`src/inventory_engine.py`):** Processes incoming vendor deliveries (Goods Receipt) and workshop issues (Goods Issue) to compute real-time closing stock and valuation.
3. **Critical Reorder & FIFO Shelf-Life Alerts:** Flags spare parts below minimum reorder level and detects expiring rubber seals/lubricants under **FIFO (First-In, First-Out)** rules.
4. **Automated Management Excel Report (`src/generate_excel_report.py`):** Generates a multi-sheet `.xlsx` store audit report ready for site managers and procurement teams.

## Quick Start
```bash
git clone https://github.com<your-username>/hemm-drilling-store-inventory-manager.git
cd hemm-drilling-store-inventory-manager
pip install -r requirements.txt
python src/inventory_engine.py
python src/generate_excel_report.py
```


```
hemm-drilling-store-inventory-manager/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── spare_parts_master.csv
│   └── stock_movements_log.csv
├── docs/
│   └── Store_SOP_and_SAP_MM_Workflow.md
└── src/
    ├── __init__.py
    ├── inventory_engine.py
    └── generate_excel_report.py
```
