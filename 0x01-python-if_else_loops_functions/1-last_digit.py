#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number2 = number * -1
else:
    number2 = number
if (number2 % 10) > 5:
    print("Last digit of {:d} is {:d}".format(number, (number2 % 10)), "and is greather than 5")
elif (number2 % 10) == 0:
    print("Last digit of {:d} is {:d}".format(number, (number2 % 10)), "and is 0")
else:
    print("Last digit of {:d} is {:d}".format(number, (number2 % 10)), "and is less than 6 and not 0")
