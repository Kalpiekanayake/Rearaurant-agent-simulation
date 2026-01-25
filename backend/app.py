# app.py

from flask import Flask, request, jsonify
from agents import TableAgent, KitchenAgent, CashierAgent, DispatcherAgent

app = Flask(__name__)

kitchen_agent = KitchenAgent()
cashier_agent = CashierAgent()
dispatcher = DispatcherAgent(kitchen_agent, cashier_agent)

ORDERS = []


@app.route("/order", methods=["POST"])
def place_order():
    data = request.json
    table = TableAgent(data["table"])
    order = table.create_order(data["item"])

    processed_order = dispatcher.dispatch(order)
    ORDERS.append(processed_order)

    return jsonify(processed_order)


@app.route("/active_orders")
def active_orders():
    return jsonify(ORDERS)


if __name__ == "__main__":
    app.run(debug=True)
