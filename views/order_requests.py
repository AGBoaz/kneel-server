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

def create_order(new_order):
    """creates one order"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            ( metal_id, size_id, style_id )
        VALUES
            ( ?, ?, ? )
        """, (new_order['metal_id'], new_order['size_id'], new_order['style_id'], ))

        id = db_cursor.lastrowid
        new_order['id'] = id 
    return new_order

def delete_order(id):
    """ delete an order """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Orders
        WHERE id = ?
        """, (id, ))


def update_order(id, new_order):
    """ update an orders information
    """
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break