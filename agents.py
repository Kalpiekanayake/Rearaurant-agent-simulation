# agents.py

import sqlite3

DB = "restaurant.db"

class TableAgent:
    def __init__(self, table_number):
        self.table_number = table_number
        self._register_table()

    def _register_table(self):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO tables(table_number) VALUES (?)", (self.table_number,))
        conn.commit()
        conn.close()

    def place_order(self, items):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        items_str = ",".join(items)
        cursor.execute(
            "INSERT INTO orders(table_number, items, status) VALUES (?, ?, ?)",
            (self.table_number, items_str, "PLACED")
        )
        conn.commit()
        conn.close()
        print(f"Table {self.table_number} placed order: {items}")

    def check_orders(self):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute("SELECT items, status FROM orders WHERE table_number = ?", (self.table_number,))
        orders = cursor.fetchall()
        print(f"\nStatus for Table {self.table_number}:")
        for items, status in orders:
            print(f"  Items: {items.split(',')} | Status: {status}")
        conn.close()

    def request_bill(self):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute("SELECT items FROM orders WHERE table_number = ?", (self.table_number,))
        orders = cursor.fetchall()
        total = 0
        for (items_str,) in orders:
            items = items_str.split(",")
            for item in items:
                cursor.execute("SELECT price FROM menu WHERE item_name = ?", (item,))
                price = cursor.fetchone()[0]
                total += price
        print(f"\nTable {self.table_number} total bill: ${total:.2f}")
        conn.close()


class KitchenAgent:
    def update_orders(self):
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        # Get orders that are PLACED or PREPARING
        cursor.execute("SELECT order_id, status FROM orders WHERE status IN ('PLACED','PREPARING')")
        orders = cursor.fetchall()
        for order_id, status in orders:
            if status == "PLACED":
                cursor.execute("UPDATE orders SET status = 'PREPARING' WHERE order_id = ?", (order_id,))
                print(f"Order {order_id} is now PREPARING")
            elif status == "PREPARING":
                cursor.execute("UPDATE orders SET status = 'READY' WHERE order_id = ?", (order_id,))
                print(f"Order {order_id} is now READY")
        conn.commit()
        conn.close()
