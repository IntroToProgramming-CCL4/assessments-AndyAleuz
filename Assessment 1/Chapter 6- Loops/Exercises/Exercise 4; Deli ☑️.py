# Create a list of sandwich orders heheheh search the internet.
sandwich_orders = ["Bacon cheese Burger", "Turkey Club", "BLT", "Roast Beef Sandwich.", "Grilled Cheese", "Nutella Sandwich"]

# Create an empty list for finished sandwiches using equeals and brackets
finished_sandwiches = []

# Loop through the list of sandwich orders using a while loop.
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"Your Order has arrived, one {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print the list of finished sandwiches.
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
