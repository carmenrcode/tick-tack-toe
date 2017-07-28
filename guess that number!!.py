import random

goal = random.randint(0,25)

for i in range(0,6):
    guess = raw_input("Please enter a guess: ")
    guess = int(guess)

    if guess < goal:
        print "guess is too low"

    if guess > goal:
        print "guess is too high"

    if guess == goal:
        print "Congratulations! That is the correct answer"
        break
keystroke = raw_input("Press enter to exit")
