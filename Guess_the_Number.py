import random

def guess_the_number(x):
    Low = 1
    High = x
    number = random.randint(Low, High)
    feedback = 0
    while feedback != number:
     feedback = int(input('Can you guess the Number?? :'))
     if feedback < number:
      print(f'{feedback} is too low from THE number')
     elif feedback > number:
      print(f'{feedback} is too high from THE number')
    
    print(f'Hurray you guessed {number} correctly !!')

guess_the_number(10)