import random
while True:
    user_input = input("Enter 'd' to generate a random number: ")
    if user_input.lower() == 'd':
        random_number = random.randint(1,6)
        print("Random number:", random_number)
    elif user_input.lower() != '':
        print("Invalid input. Please enter 'd' to generate a random number.")
    else:
        break
