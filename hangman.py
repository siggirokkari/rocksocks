import random
import hangman_definitions
while True:
 
    word_list = hangman_definitions.create_word_list("5Letters.txt") #create word list

    word_to_guess = word_list[random.randrange(0,len(word_list))].upper() #choose one word at random from the word_list
    word_to_guess_length = len(word_to_guess)

    lives = 7 # Lives the player has. eg number of guessses.
    print("Welcome to HANGMAN!")
    print("I have chosen a", word_to_guess_length, "character long word and you have", lives, "guesses to guess the word! Good Luck!")

    guessed_char = []   #Empty list for characters already guessed
    word_so_far = "_" * word_to_guess_length    #String to show the word with characters guessed correctly

    while True:
        if "_" in word_so_far: #Check if the word is complete
            while True:         #Check if input is more than one character
                guessed_char.sort()
                print("Characters already guessed:", guessed_char)
                print("The word so far:", word_so_far)
                char_guess = input("Guess a character: ").upper()       
                if len(char_guess) == 1:
                    break
                else:
                    print("Only write one character.")
                    continue
            if char_guess not in guessed_char:  #Check if the character has already been guessed
                if char_guess in word_to_guess:     #Check if character is in the word,
                    char_count = word_to_guess.count(char_guess)    #Check how many times the character is in the word
                    print("The word does contain",char_guess,char_count,"times.")
                    guessed_char.append(char_guess)     #Put the character in the already guessed list
                    inner_str = ""
                    for i in range(len(word_to_guess)):     #Create the display string for the word so far
                        if word_to_guess[i] == char_guess:
                            inner_str += word_to_guess[i]
                        else:
                            if word_so_far[i] == "_":
                                inner_str += "_"
                            else:
                                inner_str += word_so_far[i]
                    word_so_far = inner_str

                elif char_guess not in word_to_guess and lives > 1:     #Check if player any guesses left
                    print("The character is not in the word.")
                    lives -=1
                    print("You have",lives," lives left!")
                    guessed_char.append(char_guess)

                elif char_guess not in word_to_guess and lives == 1:    #Last wrong guesso

                    print("The character is not in the word and this was your last guess!")
                    print("The word was:",word_to_guess)
                    print("Game Over! You Lost!")
                    break
            else:
                print("You have already guessed this character! Try another one.")
                continue
        else:
            print("You found the Word! It is:", word_so_far)
            print("You Won! Congratulations!")
            break
    

    play_again = input("Do you want to play again? (yes or no) ")

    if play_again == "yes":
        continue
    else:
        break
