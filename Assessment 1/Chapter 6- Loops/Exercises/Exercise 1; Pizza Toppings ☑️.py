pizza_toppings = []

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    pizza_toppings.append(topping)
    print(f"You'll add {topping} to your pizza.")

if pizza_toppings:
    print("\nYour pizza will have the following toppings:")
    for topping in pizza_toppings:
        print(topping)
