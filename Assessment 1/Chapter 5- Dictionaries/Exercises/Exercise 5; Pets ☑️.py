# Create a list of dictionaries representing different pets with various traits (Put silly names ehehehehe)
pets = [
    {"animal": "Dog", "name": "Argonaut", "appearance": "White Fluffy coat", "favorite_food": "Chicken Nuggets", "owner": "Aliaciana"},
    {"animal": "Cat", "name": "Whemingay", "appearance": "Orange Sleek fur", "favorite_food": "Mango Yogurt", "owner": "Arganaed"},
    {"animal": "Parrot", "name": "Panot", "appearance": "Colorful Shiny feathers", "favorite_food": "Sun Flower Seeds", "owner": "Arganaed"},
    {"animal": "Fish", "name": "Bang", "appearance": "Bright scales", "favorite_food": "little worms", "owner": "Solomon"},
    {"animal": "Rabbit", "name": "Bunny", "appearance": "Fat Long ears", "favorite_food": "Celery", "owner": "Ayana"}
]

# Loop through the list and print information about each pet, including their name, appearance, favorite food, and owner
for pet in pets:
    print(f"Pet: {pet['animal']}")
    print(f"Name: {pet['name']}")
    print(f"Appearance: {pet['appearance']}")
    print(f"Favorite Food: {pet['favorite_food']}")
    print(f"Owner: {pet['owner']}")
    print()  # Print a blank line to separate each pet's information
