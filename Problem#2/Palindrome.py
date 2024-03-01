"""
Name: Braedon Gehring
Lab Time: Friday, 3:00 pm
"""
def check_palindrome(user_input):
 #type your code here
    user_input = user_input.replace(" ","").lower()
    if user_input == user_input[::-1] :
        print("palindrome: " + user_input)
    else :
        print("not a palindrome: " + user_input)
    return user_input == user_input[::-1]
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
