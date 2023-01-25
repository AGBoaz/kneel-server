METALS = [
    {
      "id": 1,
      "metal": "Sterling Silver",
      "price": 12.42
    },
    {
      "id": 2,
      "metal": "14K Gold",
      "price": 736.4
    },
    {
      "id": 3,
      "metal": "24K Gold",
      "price": 1258.9
    },
    {
      "id": 4,
      "metal": "Platinum",
      "price": 795.45
    },
    {
      "id": 5,
      "metal": "Palladium",
      "price": 1241
    }
]


def get_all_metals():
    """gets all the metals
    """
    return METALS


# Function with a single parameter
def get_single_metal(id):
    """gets one metal
    """

    requested_metal = None

    for metal in METALS:      
        if metal["id"] == id:
            requested_metal = metal

    return requested_metal

def create_metal(metal):
    """creates one metal
    """
    # Get the id value of the last metal in the list
    max_id = METALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the metal dictionary
    metal["id"] = new_id

    # Add the metal dictionary to the list
    METALS.append(metal)
    return metal