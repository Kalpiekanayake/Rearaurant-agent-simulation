# main.py

from agents import TableAgent, KitchenAgent, CashierAgent

# Step 0: Setup menu
menu = {
    "Fried Rice": 5.0,
    "Coke": 1.5,
    "Kottu": 6.0,
    "Burger": 4.0
}

# Step 1: Create agents
table1 = TableAgent(1)
table2 = TableAgent(2)
kitchen = KitchenAgent()
cashier = CashierAgent(menu)

# Step 2: Tables place orders
order1 = table1.place_order(["Fried Rice", "Coke"])
order2 = table2.place_order(["Kottu", "Coke"])

# Step 3: Kitchen receives orders
kitchen.receive_order(order1)
kitchen.receive_order(order2)

# Step 4: Check current status
table1.check_orders()
table2.check_orders()

# Step 5: Kitchen updates orders (simulate time)
print("\n--- Kitchen updating orders ---")
kitchen.update_orders()

# Step 6: Tables check orders again
table1.check_orders()
table2.check_orders()

# Step 7: Tables request bill from cashier
table1.request_bill(cashier)
table2.request_bill(cashier)
