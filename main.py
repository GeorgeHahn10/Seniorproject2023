
from random import random

import request

x = random()
print(x)
y = input("enter max number: ")
print(y)
print(int(x * int(y)))
# This is a comment
english_greeting = "Hello "
print(english_greeting)
print(english_greeting + "Mister.")
print((english_greeting + "Mister.") * 5)
spanish_greeting = "Hola "
len(spanish_greeting)
print(len(spanish_greeting))
print("The maximum number in a range of 1 numbers is, {}, this value multiplied by the maximum number in the range is, {}.".format(y, x))
name = "George"
name.lower()
print(name.lower())
name.count("e")
print(name.count("e"))

print(int("5"))
print(int("5") + int("7"))

print("Hi George, how was your day on a scale of 1 to 10")
num = input("Enter Number:123")
print(num)

vacation = "Florida"
print(vacation[-1])
print(vacation[0:4])

over_18 = True
over_21 = False
print(over_18 and over_21)
print(over_18 or over_21)
print(not over_21)

age = 35
print(age < 33)
print(6 == "6")
print(6 == int("6"))
print("test: " + str(bool("Los Angeles" < "Zimbabwe")))
if age > 25:
    print("You cannot legally rent a car")
if age == 35:
    print("I am getting older.")


on_base_probability = .500
o = on_base_probability
if x > o:
    print("We are going to draft you to the Pittsburgh Pirates.")
else:
    print("Sorry you are not good enough to play in the MLB.")

first_divisor = 24
second_divisor = 36
counting = True
i = 1
while counting:
    if i % first_divisor == 0 and i % second_divisor == 0:
        break
    i += 1
print("The Least Common Multiple of", first_divisor, "and", second_divisor, "is", i, ".")

r = request.reqeust("IBM")






