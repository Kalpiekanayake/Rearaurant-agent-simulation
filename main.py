# main.py

from agents import TableAgent, KitchenAgent

# Create agents
table1 = TableAgent(1)
table2 = TableAgent(2)

kitchen = KitchenAgent()

# Tables place orders
order1 = table1.place_order(["Fried Rice", "Coke"])
order2 = table2.place_order(["Kottu"])

# Kitchen receives orders
kitchen.receive_order(order1)
kitchen.receive_order(order2)

# First status check
table1.check_orders()
table2.check_orders()

print("\n--- Kitchen updating orders ---")
kitchen.update_orders()

# Second status check
table1.check_orders()
table2.check_orders()

print("\n--- Kitchen updating orders again ---")
kitchen.update_orders()

# Final status check
table1.check_orders()
table2.check_orders()
