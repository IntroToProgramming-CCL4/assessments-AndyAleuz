# Create a variable for a person's name with whitespace characters to check the strip functions.
name = "\t   Andrea Cyra Valenzuela Bautista   \n"

# Print the name once to display the whitespace around the name to check the output with out the strip
print("Name with whitespace:", name)

# Print the name after using lstrip() function is used to remove leading (leftmost) whitespace
print("Name after lstrip():", name.lstrip())

# Print the name after using rstrip() function is used to remove leading (righttmost) whitespace
print("Name after rstrip():", name.rstrip())

# Print the name after using strip() to remove both left and right whitespace or empty space.
print("Name after strip():", name.strip())