from rest_framework import views,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import action
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
    

# class TenseQuizViewSet(viewsets.ViewSet):
#     @action(detail=False, methods=['get'])
#     def level_choices(self, request):
#         serializer = LevelChoiceSerializer()
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = LevelChoiceSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         level = serializer.validated_data['level']

#         questions = None
#         if level == 'beginner':
#             questions = TenseQuiz().beginner_questions
#         elif level == 'medium':
#             questions = TenseQuiz().medium_questions
#         elif level == 'expert':
#             questions = TenseQuiz().expert_questions
        
#         if questions is None:
#             return Response({"status": 0, "error": "Invalid level."}, status=status.HTTP_400_BAD_REQUEST)
        
#         quiz = TenseQuiz()
#         quiz.run_quiz(questions)
#         next_question = quiz.get_next_question()
#         return Response({"status": 1, "message": f"Quiz started! Level: {level.capitalize()}.", "question": next_question['question']})

#     @action(detail=False, methods=['post'])
#     def answer_question(self, request):
#         serializer = AnswerSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user_answer = serializer.validated_data['answer']

#         quiz = TenseQuiz()  # Create a new quiz instance
#         response = quiz.check_answer(user_answer)
#         if response['correct']:
#             return Response({"message": "Correct answer!"})
#         else:
#             return Response({"message": "Incorrect answer. Try again."})

#     @action(detail=False, methods=['get'])
#     def get_score(self, request):
#         quiz = TenseQuiz()  # Create a new quiz instance
#         response = quiz.get_score()
#         return Response({"message": response['message']})


class QuizAPIView(APIView):
    def post(self, request):
        # Validate level choice
        level_serializer = LevelChoiceSerializer(data=request.data)
        if not level_serializer.is_valid():
            return Response(level_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Get the validated level
        level = level_serializer.validated_data['level']
        
        # Check if the user input is "start" to begin the quiz
        start_input = request.data.get('start_quiz', False)
        if not start_input:
            return Response({"message": "Type 'start' to begin the quiz."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Initialize quiz based on the selected level
        quiz = TenseQuiz()
        if level == "beginner":
            questions = quiz.beginner_questions
        elif level == "medium":
            questions = quiz.medium_questions
        elif level == "expert":
            questions = quiz.expert_questions
        else:
            return Response({"error": "Invalid level"}, status=status.HTTP_400_BAD_REQUEST)

        # Welcome message
        if not request.session.get('quiz_started', False):
            request.session['quiz_started'] = True
            return Response({"message": "Welcome to the English Tense Quiz!"}, status=status.HTTP_200_OK)

        # Validate user's answer
        serializer = AnswerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Get the validated answer
        user_answer = serializer.validated_data['answer']

        # Get current question index from session
        current_question = request.session.get('current_question', 0)
        
        # Check if there are more questions
        if current_question < len(questions):
            question = questions[current_question]
            response = {
                "question": f"Question {current_question + 1}: {question['question']}",
                "user_answer": f"Your answer: {user_answer}",
                "score": request.session.get('score', 0),  # Get the current score from session
                "Next question": f"Question {current_question + 1}: {questions[current_question + 1]['question']}",
            }
            if user_answer.lower() == question['answer'].lower():
                response["feedback"] = "Correct!"
                request.session['score'] = response["score"] + 1  # Update score in session
            else:
                response["feedback"] = f"Incorrect. The correct answer is '{question['answer']}'."
            
            request.session['current_question'] = current_question + 1  # Move to the next question
            return Response(response, status=status.HTTP_200_OK)
        else:
            final_score = request.session.get('score', 0)
            final_response = {"message": "Quiz complete! Your final score is:", "score": final_score}
            request.session.pop('current_question', None)  # Clear session variables
            request.session.pop('score', None)
            request.session.pop('quiz_started', None)  # Clear quiz started flag
            return Response(final_response, status=status.HTTP_200_OK)
    
# class BoggleGameView(APIView):
#     def post(self, request):
#         serializer = BoggleInputSerializer(data=request.data)
#         if serializer.is_valid():
#             player_words = serializer.validated_data['player_words']
#             # Initialize or get the BoggleGame instance
#             game = BoggleGame()
#             board = game.generate_board()
#             valid_words = game.words_for_boards[board]
#             correct_guesses = [word for word in player_words if word in valid_words]
#             score = len(correct_guesses)
#             return Response({'score': score, 'correct_guesses': correct_guesses}, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BoggleGameView(APIView):
#     def post(self, request):
#         serializer = BoggleInputSerializer(data=request.data)
#         if serializer.is_valid():
#             player_words = serializer.validated_data['player_words'].split(',')
#             # Initialize or get the BoggleGame instance
#             game = BoggleGame()
#             board = game.generate_board()
#             valid_words = game.words_for_boards[board]
#             correct_guesses = [word for word in player_words if word.upper() in valid_words]
#             score = len(correct_guesses)
#             return Response({
#                 'board': board,
#                 'elapsed_time': 0,  # Placeholder for elapsed time as it's not handled in this view
#                 'player_words': player_words,
#                 'correct_guesses': correct_guesses,
#                 'score': score
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoggleGameView(APIView):
    serializer_class = BoggleInputSerializer
    def get(self, request):
        game = BoggleGame()
        board = game.generate_board()
        game.display_board(board)  # Display the board
        return Response({'board': board}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BoggleInputSerializer(data=request.data)
        if serializer.is_valid():
            player_words = serializer.validated_data['player_words'].split(',')
            # Initialize or get the BoggleGame instance
            game = BoggleGame()
            board = game.generate_board()
            valid_words = game.words_for_boards[board]
            correct_guesses = [word for word in player_words if word.upper() in valid_words]
            score = len(correct_guesses)
            elapsed_time = 0  # Placeholder for elapsed time as it's not handled in this view
            return Response({
                'board': board,
                'elapsed_time': elapsed_time,
                'player_words': player_words,
                'correct_guesses': correct_guesses,
                'score': score
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)