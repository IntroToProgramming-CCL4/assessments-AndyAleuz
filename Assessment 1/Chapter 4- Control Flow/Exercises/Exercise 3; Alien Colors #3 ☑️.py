# Ask the user for the alien's color
alien_color = input("Enter the color of the alien (green, yellow, or red): ")

if alien_color == 'green':
    print("Player just earned 5 points for shooting a green alien.")
elif alien_color == 'yellow':
    # This version passes the if test for 'yellow'.
    print("Player just earned 10 points for shooting a yellow alien.")
elif alien_color == 'red':
    # This version passes the if test for 'yellow'.
    print("Player just earned 15 points for shooting a red alien.")
else:
    # This version fails the if test because it's not 'green'.
    pass