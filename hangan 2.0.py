word = "banana"
hidden = []
used = []
lives  = 6
stages = [" O\n_|_\n |\n/ \\",
          " O\n_|\n |\n/ \\",
          " O\n |\n |\n/ \\",
          " O\n |\n |\n/",
          " O\n |\n |\n",
          " O",
          ""]


for i in range(0,len(word)):
    hidden.append("_")


while lives > 0:
    #dont forget 2 draw.
    print "player:\n",stages[lives]

    print hidden
    guess = raw_input("Guess a letter: ")
    
    if not guess in used:
        used.append(guess)
    else:
        continue

    #if they guessed a correct letter 
    if guess in word:
        #replace underscore with that letter
        for j in range(0, len(word)):
            if word[j] == guess:
               hidden [j] = word [j]
    # if they were wrong
    else:
        lives -= 1
        if lives == 0:
            break

    if hidden.count('_') == 0:
        break

print "The word was:",word

if lives > 0:
    print "You Won!:D"

if lives == 0:
    print stages[0]
    print "You lost.:("
