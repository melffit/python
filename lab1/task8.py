import random
number = random.randint(1, 100)
print("Я загадал число от 1 до 100, угадай его")
while True:
    guess = int(input("твоя догадка: "))
    if guess < number:
        print("больше")
    elif guess > number:
        print("меньше")
    else:
        print("ты угадал")
        break