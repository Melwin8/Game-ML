import random
import time

class BoggleGame:
    def __init__(self):
        self.words_for_boards = {
            (
                ('C', 'A', 'T', 'S'),
                ('E', 'A', 'T', 'E'),
                ('H', 'E', 'A', 'R'),
                ('F', 'A', 'T', 'S')

            ): {'CAT', 'EAT', 'EATS', 'HAT', 'HEAR', 'HEATS', 'FAT', 'FAST', 'FATE','HEAT'},
            (
                ('S', 'T', 'O', 'P'),
                ('I', 'N', 'E', 'R'),
                ('M', 'A', 'K', 'E'),
                ('T', 'R', 'I', 'P')
            ): {'STOP', 'STONE', 'TRIP', 'MAKE', 'MAKES', 'TRIPS', 'TRAP', 'RIMS', 'RIP', 'RINSE'},
            (
                ('H', 'O', 'M', 'E'),
                ('C', 'A', 'R', 'S'),
                ('L', 'I', 'S', 'T'),
                ('T', 'R', 'A', 'P')
            ): {'HOME', 'CAR', 'CARS', 'LIST', 'LIME', 'SLIM', 'AIR', 'HOLE', 'HOT', 'EAT'},
            (
                ('B', 'E', 'A', 'C'),
                ('H', 'E', 'L', 'P'),
                ('P', 'R', 'I', 'S'),
                ('G', 'I', 'F', 'T')
            ): {'BEACH', 'HELP', 'PRIG', 'GIFT', 'RIP', 'RIG', 'PAT', 'TIP', 'PIE', 'BEAT'}
        }
        self.score = 0

    def generate_board(self):
        return random.choice(list(self.words_for_boards.keys()))

    def display_board(self, board):
        for row in board:
            print(" ".join(row))

    def display_hint(self, hint_words):
        print("\nHint words:", ", ".join(hint_words))

    def play(self):
        print("Welcome to Boggle!")
        while True:
            board = self.generate_board()  # Generate a new board each time the player wants to continue
            print("\nGenerated Boggle Board:")
            self.display_board(board)
            start_time = time.time()
            input("Press Enter to stop the timer and guess the words...")
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("\nTime elapsed: {:.2f} seconds".format(elapsed_time))
            player_words = input("Enter your guessed words separated by spaces (type 'hint' for hint): ").strip().upper().split()
            
            if 'hint' in player_words:  # Check if player wants a hint
                valid_words = self.words_for_boards[board]
                hint_words = random.sample(valid_words, min(3, len(valid_words)))  # Select up to 3 random words as hints
                self.display_hint(hint_words)
                continue  # Skip scoring and continue the game
            
            valid_words = self.words_for_boards[board]
            correct_guesses = [word for word in player_words if word in valid_words]
            incorrect_guesses = [word for word in player_words if word not in valid_words]
            self.score += len(correct_guesses)
            print("\nCorrect guesses:")
            for word in correct_guesses:
                print(word)
            print("\nIncorrect guesses:")
            for word in incorrect_guesses:
                print(word)
            print("\nYour score is:", self.score)

            play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    game = BoggleGame()
    game.play()