while True:
    # Prompt the user for input (age or "exit")
    user_input = input("Please enter the age (or type 'exit' to exit): ")

    # Check if the user wants to exit the program
    if user_input.lower() == 'exit':
        print("You have Exited the program.")
        break  # Exit the loop if the user types 'exit'

    # Convert the user input to an integer (age)
    age = int(user_input)

    # Determine the stage of life based on age
    if age < 2:
        print("The person is a baby.")
    elif age < 4:
        print("The person is a toddler.")
    elif age < 13:
        print("The person is a kid.")
    elif age < 20:
        print("The person is a teenager.")
    elif age < 65:
        print("The person is an adult.")
    elif age > 65:
        print("The person is an elder.")
    else:
    # This version fails the if test because it's not 'green'.
        pass