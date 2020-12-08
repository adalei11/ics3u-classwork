from typing import List

from words import WORD_LIST


def main():
    ATTEMPTS_ALLOWED = 6

    secret_word = get_random_word(WORD_LIST)

    correct_guesses = []
    incorrect_guesses = []
    lives = calc_attempts_remaining(ATTEMPTS_ALLOWED, incorrect_guesses)

    result = None
    while result is None:

        # display lives left
        print_lives_left(lives, ATTEMPTS_ALLOWED)

        # display hidden word
        blanked_word = reveal_letters(secret_word, correct_guesses)
        print(blanked_word)
        print()

        # get guess
        guess = get_guess(correct_guesses + incorrect_guesses)

        if letter_is_in_word(guess, secret_word):
            print("That is correct!")
            correct_guesses.append(guess)
        else:
            print("Incorect.")
            incorrect_guesses.append(guess)
        
        lives = calc_attempts_remaining(ATTEMPTS_ALLOWED, incorrect_guesses)
        
        if all_letters_present_in_list(secret_word, correct_guesses):
            result = "win"
        elif lives <= 0:
            result = "lose"

    print(word_reveal_message(secret_word))
    print(outcome_message(result))


def get_random_word(word_list: list) -> str:
    
    return random.choice(word_list)




def print_lives_left(remaining: int, out_of: int):
    return(f"You have {remaining} lives left out of {out_of}")



def reveal_letters(word: str, visible_letters: List[str]) -> str:
    hidden_word = ""
    for letter in word:
        if letter in visible_letters:
            hidden_word += letter
        else:
            hidden_word += "_"
        hidden_word += " "
    return hidden_word.strip()
  


def calc_attempts_remaining(attempts_allowed: int, incorrect: List[str]) -> int:
    return attempts_allowed - len(incorrect)



def word_reveal_message(word: str) -> str:
    return f"The secret word was '{word}'."



def outcome_message(result: str) -> str:
  if result == "win":
    return "You win!"
  else:
    return "You lose!"



def get_guess(all_guesses: List[str]) -> str:
    while True:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        letter = input("Please enter a letter to guess: ")
        if letter not in all_guesses and len(letter) == 1 and letter in alphabet:
            return letter
        elif letter in all_guesses:
            print("you already tried this")
        elif len(letter) != 1:
            print("error string inputed > 1 letter")
        else:
            print("not a letter")
        print()


def letter_is_in_word(letter: str, word: str) -> bool:
    return letter in word 



def all_letters_present_in_list(word: str, letter_list: List[str]) -> bool:

    for i in range(len(word)):
        if word[i] not in letter_list:
            return False
    return True


if __name__ == "__main__":
    main()
