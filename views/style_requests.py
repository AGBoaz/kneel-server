STYLES = [
    {
      "id": 1,
      "style": "round",
      "price": 400.42
    },
    {
      "id": 2,
      "style": "marquise",
      "price": 1472.4
    },
    {
      "id": 3,
      "style": "radiant",
      "price": 1198.9
    },
    {
      "id": 4,
      "style": "asscher",
      "price": 855.45
    },
    {
      "id": 5,
      "style": "oval",
      "price": 1371
    }
]


def get_all_styles():
    """gets all the styles
    """
    return STYLES


# Function with a single parameter
def get_single_style(id):
    """gets one style
    """

    requested_style = None

    for style in STYLES:      
        if style["id"] == id:
            requested_style = style

    return requested_style

def create_style(style):
    """creates one style
    """
    # Get the id value of the last style in the list
    max_id = STYLES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the style dictionary
    style["id"] = new_id

    # Add the style dictionary to the list
    STYLES.append(style)
    return style