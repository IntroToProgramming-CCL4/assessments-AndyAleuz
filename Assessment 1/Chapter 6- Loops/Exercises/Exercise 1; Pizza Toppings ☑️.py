# Create an empty list to store pizza toppings...
pizza_toppings = []

# Start an infinite loop to collect pizza toppings from the users input.
while True:
    # Prompt the user to enter a pizza topping (or 'quit' to finish)
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    # Check if the user entered 'quit' to exit the loop..
    if topping.lower() == 'quit':
        break  # Exit the loop if 'quit' is entered
    
    # Add the entered topping to the list of pizza toppings by typing in.
    pizza_toppings.append(topping)
    
    # Print a message indicating the topping will be added to the pizza.
    print(f"You'll add {topping} to your pizza.")

# Check if there are any pizza toppings in the list
if pizza_toppings:
    # If toppings are present, print a message listing the toppings of all the users have added,
    print("\nYour pizza will have the following toppings:")
    
    # Loop through the list of pizza toppings and print each topping
    for topping in pizza_toppings:
        print(topping)
