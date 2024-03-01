"""
Name: Braedon Gehring
Lab Time: Friday, 3:00 pm
"""
def process_input(user_input):
      # Split into separate strings
  input_string = user_input.split()
    # Convert strings to floats
  input_string = [eval(x) for x in input_string]
    # Get max and average
  max_value = format(max(input_string),".2f")
  average_value = format((sum(input_string)/len(input_string)),".2f")
  return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(max_value,average_value)
