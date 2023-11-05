# Create a list of people you'd like to invite to dinner
guests = ["Albert Einstein", "Nikola Tesla", "Isaac Newton", "Galileo Galilei", "Leonardo da Vinci", "Marie Curie", "Charles Darwin"]

# Specify the details of the dinner event
event_date = "November 7, 2023"
event_location = "The Library of Congress, Washington, D.C"
invitor = "The Host Committee of Knowledge Society"

# Create a loop to ask the user for names and display invitations repeatedly
while True:
    guest_name = input("Please enter a name on the list (or 'q' to quit): ")
    
    if guest_name == 'q':
        print("You have exited the invitation list. Thank you for using the program!")
        break  # Exit the loop if 'q' is entered
    
    if guest_name in guests:
        if guest_name == "Marie Curie":
            # Create an engaging message about Marie Curie's absence
            print(f"Unfortunately, {guest_name} sends her apologies and can't make it to the dinner. She's currently in the lab, conducting groundbreaking experiments.")
            
            # Remove Marie Curie from the guest list
            guests.remove(guest_name)
            
            # Invite a new guest to replace Marie Curie
            new_guest = input("Who would you like to invite in her place? Please enter the new guest's name: ")
            guests.append(new_guest)
            
            # Display a formal invitation to the new guest
            invitation_message = f"Dear {new_guest},\n\nI am writing to extend a formal invitation to you for a dinner event. Your presence would be a great honor and privilege. The dinner will take place on {event_date} at {event_location}. We anticipate an evening of engaging conversation and camaraderie. Kindly confirm your attendance at your earliest convenience and let us know of your availability. We are looking forward to your positive response and to spending a memorable evening together.\n\nSincerely,\n{invitor}\n"
            print(invitation_message)
        else:
            # Send an invitation to the original guest
            invitation_message = f"Dear {guest_name},\n\nI am writing to extend a formal invitation to you for a dinner event. Your presence would be a great honor and privilege. The dinner will take place on {event_date} at {event_location}. We anticipate an evening of engaging conversation and camaraderie. Kindly confirm your attendance at your earliest convenience and let us know of your availability. We are looking forward to your positive response and to spending a memorable evening together.\n\nSincerely,\n{invitor}\n"
            print(invitation_message)
    else:
        print("The entered name is not on the list.")

# Print a second set of invitations for the remaining guests
print("\nSecond Set of Invitations:")
for guest in guests:
    invitation_message = f"Dear {guest},\n\nI am writing to extend a formal invitation to you for a dinner event. Your presence would be a great honor and privilege. The dinner will take place on {event_date} at {event_location}. We anticipate an evening of engaging conversation and camaraderie. Kindly confirm your attendance at your earliest convenience and let us know of your availability. We are looking forward to your positive response and to spending a memorable evening together.\n\nSincerely,\n{invitor}\n"
    print(invitation_message)
