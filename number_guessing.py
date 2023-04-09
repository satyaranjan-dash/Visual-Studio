import random
print("WeLcOmE tO tHe GuEsSiNg GaMe")

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("Kudos! You got it right!")
        break
    elif user_guess > random_number:
        print("Opps! You were above the number!")
    else:
        print("Opps! You were below the number!")
print("Lucky! You got it right in", guesses, "guesses.")