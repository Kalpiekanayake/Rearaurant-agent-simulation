from agents import TableAgent, KitchenAgent

# Create multiple tables
tables = [TableAgent(i) for i in range(1, 4)]  # Tables 1, 2, 3

# Create kitchen agent
kitchen = KitchenAgent()

# Simulate orders
orders_to_place = [
    (1, "Fried Rice"),
    (2, "Noodles"),
    (1, "Coke"),
    (3, "Burger"),
    (2, "Water")
]

# Tables place orders and kitchen receives them
for table_num, item in orders_to_place:
    table = tables[table_num - 1]  # get table object
    order = table.place_order(item)
    kitchen.receive_order(order)

# Process all orders in kitchen
print("\n--- Processing Orders ---")
kitchen.process_orders()
