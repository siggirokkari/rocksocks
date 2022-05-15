import random
while True:
    print("Welcome to Guess The Number!")
    print("The game chooses one whole number from a range you choose (starting and ending number inclusive)")
    print("Then you try to guess that number, and the game will give you clues along the way.")
    print("Good luck and have fun!")

    range_start = 0
    range_end = 0

    while True:
        input_range_start = input("Type start of your range: ")
        if input_range_start.isdigit():
            range_start = int(input_range_start)
            break
        else:
            print("Wrong input, type only numbers.")
            continue

    while True:
        input_range_end = input("Type end of your range: ")
        if input_range_end.isdigit():
            range_end = int(input_range_end)
            break
        else:
            print("Wrong input, type only numbers.")
            continue

    guess_num = 0
    num_to_guess = random.randrange(range_start,range_end+1)
    print("I have chosen a number! Let's begin!")

    while True:
        num_guess = input("Guess the number! ")
        while True:
            if num_guess.isdigit():
                num_guess = int(num_guess)
                break
            else:
                print("Wrong input, type only numbers.")
                continue
        
        if num_guess == num_to_guess:
            print("You are right! I did choose the number", num_to_guess,"!")
            guess_num += 1
            break

        elif num_guess < num_to_guess:
            print("That is not correct! The number I chose is higher!")
            guess_num += 1
            continue

        else:
            print("That is not correct! The number I chose is lower!")
            guess_num += 1
            continue

    print("Game over!")
    print("It took you", guess_num, "guesses to find the correct number!")
    again = input("Want to play again? (yes or no)")
    if again == "yes":
        continue
    else:
        break
