# main.py

from database import init_db
from agents import TableAgent, KitchenAgent

# Step 0: Initialize DB
init_db()

# Step 1: Create agents (3 tables)
table1 = TableAgent(1)
table2 = TableAgent(2)
table3 = TableAgent(3)
kitchen = KitchenAgent()

# Step 2: Tables place orders
table1.place_order(["Fried Rice", "Coke"])
table2.place_order(["Kottu", "Coke"])
table3.place_order(["Burger", "Coke"])

# Step 3: First check
table1.check_orders()
table2.check_orders()
table3.check_orders()

# Step 4: Kitchen updates orders
print("\n--- Kitchen updating orders ---")
kitchen.update_orders()

# Step 5: Check again
table1.check_orders()
table2.check_orders()
table3.check_orders()

# Step 6: Kitchen updates orders again
print("\n--- Kitchen updating orders again ---")
kitchen.update_orders()

# Step 7: Final status check
table1.check_orders()
table2.check_orders()
table3.check_orders()

# Step 8: Request bills
table1.request_bill()
table2.request_bill()
table3.request_bill()
