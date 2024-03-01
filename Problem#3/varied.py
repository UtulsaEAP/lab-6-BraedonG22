"""
Name: Braedon Gehring
Lab Time: Friday, 3:00 pm
"""
def process_input(input_string):
      # Split into separate strings
  input_string = user_input.split()
    # Convert strings to floats
  input_string = [float(x) for x in input_string]
    # Get max and average
  max_value = max(input_string)
  average_value = (sum(input_string)/len(input_string))
  return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
