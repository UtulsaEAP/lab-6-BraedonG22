def process_user_contacts(user_input):
    user_contacts = user_input

 
    user_input = user_input
    tokens = user_contacts.split(", ")

    # Put word pairs into a dictionary
    word_pairs = {'Joe': 123-4532, 'Linda': 983-4123, 'Frank': 867-5309}
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    print(word_pairs[contact_name])
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
