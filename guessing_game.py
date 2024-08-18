import random
def game():
    number_to_guess =random.randint(1,50)
    print(number_to_guess)
    print('welcome to number guessing game..!')
    print('i have chosen a number can you guess it correctly...!')

attempts=0

while guess != number_to_guess:   
    
    guess=int(input("enter the number...!"))
    
    attempts+=1

    if guess< number_to_guess :
        print("number is too low...!")

    elif guess>number_to_guess:
        print("number is too high...!")

    else:
        print('congratulations,your guess is correct..!')
        print('your attempts are:-',attempts)