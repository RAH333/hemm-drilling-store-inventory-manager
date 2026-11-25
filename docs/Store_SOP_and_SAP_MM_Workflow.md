# Standard Operating Procedure (SOP): HEMM & Drilling Spare Parts Store

## 1. Material Inward & GRN Process (`ME23N` -> `MIGO`)
1. Verify vendor Delivery Challan and Tax Invoice against approved Purchase Order (`ME23N`).
2. Inspect OEM part numbers, thread/dimension specs (drill rods, bits, bearings), and seal integrity with Mechanical Maintenance Engineer.
3. Post Goods Receipt Note (GRN) in SAP (`MIGO` Movement Type `101`).
4. Apply bin tag with Material Code, GRN Date (for FIFO tracking), and store in designated rack/yard location.

## 2. Workshop Material Issue (`MIGO` Movement Type `201`)
1. Receive approved Material Reservation / Work Order slip from HEMM or Exploration Drilling maintenance team.
2. Pick oldest stock first (**FIFO**) for elastomers (O-rings, hydraulic hoses) and lubricants.
3. Post Goods Issue against equipment cost center and update physical bin card.

## 3. Cycle Counting & Physical Verification (`MI01` / `MI04` / `MI07`)
- **Class A (High-Value Core Bits, Bearings, Pumps):** Weekly physical count.
- **Class B (Filters, Ground Engaging Tools):** Bi-weekly physical count.
- **Class C (Fasteners, Standard O-Rings):** Monthly physical count.
- 
