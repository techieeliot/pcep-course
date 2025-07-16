import random

make_int = random.randint(1,4)

print("Random integer:", make_int)


wager = input("How much do you want to wager? ")

multiplier = random.randint(-1, 100)

result = int(wager) * multiplier
