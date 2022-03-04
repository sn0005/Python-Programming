import random

def number_guesser(x):
 print(f'Think of number between 1 and {x}. Computer will try to guess the number')
 Low = 1
 High = x
 feedback = ''
 while feedback != 'y':
  guess = random.randint(Low, High)
  feedback = input(f'Is {guess} the number y/n :').lower()
  if feedback == 'n':
    prompt = input(f'Is the number guessed is too high (H) or too low (L) :').lower()
    if prompt == 'h':
     High = guess - 1
    elif prompt == 'l':
     Low = guess + 1
 print(f'Hurray Computer guessed {guess} correctly !!')

number_guesser(20)