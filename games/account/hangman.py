import openai
import random
import time

# Set up your OpenAI API key (replace with your actual key)

word_list = [
    "apple", "beautiful", "potato", "orange", "mango", "malayalam", "happy","blood","album","magic","brick","chicken","helicopter","furniture","television",
    "aeroplane", "peacock", "earth", "mother", "lotus", "penguin", "dove","ambassador","autonomous","basketball","blackberry",
    "monkey", "quilt", "computer", "mathematics", "watch","dress","fruit","glass","eagle","criminal","customer","manuscript","meditation",
    "children","homeless","medicine","lightning","thunder","marriage","princess","bathroom","makeup","money","industry",
    "selfish","cigarette","lipstick","scissors","passport","notebook","laptop","toothbrush","headphone","newspaper","magazine",
    ""
]

def generate_hint(word):
    """Generates a hint for the chosen word using OpenAI's gpt-3.5-turbo-instruct engine.

    Args:
        word: The word to generate a hint for.

    Returns:
        A string containing the generated hint, or an error message if the request fails.
    """

    prompt = f"What are the characteristics of the word '{word}' without explicitly showing the word in just 1 or 2 small sentence?"
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5
        )
        return response.choices[0].text.strip()
    except openai.OpenAIError as e:
        print(f"Error generating hint: {e}")
        return "Failed to generate hint. Please try again later."

def select_word(difficulty):
    """Selects a word from the word list based on the chosen difficulty.

    Args:
        difficulty: The desired difficulty level ("easy", "medium", or "hard").

    Returns:
        The chosen word, or None if an invalid difficulty is selected.
    """

    if difficulty == "easy":
        return random.choice([word for word in word_list if len(word) <= 5])
    elif difficulty == "medium":
        return random.choice([word for word in word_list if 6 <= len(word) <= 7])
    elif difficulty == "hard":
        return random.choice([word for word in word_list if len(word) >= 8])
    else:
        print("Invalid difficulty level. Please choose between easy, medium, or hard.")
        return None

def main():
    """Runs the Hangman game loop."""

    difficulty = input("Choose difficulty level (easy, medium, hard): ").lower()
    chosen_word = select_word(difficulty)

    if chosen_word:
        # Initialize score and timer based on difficulty
        if difficulty == "easy":
            score = 10
            total_time = 60
        elif difficulty == "medium":
            score = 20
            total_time = 45
        elif difficulty == "hard":
            score = 30
            total_time = 30

        lives = 7
        display = ["_"] * len(chosen_word) 

        print("Welcome to Hangman!")
        print(f"The word has {len(chosen_word)} letters.")
        print(f"Total time allowed: {total_time} seconds")

        hint = generate_hint(chosen_word)
        print("Hint:", hint)  # Provide hint generated by OpenAI

        print(" ".join(display))  # Display the initial word representation

        # Start time for tracking game duration
        start_time = time.time()
        # Initialize game_over flag to indicate ongoing game
        game_over = False
        # Loop continues until game_over becomes True
        while not game_over:
            if time.time() - start_time > total_time:
                print(f"Time's up!\nThe word was: {chosen_word}")
                game_over = True
                break
            guessed_letter = input("Guess a letter: ").lower() # Prompt player for a guess and convert to lowercase

            found = False  # Initialize a flag to track if the guessed letter is found in the word

            # Check if the guessed letter is in the chosen word
            # Loop through each position in the chosen word
            for position in range(len(chosen_word)):
                # Get the letter at the current position     
                letter = chosen_word[position] 
                # Check if the guessed letter matches the current letter          
                if letter == guessed_letter:
                    # If a match, update the display with the guessed letter
                    display[position] = guessed_letter
                    # Set a flag indicating a correct guess
                    found = True
                    print("Correct guess!")
                    score += 5  # Increase score for correct guess

            # Display the updated word representation
            print(" ".join(display))

            # Handle incorrect guess and remaining lives
            if not found:  # Check if the guessed letter wasn't found in the word
                lives -= 1
                print("Incorrect guess.")
                print(f"Remaining lives: {lives}") 
                if lives == 0: # Check if lives have reached 0 (indicating game over)
                    game_over = True  # Set game_over flag to True to end the loop
                    print(f"\nYou lose! The word was: {chosen_word}")

            # Check for victory
            if "_" not in display:
                game_over = True
                print("\nYou won! Congratulations!")
                # Capture end time for calculating game duration
                end_time = time.time()  
                 # Calculate elapsed time since game start
                elapsed_time = end_time - start_time
                # Display total game time (formatted to 2 decimal places)
                # print(f"Total time taken: {elapsed_time:.2f} seconds")
                print(f"Final score: {score}")


        print("Thanks for playing!")

if __name__ == "__main__":
    main()










    



