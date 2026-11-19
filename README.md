# Warehouse Restock Report

A Python program that checks a warehouse's inventory, lists which items need restocking, and looks up any item's quantity, aisle and stock value.

## The Problem

Without this program, a warehouse manager would need to check every item's count against its reorder point by hand. This program gives the manager a clear summary of the items that need to be reordered.

## Features

- `find_inventory_total` gives back the total stock value of all inventory in the warehouse.
- `find_reorder_products` gives back a list of full inventory records that need to be reordered if quantity is at or below the reorder point.
- `find_reorder_items` gives back just the names of the items that need to be reordered if quantity is at or below the reorder point.
- `find_item_quantity` gives back the quantity of a specific item or returns "Not found" if item doesn't exist.
- `find_item_aisle` gives back the aisle of a specific item or returns "Not found" if item doesn't exist.
- `find_item_total` gives back one specific item's stock value or returns "Not found" if item doesn't exist.
- Prints a readable restock list, one line per item with its quantity, reorder point and aisle.

## Sample Output

```
Packing tape: 8 on hand, reorder at 20, aisle A2
Office desk: 5 on hand, reorder at 10, aisle F1
Office chair: 10 on hand, reorder at 10, aisle F2
Printer: 15 on hand, reorder at 15, aisle E1
```

## How to Run

```
python restock_report.py
```