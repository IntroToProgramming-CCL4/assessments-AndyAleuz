# Create a list of people you'd like to invite to dinner
guests = ["Albert Einstein", "Nikola Tesla", "Isaac Newton", "Galileo Galilei", "Leonardo da Vinci", "Marie Curie", "Charles Darwin"]

# Specify the details of the dinner event
event_date = "November 7, 2023"
event_location = "The Library of Congress, Washington, D.C"
invitor = "The Host Committee of Knowledge Society"

# Print a message that only two people can be invited
print("Dear Guests, due to limited seating, we can only invite two people for dinner. We apologize for any inconvenience.\n")

# Use pop() to remove guests from your list one at a time until only two names remain
while len(guests) > 2:
    guest = guests.pop()
    print(f"Regrettably, {guest}, we can't invite you to the dinner this time. We hope to see you at future events.\n")

# Print a message to the two people still on your list
print("Invitations have been extended to the following guests:\n")
for guest in guests:
    invitation_message = f"Dear {guest},\n\nYou are cordially invited to the dinner event. Your presence would be a great honor and privilege. The dinner will take place on {event_date} at {event_location}. We anticipate an evening of engaging conversation and camaraderie. Kindly confirm your attendance at your earliest convenience and let us know of your availability. We are looking forward to your positive response and to spending a memorable evening together.\nSincerely,\n{invitor}\n"
    print(invitation_message)

# Use del to remove the other names from your list
del guests[2:]

# Print the final guest list with only two names
print("\nUnfortunately, we can only accommodate two guests for this dinner. The final guest list includes:\n")
for guest in guests:
    print(guest)

# Empty the list
guests = []

# Print your updated guest list, which is now empty
print("\nUpdated guest list:", guests)
