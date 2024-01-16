#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digitlast = number % -10
else:
    digitlast = number % 10
if digitlast > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, digitlast))
elif digitlast < 6 and digitlast != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, digitlast))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
