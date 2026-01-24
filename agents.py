# agents.py

class TableAgent:
    def __init__(self, table_number):
        self.table_number = table_number
        self.orders = []

    def place_order(self, items):
        order = {
            "table": self.table_number,
            "items": items,
            "status": "PLACED"
        }
        self.orders.append(order)
        print(f"Table {self.table_number} placed order: {items}")
        return order

    def check_orders(self):
        print(f"\nStatus for Table {self.table_number}:")
        for order in self.orders:
            print(f"  Items: {order['items']} | Status: {order['status']}")

    def request_bill(self, cashier_agent):
        total = cashier_agent.calculate_bill(self.orders)
        print(f"\nTable {self.table_number} total bill: ${total:.2f}")


class KitchenAgent:
    def __init__(self):
        self.active_orders = []

    def receive_order(self, order):
        order["status"] = "PREPARING"
        self.active_orders.append(order)
        print(f"Kitchen started preparing order from Table {order['table']}")

    def update_orders(self):
        for order in self.active_orders:
            if order["status"] == "PREPARING":
                order["status"] = "READY"
                print(f"Order from Table {order['table']} is READY")
            elif order["status"] == "READY":
                order["status"] = "SERVED"
                print(f"Order from Table {order['table']} has been SERVED")


class CashierAgent:
    def __init__(self, menu):
        """
        menu = dictionary of item:price
        """
        self.menu = menu

    def calculate_bill(self, orders):
        total = 0
        for order in orders:
            for item in order["items"]:
                price = self.menu.get(item, 0)
                total += price
        return total
