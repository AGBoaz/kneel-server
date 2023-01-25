import time
import sqlite3
from models import Metal

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



# Function with a single parameter
def get_single_order(id):
    """gets one order
    """

    requested_order = None

    for order in ORDERS:      
        if order["id"] == id:
            requested_order = order

    return requested_order

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