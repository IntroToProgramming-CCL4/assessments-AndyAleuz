# Create a dictionary of rivers and the countries they run through of cour the earth charrr...
rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China',
    'Mississippi': 'United States',
    'Danube': 'Germany',
    'Volga': 'Russia',
    'Ganges': 'India'
}

# Loop to print a sentence about each river the country where it flows
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# Loop to print the name of each river in the dictionary
print("\nList of rivers:")
for river in rivers.keys():
    print(river)

# Loop to print the name of each country in the dictionary
print("\nList of countries:")
for country in rivers.values():
    print(country)
