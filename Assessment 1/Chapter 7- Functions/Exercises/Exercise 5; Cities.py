# Define a lambda function called 'describe_city' that accepts two parameters: 'city' and 'country' with a default value.
describe_city = lambda city, country="Country": print(f"{city} is in {country}")

# Call the lambda function to describe three different cities:
# 1. Reykjavik in Iceland
describe_city("Reykjavik", "Iceland")

# 2. Paris in the default country (since 'country' is not provided)
describe_city("Paris")

# 3. Tbilisi in Georgia 
describe_city("Georgia", "Tbilisi")

# 4. Cebu in Philipppines
describe_city("New York", "Philippines")
