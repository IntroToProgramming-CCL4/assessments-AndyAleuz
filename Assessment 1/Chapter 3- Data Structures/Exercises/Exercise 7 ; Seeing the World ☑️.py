# Define the list of places you'd like to visit
places_to_visit = ["Australia", "Barbados", "Costa Rica", "Dominican Republic", "Ecuador"]

# Print the list in its original order
print("Original Order:", places_to_visit)

# Use sorted() to print the list in alphabetical order without modifying the actual list
print("Alphabetical Order:", sorted(places_to_visit))

# Show that the original list is still in its original order
print("Original Order:", places_to_visit)

# Use sorted() to print the list in reverse alphabetical order without changing the original list
print("Reverse Alphabetical Order:", sorted(places_to_visit, reverse=True))

# Show that the original list is still in its original order
print("Original Order:", places_to_visit)

# Use reverse() to change the order of the list
places_to_visit.reverse()
print("Reversed Order:", places_to_visit)

# Use reverse() to change the order of the list again to get back to the original order
places_to_visit.reverse()
print("Original Order:", places_to_visit)

# Use sort() to change the list to alphabetical order
places_to_visit.sort()
print("Sorted Alphabetical Order:", places_to_visit)

# Use sort() to change the list to reverse alphabetical order
places_to_visit.sort(reverse=True)
print("Sorted Reverse Alphabetical Order:", places_to_visit)
