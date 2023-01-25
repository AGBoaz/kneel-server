SIZES = [
    {
      "id": 1,
      "carats": 24,
      "price": 12.42
    },
    {
      "id": 2,
      "carats": 14,
      "price": 736.4
    },
    {
      "id": 3,
      "carats": 24,
      "price": 1258.9
    },
]


def get_all_sizes():
    """gets all the sizes
    """
    return SIZES


# Function with a single parameter
def get_single_size(id):
    """gets one size
    """

    requested_size = None

    for size in SIZES:      
        if size["id"] == id:
            requested_size = size

    return requested_size

def create_size(size):
    """creates one size
    """
    # Get the id value of the last size in the list
    max_id = SIZES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the size dictionary
    size["id"] = new_id

    # Add the size dictionary to the list
    SIZES.append(size)
    return size