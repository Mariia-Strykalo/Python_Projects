WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


def main():
    print("Welcome to Spelling Bee!")
    for words, points in WORDS.items():
        print(F"{words} was worth {points} points.")

main()




#WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}


#def main():
    #print("Welcome to Spelling Bee!")
    #print("Your letters are: A I P C R H G")

    #while len(WORDS) > 0:
        #print(f"{len(WORDS)} words left!")
        #guess = input("Guess a word: ")

        #if guess == "GRAPHIC":
            #WORDS.clear() # очищаємо словник повністю
            #print("You've won!")
        #if guess in WORDS.keys():
            #points = WORDS.pop(guess) # видаляємо слово та беремо його значення (очки)
            #print(f"Good job! You scored {points} points.")

    #print("That's the game!")

#main()
