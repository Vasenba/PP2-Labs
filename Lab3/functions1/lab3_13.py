import random

print("Hello! What is your name?")
name = str(input())

num = random.randint(1, 20)

cnt = 0
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
while True:
    print("Take a guess.")  
    a = int(input())
    if (a > num):
        print("Your guess is too high")
        cnt += 1
    elif (a < num):
        print("Your guess is too low")
        cnt += 1
    elif (a == num):
        print("Good job, ", name, "! You guessed my number in ", cnt, " guesses!")
        break
