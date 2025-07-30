print("final project")


import random

def guess_the_number():


    first_number = int(input("Enter first number range: "))
    second_number = int(input("Enter second number range: "))

    correct_answer = random.randint(first_number, second_number)
    attmept = 0

    while True:
        try:
            guess = int(input("Guess the number: "))
            attmept += 1

            if guess > correct_answer:
                print("try lower")
            elif guess < correct_answer:
                print("try higher")
            elif guess == correct_answer:
                print(f"correct numer was {correct_answer} \nyou guessed correct number in {attmept} attmept")
                break
        except ValueError:
            print("Sorry, you didn't enter a number.")


guess_the_number()