# agents.py

class TableAgent:
    def __init__(self, table_number):
        self.table_number = table_number

    def create_order(self, item):
        return {
            "table": self.table_number,
            "item": item,
            "status": "NEW"
        }


class KitchenAgent:
    def receive(self, order):
        order["kitchen_status"] = "RECEIVED"
        return order


class CashierAgent:
    def receive(self, order):
        order["bill"] = self.calculate_bill(order["item"])
        return order

    def calculate_bill(self, item):
        price_list = {
            "Fried Rice": 1200,
            "Kottu": 1400,
            "Noodles": 1000
        }
        return price_list.get(item, 0)


class DispatcherAgent:
    def __init__(self, kitchen, cashier):
        self.kitchen = kitchen
        self.cashier = cashier

    def dispatch(self, order):
        order = self.kitchen.receive(order)
        order = self.cashier.receive(order)
        order["status"] = "DISPATCHED"
        return order
