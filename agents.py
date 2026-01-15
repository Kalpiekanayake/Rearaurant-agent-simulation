# agents.py

class TableAgent:
    def __init__(self, table_number):
        self.table_number = table_number

    def place_order(self, item):
        """Return order as dictionary"""
        return {"table": self.table_number, "item": item, "status": "pending"}


class KitchenAgent:
    def __init__(self):
        self.orders = []

    def receive_order(self, order):
        """Add order to kitchen queue"""
        self.orders.append(order)
        print(f"Order received from Table {order['table']}: {order['item']}")

    def process_orders(self):
        """Process all pending orders"""
        for order in self.orders:
            if order["status"] == "pending":
                order["status"] = "ready"
                print(f"Order ready for Table {order['table']}: {order['item']}")
