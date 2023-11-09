# Define a lambda function called 'make_shirt' that accepts two parameters: 'size' and 'message'.
make_shirt = lambda size, message: print(f"Shirt size: {size}, Message: {message}")

# Call the 'make_shirt' function using positional arguments.
# Here, we provide the size "Large" and the message "“Consuelo de bobo”" as positional arguments.
make_shirt("Large", "“Consuelo de bobo”")

# Call the 'make_shirt' function using keyword arguments.
# Here, we provide the size as a keyword argument "Medium" and the message as a keyword argument "“Repapips”"
make_shirt(size="Medium", message="“Repapips”")
