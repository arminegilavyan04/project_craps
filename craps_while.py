import random


def game():
    repetition = 0
    sum_value = 0
    while True:
        num1 = random.randrange(1, 7)
        num2 = random.randrange(1, 7)
        print(f"The sum of the dice is {num1} + {num2} = {num2 + num1}.")
        if repetition == 0 and num1 + num2 in [2, 3, 12]:
            return print("You lost")
        elif repetition == 0 and num1 + num2 in [7, 11]:
            return print("You won")
        elif repetition == 0:
            sum_value = num1 + num2
            print(f"Now your goal number is {sum_value}.")
        elif repetition != 0:
            if num1 + num2 == 7:
                return print("You lost")
            elif sum_value == num2 + num1:
                return print("You won")
        repetition = 1


game()