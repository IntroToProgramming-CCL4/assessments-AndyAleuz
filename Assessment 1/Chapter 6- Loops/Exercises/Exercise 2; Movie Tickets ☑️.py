# Welcome to the Movie Ticket Pricing System! Get ready to embark on an age-based adventure.

while True:
    age_input = input("Please enter your age (or 'quit' to exit): ")

    if age_input.lower() == 'quit': #put this as a break when the user quit.
        break

    age = int(age_input)  # Move this line inside the loop to correctly handle age input.
    
    # Let's see if the user is qualified for a discount...

    if age < 3:
        print("Your ticket is free.")

    elif 3 <= age <= 12:
        print("Your ticket costs $10.")

    else:
        print("Your ticket costs $15.")

# That's a wrap, folks! Print your final outcome after inputing your age.
print("Thank you for using our program. Enjoy your movie.")
