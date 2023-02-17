#!/user/bin/python

print("Welcome to the DUMB DOG QUIZ!")
answer = input("Would you like to take the quiz? (yes or no): ")

if answer.lower() == "yes":
    height = int(input("What is your height in inches?: "))
    weight = int(input("What is your weight in pounds?: "))
    size = height * weight
    if size >= 1000:
        print("You are a large dog!")
    elif size <=999 and size >=600 :
        print("You are a medium-sized dog!")
    else:
        print("You are a small dog!")
else:
    print("Okay, have a nice day!")














