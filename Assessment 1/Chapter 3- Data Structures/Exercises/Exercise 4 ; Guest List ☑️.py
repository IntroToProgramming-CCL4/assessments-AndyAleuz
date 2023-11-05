# Create a list of people you'd like to invite to dinner
guests = ["Albert Einstein", "Nikola Tesla", "Isaac Newton", "Galileo Galilei", "Leonardo da Vinci", "Marie Curie", "Charles Darwin"]

# Specify the details of the dinner event
event_date = "November 7, 2023"
event_location = "The Library of Congress, Washington, D.C"
invitor = "The Host Committee of Knowledge Society"

# Create a loop to repeatedly ask the user for names and display invitations
while True:
    guest_name = input("Please enter a name on the list (or 'q' to quit): ")
    
    if guest_name == 'q':
        print("You have exited the invitation list. Thank you for using the program!")
        break  # Exit the loop if 'q' is entered
    
    if guest_name in guests:
        invitation_message = f"Dear {guest_name},\n\nI am writing to extend a formal invitation to you for a dinner event. Your presence would be a great honor and privilege.\n\nThe dinner will take place on {event_date} at {event_location}. We anticipate an evening of engaging conversation and camaraderie.\n\nKindly confirm your attendance at your earliest convenience and let us know of your availability.\n\nWe are looking forward to your positive response and to spending a memorable evening together.\n\nSincerely,\n{invitor}\n"
        print(invitation_message)
    else:
        print("The entered name is not on the list, please Try Again")
