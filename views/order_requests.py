import time
import json
import sqlite3
from models import Order

ORDERS = [
    {
      "id": 1,
      "order_id": 1,
      "size_id": 1,
      "style_id": 1,
      "time_stamp": time.time()
    },
    {
      "id": 2,
      "order_id": 1,
      "size_id": 2,
      "style_id": 1,
      "time_stamp": time.time()
    },
]


def get_all_orders():
    """gets all the orders
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM Orders o
        """)

        orders = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Order(row['id'], row['metal_id'], row['size_id'], row['style_id'])
            orders.append(order.__dict__)
    return orders


# Function with a single parameter
def get_single_order(id):
    """gets one order"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM Orders o
        WHERE o.id = ?
        """, (id, ))

        data = db_cursor.fetchone()
        order = Order(data['id'], data['metal_id'], data['size_id'], data['style_id'])

        return order.__dict__

def create_order(order):
    """creates one order
    """
    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    order["id"] = new_id

    # Add the order dictionary to the list
    ORDERS.append(order)
    return order

def delete_order(id):
    """ delete an order 
    """
    # Initial -1 value for order index, in case one isn't found
    order_index = -1

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index

    if order_index >= 0:
        ORDERS.pop(order_index)


def update_order(id, new_order):
    """ update an orders information
    """
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break