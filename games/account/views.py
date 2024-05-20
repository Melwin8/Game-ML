import time
import random
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework.permissions import AllowAny
from .gaming import TenseQuiz 
from .boggle import BoggleGame
# from .gaming import Question

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    serializer_class=CustomUserSerializer
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":1,"message": "User registered successfully",'data':serializer.data},status=status.HTTP_201_CREATED)
        return Response({"status":0,"error": "User registration failed", "errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserloginView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer
    

class QuizAPIView(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quiz = TenseQuiz()

    def post(self, request):
        # Validate level choice
        level_serializer = LevelChoiceSerializer(data=request.data)
        if not level_serializer.is_valid():
            return Response(level_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Get the validated level
        level = level_serializer.validated_data['level']
        
        # Initialize quiz based on the selected level
        if level == "beginner":
            questions = self.quiz.beginner_questions
        elif level == "medium":
            questions = self.quiz.medium_questions
        elif level == "expert":
            questions = self.quiz.expert_questions
        else:
            return Response({"error": "Invalid level"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the quiz has started
        if not request.session.get('quiz_started', False):
            request.session['quiz_started'] = True
            request.session['questions'] = questions  # Store questions in session
            request.session['current_question'] = 0  # Initialize current question index
            # Prepare the response for the first question
            response = {
                "message": "Welcome to the English Tense Quiz! Type your answers below.",
                "question": f"Question 1: {questions[0]['question']}",
            }
            return Response(response, status=status.HTTP_200_OK)

        # Get current question index from session
        current_question = request.session.get('current_question', 0)
        questions = request.session.get('questions')

        # Check if there are more questions
        if current_question < len(questions):
            question = questions[current_question]

            # Validate user's answer
            serializer = AnswerSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            # Get the validated answer
            user_answer = serializer.validated_data['answer']

            response = {
                "question": f"Question {current_question + 1}: {question['question']}",
                "user_answer": f"Your answer: {user_answer}",
                "score": request.session.get('score', 0),  # Get the current score from session
            }

            if user_answer.lower() == question['answer'].lower():
                response["feedback"] = "Correct!"
                # Increase score only if the answer is correct
                request.session['score'] = response["score"] + 1  # Update score in session

            else:
                response["feedback"] = f"Incorrect. The correct answer is '{question['answer']}'."

            # Move to the next question
            request.session['current_question'] = current_question + 1

            # Check if there are more questions after this
            if current_question + 1 < len(questions):
                response["Next question"] = f"Question {current_question + 2}: {questions[current_question + 1]['question']}"

            return Response(response, status=status.HTTP_200_OK)
        else:
            final_score = request.session.get('score', 0)  # Get the final score
            request.session.pop('current_question', None)  # Clear session variables
            request.session.pop('score', None)
            request.session.pop('quiz_started', None)  # Clear quiz started flag
            request.session.pop('questions', None)  # Clear questions from session
            final_response = {"message": "Quiz complete! Your final score is:", "score": final_score}
            return Response(final_response, status=status.HTTP_200_OK)
    

class BoggleGameAPIView(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = BoggleGame()
        self.board = None  # Initially set board to None

    def get(self, request, format=None):
        if self.board is None:
            # Game hasn't started yet, generate the initial board
            self.board = self.game.generate_board()
            print("board",self.board)

        # Input messages
        messages = [
            "Welcome to Boggle!",
            "Try to find as many words as you can in the given board.",
            "Type your words separated by spaces and submit to check your score.",
            "You can also type 'hint' for a hint to get started.",
        ]

        # Return the current board and input messages on GET request
        response_data = {
            'board': self.board,
            'messages': messages,
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def display_board(self, board):
        board_str = "\n".join([" ".join(row) for row in board])
        return board_str

    def display_hint(self, hint_words):
        hint_str = "\nHint words: " + ", ".join(hint_words)
        return hint_str

    def post(self, request, format=None):
        serializer = BoggleGameSerializer(data=request.data)
        # guessed_words=[]
        if serializer.is_valid():
            self.board = self.game.generate_board()
            # guessed_word = [guessed_words.append(word) for word in serializer.validated_data['guessed_words']]
            guessed_words = []
            guessed_word = serializer.validated_data.get('guessed_words')
            
            if guessed_word:
                if isinstance(guessed_word, str):
                    # Split the input string by spaces to get individual words
                    guessed_words = guessed_word.split()
                    print("split",guessed_words)
                elif isinstance(guessed_word, list):
                    guessed_words.extend([ word.upper() for phrase in guessed_word for word in phrase.split()])
                    print("list",guessed_words)
            

            print("guessed",guessed_words)
            self.game.score = 0  # Reset score for each new game

            valid_words = self.game.words_for_boards[self.board]
            print(valid_words)
            correct_guesses = [word for word in guessed_words if word in valid_words]
            incorrect_guesses = [word for word in guessed_words if word not in valid_words]
            print("correct guesss",correct_guesses)
            self.game.score += len(correct_guesses)
        
            # Prepare response data
            response_data = {
                'board': self.display_board(self.board),  # Include the board in the response
                'score': self.game.score,
                'valid_words': list(valid_words),
                'correct_guesses': correct_guesses,
                'Incorrect Guesses':incorrect_guesses
            }

            # Check if 'hint' is in guessed words
            if 'hint' in guessed_words:
                hint_words = random.sample(valid_words, min(3, len(valid_words)))
                response_data['hint'] = self.display_hint(hint_words)

            play_again = request.data.get('play_again', '').lower()
            if play_again == 'yes':
                # Reset the board for a new game
                self.board = self.game.generate_board()

            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)