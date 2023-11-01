# Cost of each USB stick is 6 punds as per the activity and the total budget in pounds is 50.
usb_stick_cost = 6
total_budget = 50

# Calculate how many USB sticks she can buy
usb_sticks_bought = total_budget // usb_stick_cost

# Calculate how many pounds she will have left by finding the remainder when her budget is divided by the cost of each USB stick.
pounds_left = total_budget % usb_stick_cost


# Display the results to the user, showing how many USB sticks she can buy and how much money she'll have remaining.
print("Given her initial budget of £50 and the cost of each USB stick at £6, this program calculates how many USB sticks she can buy and how much money she'll have left.")
print(f"She can buy {usb_sticks_bought} USB sticks.")
print(f"She will have £{pounds_left} left.")