"""
Name: Braedon Gehring
Lab Time: Friday, 3:00 Pm
"""

def food_input():
    user_input = input()
    tokens = user_input.split()
    #type you while  loop here
    printed = False
    while True :
        if tokens[0] == 'quit' :
            break
        elif not printed:
             print(f'Eating' , tokens[1] + ' ' + tokens[0] , 'a day keeps you happy and healthy.') 
        printed = True
           
    

if __name__ == "__main__":
    food_input()
