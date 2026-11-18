inventory = [
    {"item": "Packing tape", "quantity": 8, "reorder_point": 20, "aisle": "A2", "unit_price": 5},
    {"item": "Office desk", "quantity": 5, "reorder_point": 10, "aisle": "F1", "unit_price": 300},
    {"item": "Office chair", "quantity": 10, "reorder_point": 10, "aisle": "F2", "unit_price": 100},
    {"item": "Printer", "quantity": 15, "reorder_point": 15, "aisle": "E1", "unit_price": 150},
    {"item": "Monitor", "quantity": 20, "reorder_point": 15, "aisle": "E2", "unit_price": 200},
    {"item": "Keyboard", "quantity": 25, "reorder_point": 20, "aisle": "E3", "unit_price": 80},
]

def find_inventory_value(inventory):
    total = 0
    for item in inventory:
        item_total_price = item["quantity"] * item["unit_price"]
        total = total + item_total_price
    return total

print(find_inventory_value(inventory))