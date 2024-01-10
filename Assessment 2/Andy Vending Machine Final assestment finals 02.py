import os

# ASCII Art to Welcome users of the vending machine.
greeting_message = """
*************************************************
  _    _  ____  __     ___  _____  __  __  ____   
 ( \/\/ )( ___)(  )   / __)(  _  )(  \/  )( ___)  
  )    (  )__)  )(__ ( (__  )(_)(  )    (  )__)   
 (__/\__)(____)(____) \___)(_____)(_/\/\_)(____)  
    Welcome to the Andy Aleuz Vending Machine!
        Grab a snack for your fright!
*************************************************
"""

# Define your vending machine items
andy_vending_machine = [
    {"code": "A01", "name": "Goldilocks Yema", "price": 2.50},
    {"code": "A02", "name": "Lemon Square Cupcake", "price": 1.50},
    {"code": "A03", "name": "Pastillas de Leche", "price": 3.00},
    {"code": "D10", "name": "Goldilocks Brownie Bites", "price": 1.25},
    {"code": "D11", "name": "ChocoLuxe Dark Chocolate Almond Brownies", "price": 4.00},
    {"code": "D12", "name": "Mama's Best Rocky Road Brownies", "price": 2.50},
    {"code": "B04", "name": "Kopiko 78°c", "price": 4.50},
    {"code": "B05", "name": "Milo Chocolate Drink", "price": 2.75},
    {"code": "B06", "name": "Nescafe 3 in 1 Coffee", "price": 3.25},
    {"code": "C07", "name": "Delmote Pineapple Juice", "price": 5.00},
    {"code": "C08", "name": "C2 Red Tea with Apple", "price": 3.75},
    {"code": "C09", "name": "C2 Cool and Clean Kiwi", "price": 2.00},
]

# Prices dictionary, this displays the dictionary as it is.
prices = {item["name"]: item["price"] for item in andy_vending_machine}

# Clear Screen Function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII Art Thank You Message with a boogie and a little scary comment (-_-)
User_thank_you_message = """
******************************************
  ____  _   _    __    _  _  _  _  ___ 
 (_  _)( )_( )  /__\  ( \( )( )/ )/ __)
   )(   ) _ (  /(__)\ (  ) | |  ( \__ |
  (__) (_) (_)(__)(__)(_)\_)(_)\_)(___/

    "You've chosen wisely! kabarkada, 
    Thanks a bunch for rolling inwith us!
******************************************
"""

# A function that computes and returns the change of the user
def calculate_change(overall_cost, money_entered):
    return max(0, money_entered - overall_cost)

# A function that prints the user receipt.
def print_receipt(bought_items, overall_cost):
    print("\nReceipt:")
    for item, quantity in bought_items.items():
        matching_codes = [code for code, name in prices.items() if name == item]
        if matching_codes:
            item_code = matching_codes[0]
            print(f"{item} - Code: {item_code} - AED {prices[item]:.2f} x {quantity} = AED {prices[item] * quantity:.2f}")
        else:
            print(f"{item} - AED {prices[item]:.2f} x {quantity} = AED {prices[item] * quantity:.2f}")
    print("overall Cost: AED {:.2f}".format(overall_cost))

# This is the Main program of the Vending machine
def main():
    clear_screen()
    print(greeting_message)

    # Initialize variables
    vending_user_money = float(input("\nEnter the amount of money you would like to spend in the Machine: AED "))
    bought_items = {}

    while True:
        clear_screen()

        # To Display the Available Goods given above.
        print("Available Goods:")
        for item in andy_vending_machine:
            print(f"{item['code']} - {item['name']} - AED {item['price']:.2f}")

        # Display the current cart
        if bought_items:
            print("\nCurrent Cart:")
            for item, quantity in bought_items.items():
                print(f"{item} - AED {prices[item]:.2f} x {quantity}")

        # A user input that asks the user for the code of the available product.
        user_input = input("\nEnter the code of the item you want to purchase (or press 'e' to exit): ").upper()

        if user_input == "E":
            # Confirm exit
            confirm_exit = input("Are you sure you want to exit? (y/n): ").lower()
            if confirm_exit == "y":
                break
            else:
                continue

        if user_input in [item["code"] for item in andy_vending_machine]:
            selected_item = next(item for item in andy_vending_machine if item["code"] == user_input)
            item_name = selected_item["name"]
            item_price = selected_item["price"]

                    # Check whether the user has enough money to proceed.
            if vending_user_money >= item_price:
                vending_user_money -= item_price

                # Add the item to the purchased items additional_choice_dictionary
                bought_items[item_name] = bought_items.get(item_name, 0) + 1

                # Additional Choices for the user to have the option to add more products
                additional_choice_dictionary = input("\nDo you want to add more items? (y/n): ").lower()
                if additional_choice_dictionary == "n":
                    break
            else:
                print("You have insufficient cash. Please add additional money to the machine.")
                input("\nPress Enter to continue...")
        else:
            print("Invalid input. Please enter a valid item code in display.")
            input("\nPress Enter to continue...")

    # User Checkout Process 
    overall_cost = sum(prices[item] * quantity for item, quantity in bought_items.items())
    change = calculate_change(overall_cost, vending_user_money)

    clear_screen()
    print("\nThis is your Final Cart:")
    for item, quantity in bought_items.items():
        print(f"{item} - AED {prices[item]:.2f} x {quantity}")

    print_receipt(bought_items, overall_cost)

    if change > 0:
        print("\nChange: AED {:.2f}".format(change))

    # Conclusion
    print(User_thank_you_message)

    # Ask if the user wants to use the machine again or exit
    repeat_choice = input("\nDo you want to use the Vending machine again? (y/n): ").lower()
    if repeat_choice == "y":
        main()  # Restart the program
    else:
        print("\nThank you! Have a great day!")

# Run the program
main()

           
