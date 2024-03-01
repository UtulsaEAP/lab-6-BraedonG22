"""
Name: Braedon Gehring
Lab Time: Friday, 3:00 pm
"""
def process_and_print(input_string):
      # Split into separate strings
  input_string = user_input.split()
    # Convert strings to integers and filter out negative values
  input_data = [int(x) for x in input_string]
  negatives = [num for num in input_data if num < 0]
    # Sort integers in reverse order
  negatives.sort(reverse=True)
    # Print sorted integers
  print(negatives)

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
