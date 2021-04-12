# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

names_random1 = random.choice(names)


print(f"{names_random1} is goint to buy the meal today!")

names_random2 = names[random.randint(0, len(names)-1)]

print(f"{names_random2} is goint to buy the meal today!")