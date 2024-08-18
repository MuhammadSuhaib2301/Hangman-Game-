                            # TASK #01 : DESIGN TEXT-BASED  HANGMAN GAME
print("****************************************TASK #01****************************************************")
import random 
def select_word():
    words_list=["journey","puzzle","velocity","force","mountain","coding","python","programming","galaxy","gravity"]
    return random.choice(words_list)

def display_words(word, guess_letter):
    return " ".join([letter 
                     if letter in guess_letter 
                      else "_" for letter in word ])

def hangman_game():
    word= select_word()
    guessed_letters= set()
    incorrect_guess=0
    max_incorrect_guesses=6

    print("WELCOME TO HANGMAN GAME!")
    print("You have to guess the wird one letter at a time")
    print(f"You hav{max_incorrect_guesses} incorrect guesses allowed")

    while incorrect_guess < max_incorrect_guesses:
        print("\nCorrect word: ", display_words(word,guessed_letters))
        guess= input("Guess a letter: ").lower()

        if len(guess) !=1 or not guess.isalpha():
            print("Please Enter a Single Letter: ")
            continue

        if guess in guessed_letters:
            print("You have Already Guess that Letter")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("GOOD GUESS!")
            if all(letter in guessed_letters for letter in word):
                print(f"CONGRATULATION YOU HAVE GUESS THE WORD: {word}")
                break
        else:
            incorrect_guess+=1
            print(f"INCORRECT GUESS! You  have {max_incorrect_guesses - incorrect_guess} INCORRECT GUESS LEFT")
    
    if incorrect_guess == max_incorrect_guesses:
        print(f"SORRY YOU HAVE RUN OUT OF GUESSES THE WORD WAS : {word} ")
if __name__ == "__main__":
    hangman_game()