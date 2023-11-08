# Create a glossary (dictionary) for programming terms and their meanings. (Dapat maganda yung meaning :) )
programming_glossary = {
    "Variable": "A container that stores data and can be referenced by a name.",
    "Function": "A reusable block of code that performs a specific task or set of tasks.",
    "Loop": "A control structure that repeats a block of code until a certain condition is met.",
    "List": "A collection of ordered elements that can be of different data types.",
    "Conditional Statement": "A structure that allows you to make decisions in your code based on a condition.",
    "Dictionary": "A collection of key-value pairs used to store and retrieve data efficiently.",
    "Module": "A Python file containing reusable code that can be imported and used in other programs.",
    "String": "A sequence of characters, typically used to represent text in programming.",
    "Boolean": "A data type that can have one of two values: True or False.",
    "Exception": "An error that occurs during the execution of a program, which can be handled or left to halt the program."
}

# Print each programming term and its meaning with a newline between each pair using a loop.
for term, meaning in programming_glossary.items():
    print(f"{term}:\n{meaning}\n")
