# Create a list of sandwich orders with 3'pastrami' appearing at least three times in the Order.
sandwich_orders = [
    "Tuna", "Pastrami", "Chicken", "Pastrami", "Veggie",
    "Pastrami", "Ham and Cheese", "Turkey Club", "Pastrami"
]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Announce that the Restaurant has run out of pastrami HUHUHUHUHU :(
print("Sorry, the deli has run out of pastrami sandwiches.")

# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

# Loop through the list of sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f"Your Order is served, {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print the list of finished sandwiches.... TaPOS NAH
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
