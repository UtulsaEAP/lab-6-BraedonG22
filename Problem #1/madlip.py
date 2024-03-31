"""
Name: Braedon Gehring
Lab Time: Friday, 3:00 Pm
"""

def food_input():
    user_inputs = []
    
    while True:
        user_input = input()
        tokens = user_input.split()
        if tokens[0] == 'quit':
            break
        else:
            user_inputs.append(user_input)
            print('Eating' , tokens[1] + ' ' + tokens[0] , 'a day keeps you happy and healthy.')
            
    
if __name__ == "__main__":
    food_input()
