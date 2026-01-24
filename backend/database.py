# database.py

import sqlite3

def init_db():
    conn = sqlite3.connect("restaurant.db")
    cursor = conn.cursor()

    # Create menu table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            item_name TEXT PRIMARY KEY,
            price REAL
        )
    """)

    # Create tables table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tables (
            table_number INTEGER PRIMARY KEY
        )
    """)

    # Create orders table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_number INTEGER,
            items TEXT,
            status TEXT,
            FOREIGN KEY(table_number) REFERENCES tables(table_number)
        )
    """)

    # Insert menu items if not exist
    menu_items = [("Fried Rice", 5.0), ("Coke", 1.5), ("Kottu", 6.0), ("Burger", 4.0)]
    for item, price in menu_items:
        cursor.execute("INSERT OR IGNORE INTO menu(item_name, price) VALUES (?, ?)", (item, price))

    conn.commit()
    conn.close()
