import random
first_try = random.randrange(1, 7)
second_try = random.randrange(1, 7)
sum_try = first_try + second_try


def win():
    return f'''The sum of dice is {first_try} + {second_try} = {sum_try}
     You won.'''


def lose():
    return f'''The sum of dice is {first_try} + {second_try} = {sum_try}
    You lose.'''


def roll():
    first_goal_try = random.randrange(1, 7)
    second_goal_try = random.randrange(1, 7)
    sum_goal_try = first_goal_try + second_goal_try
    return sum_goal_try


def goal():
    roll_value = roll()
    if roll_value == sum_try:
        return f"""The sum of dice is {roll_value}.
    You won"""
    else:
        if roll_value == 7:
            return f"""The sum of dice is {roll_value}.
    You lost"""
        else:
            print(f"The sum of the dice is {roll_value}")
            return goal()


def dice():
    if sum_try == 7 or sum_try == 11:
        return win()
    elif sum_try == 2 or sum_try == 3 or sum_try == 12:
        return lose()
    else:
        print(f"""The sum of the dice is {first_try} + {second_try} = {sum_try}.
Now your goal number is {sum_try} """)
        return goal()


print(dice())