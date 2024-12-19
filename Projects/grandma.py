guesses = 0
while True:
    word = input("What do you think grandma likes? ")

    if len(word) < 10:
        print(f"Grandma doesn't like {word}!")
    else:
        print(f"Grandma likes {word} <3")

    print("")
    
    guesses +=1

    if guesses == 10:
        why = input("Is the rule: A. The word has to be greater than 10 letters, B. The word has to have double letters, or C. The word has to have the letter T in it?")

        if why == "A":
            print(f"YES!")
            break
        else:
            print(f"oh, so close! try again next time!")
            break
