"""
Name: Braedon Gehring
Lab Time: Friday, 3:00 pm
"""
def process_and_print(user_input):
      # Split into separate strings
  input_data = sorted([int(x) for x in user_input.split() if int(x) < 0], reverse = True)
    # Sort integers in reverse order

  for num in input_data : 
    print(num, end=' ')


if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
