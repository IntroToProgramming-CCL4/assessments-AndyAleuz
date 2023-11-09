# Define a lambda function called 'make_shirt'.
make_shirt = lambda size="Large", message="I love Python": print(f"Shirt size: {size}, Message: {message}")

# Create a large shirt with the default message
make_shirt()

# Create a medium shirt with the default message
make_shirt("Medium")

# Create a small shirt with a custom message
make_shirt("Small", "Keep Coding EMEH!")
