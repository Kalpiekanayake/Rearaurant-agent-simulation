# app.py

from flask import Flask, request, jsonify
from agents import TableAgent, KitchenAgent, CashierAgent
from database import init_db
import sqlite3

DB = "restaurant.db"

app = Flask(__name__)
init_db()

# Agents
kitchen = KitchenAgent()
cashier = CashierAgent(menu={"Fried Rice": 5.0, "Coke":1.5, "Kottu":6.0, "Burger":4.0})

# Place order
@app.route("/place_order", methods=["POST"])
def place_order():
    data = request.json
    table_number = data["table_number"]
    items = data["items"]
    table = TableAgent(table_number)
    table.place_order(items)
    return jsonify({"message": f"Order placed for Table {table_number}"}), 201

# Get active orders
@app.route("/active_orders", methods=["GET"])
def active_orders():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT order_id, table_number, items, status FROM orders WHERE status IN ('PLACED','PREPARING')")
    orders = cursor.fetchall()
    conn.close()
    result = [{"order_id": oid, "table": t, "items": items.split(","), "status": s} for oid, t, items, s in orders]
    return jsonify(result)

# Update order status
@app.route("/update_order/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM orders WHERE order_id = ?", (order_id,))
    row = cursor.fetchone()
    if not row:
        return jsonify({"error": "Order not found"}), 404
    status = row[0]
    if status == "PLACED":
        new_status = "PREPARING"
    elif status == "PREPARING":
        new_status = "READY"
    elif status == "READY":
        new_status = "SERVED"
    else:
        new_status = status
    cursor.execute("UPDATE orders SET status=? WHERE order_id=?", (new_status, order_id))
    conn.commit()
    conn.close()
    return jsonify({"order_id": order_id, "new_status": new_status})

# Get table bill
@app.route("/bill/<int:table_number>", methods=["GET"])
def get_bill(table_number):
    table = TableAgent(table_number)
    import io
    import sys
    buffer = io.StringIO()
    sys.stdout = buffer
    table.request_bill()
    sys.stdout = sys.__stdout__
    bill_text = buffer.getvalue()
    return jsonify({"table": table_number, "bill": bill_text.strip()})

if __name__ == "__main__":
    app.run(debug=True)
