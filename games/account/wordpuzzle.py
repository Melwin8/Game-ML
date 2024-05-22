import random

# List of words for each difficulty level
easy_words = ["apple", "banana", "orange", "grape", "melon", "kiwi", "peach", "lemon"]
medium_words = ["elephant", "kangaroo", "giraffe", "rhinoceros", "zebra", "penguin", "hippopotamus"]
hard_words = ["magnificent", "extraordinary", "phenomenal", "impeccable", "incomprehensible", "unbelievable", "inconceivable"]

# Dictionary to map difficulty levels to word lists
difficulty_levels = {
    "easy": easy_words,
    "medium": medium_words,
    "hard": hard_words
}

def shuffle_word(word):
    """Function to shuffle the letters of a word"""
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

def choose_word(difficulty, used_words):
    """Function to choose a random word based on the difficulty level"""
    word_list = difficulty_levels[difficulty]
    available_words = [word for word in word_list if word not in used_words]
    if not available_words:
        if difficulty == "easy":
            print("Congratulations! You've completed the Easy level.")
            print("Moving on to the Medium level.")
            return choose_word("medium", [])
        elif difficulty == "medium":
            print("Congratulations! You've completed the Medium level.")
            print("Moving on to the Hard level.")
            return choose_word("hard", [])
        else:
            print("Congratulations! You've completed the Hard level.")
            print("You've completed all levels. Game Over!")
            exit()
    word = random.choice(available_words)
    return word

def game(difficulty):
    """Main game function"""
    score = 0
    level = 1
    used_words = []

    while True:
        # Choose a word and shuffle it
        original_word = choose_word(difficulty, used_words)
        used_words.append(original_word)  # Mark the word as used
        shuffled_word = shuffle_word(original_word)

        # Display level and shuffled word
        print(f"\nLevel: {level}")
        print(f"Shuffled word: {shuffled_word}")

        # Prompt for user input
        guess = input("Guess the original word: ").lower()

        # Check if guess is correct
        if guess == original_word:
            print("Correct!")
            score += 1
            level += 1
        else:
            print(f"Incorrect. The correct word was: {original_word}")

def main():
    """Main function"""
    print("Welcome to the Word Shuffle Challenge!")
    print("Select difficulty:")
    print("Press 'E' for Easy, 'M' for Medium, 'H' for Hard")

    difficulty = input().lower()
    if difficulty not in ["e", "m", "h"]:
        print("Invalid input. Please try again.")
        return

    if difficulty == "e":
        difficulty = "easy"
    elif difficulty == "m":
        difficulty = "medium"
    elif difficulty == "h":
        difficulty = "hard"

    game(difficulty)

if __name__ == "__main__":
    main()

# import random

# # List of words for each difficulty level
# easy_words = ["apple", "banana", "orange", "grape", "melon", "kiwi", "peach", "lemon"]
# medium_words = ["elephant", "kangaroo", "giraffe", "rhinoceros", "zebra", "penguin", "hippopotamus"]
# hard_words = ["magnificent", "extraordinary", "phenomenal", "impeccable", "incomprehensible", "unbelievable", "inconceivable"]

# # Dictionary to map difficulty levels to word lists
# difficulty_levels = {
#     "easy": easy_words,
#     "medium": medium_words,
#     "hard": hard_words
# }

# def shuffle_word(word):
#     """Function to shuffle the letters of a word"""
#     word_list = list(word)
#     random.shuffle(word_list)
#     return ''.join(word_list)

# def choose_word(difficulty, used_words):
#     """Function to choose a random word based on the difficulty level"""
#     word_list = difficulty_levels[difficulty]
#     available_words = [word for word in word_list if word not in used_words]
#     if not available_words:
#         return None, used_words  # No more words available in this difficulty
#     word = random.choice(available_words)
#     return word, used_words

# def game(difficulty):
#     """Main game function"""
#     score = 0
#     level = 1
#     used_words = []

#     while True:
#         # Choose a word and shuffle it
#         original_word, used_words = choose_word(difficulty, used_words)
#         if original_word is None:
#             if difficulty == "easy":
#                 print("Congratulations! You've completed the Easy level.")
#                 print("Moving on to the Medium level.")
#                 difficulty = "medium"
#                 used_words = []
#                 level = 1
#                 continue
#             elif difficulty == "medium":
#                 print("Congratulations! You've completed the Medium level.")
#                 print("Moving on to the Hard level.")
#                 difficulty = "hard"
#                 used_words = []
#                 level = 1
#                 continue
#             else:
#                 print("Congratulations! You've completed the Hard level.")
#                 print("You've completed all levels. Game Over!")
#                 break
        
#         used_words.append(original_word)  # Mark the word as used
#         shuffled_word = shuffle_word(original_word)

#         # Display level and shuffled word
#         print(f"\nLevel: {level}")
#         print(f"Shuffled word: {shuffled_word}")

#         # Prompt for user input
#         guess = input("Guess the original word: ").lower()

#         # Check if guess is correct
#         if guess == original_word:
#             print("Correct!")
#             score += 1
#             level += 1
#         else:
#             print(f"Incorrect. The correct word was: {original_word}")

# def main():
#     """Main function"""
#     print("Welcome to the Word Shuffle Challenge!")
#     print("Select difficulty:")
#     print("Press 'E' for Easy, 'M' for Medium, 'H' for Hard")

#     difficulty = input().lower()
#     if difficulty not in ["e", "m", "h"]:
#         print("Invalid input. Please try again.")
#         return

#     if difficulty == "e":
#         difficulty = "easy"
#     elif difficulty == "m":
#         difficulty = "medium"
#     elif difficulty == "h":
#         difficulty = "hard"

#     game(difficulty)

# if __name__ == "_main_":
#     main()