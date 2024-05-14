class TenseQuiz:
    def __init__(self):
        self.beginner_questions = [
            {"question": "What is the past tense of 'eat'?", "answer": "ate"},
            {"question": "What is the present continuous tense of 'go'?", "answer": "going"},
            {"question": "What is the future tense of 'run'?", "answer": "will run"},
            {"question": "What is the present perfect tense of 'drink'?", "answer": "have drunk"},
            {"question": "What is the past continuous tense of 'sleep'?", "answer": "was sleeping"},
            {"question": "What is the past tense of 'read'?", "answer": "read"},
            {"question": "What is the present tense of 'write'?", "answer": "write"},
            {"question": "What is the future tense of 'sing'?", "answer": "will sing"},
            {"question": "What is the present perfect tense of 'do'?", "answer": "have done"},
            {"question": "What is the past continuous tense of 'eat'?", "answer": "was eating"},
        ]
        self.medium_questions = [
            {"question": "What is the past tense of 'speak'?", "answer": "spoke"},
            {"question": "What is the present continuous tense of 'run'?", "answer": "is running"},
            {"question": "What is the future tense of 'write'?", "answer": "will write"},
            {"question": "What is the present perfect tense of 'take'?", "answer": "have taken"},
            {"question": "What is the past continuous tense of 'swim'?", "answer": "was swimming"},
            {"question": "What is the past tense of 'think'?", "answer": "thought"},
            {"question": "What is the present tense of 'drive'?", "answer": "drive"},
            {"question": "What is the future tense of 'dance'?", "answer": "will dance"},
            {"question": "What is the present perfect tense of 'see'?", "answer": "have seen"},
            {"question": "What is the past continuous tense of 'drink'?", "answer": "was drinking"},
        ]
        self.expert_questions = [
            {"question": "What is the past tense of 'begin'?", "answer": "began"},
            {"question": "What is the present continuous tense of 'fly'?", "answer": "is flying"},
            {"question": "What is the future tense of 'give'?", "answer": "will give"},
            {"question": "What is the present perfect tense of 'fall'?", "answer": "have fallen"},
            {"question": "What is the past continuous tense of 'fall'?", "answer": "was falling"},
            {"question": "What is the past tense of 'wear'?", "answer": "wore"},
            {"question": "What is the present tense of 'lead'?", "answer": "lead"},
            {"question": "What is the future tense of 'leave'?", "answer": "will leave"},
            {"question": "What is the present perfect tense of 'buy'?", "answer": "have bought"},
            {"question": "What is the past continuous tense of 'come'?", "answer": "was coming"},
        ]
        self.score = 0

    def run_quiz(self, questions):
        print("Welcome to the English Tense Quiz!")
        for i, question in enumerate(questions, 1):
            print(f"Question {i}: {question['question']}")
            user_answer = input("Your answer: ").strip().lower()
            if user_answer == question['answer']:
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer is '{question['answer']}'.")

        print(f"\nQuiz complete! Your score is {self.score}/{len(questions)}.")


if __name__ == "__main__":
    quiz = TenseQuiz()
    level = input("Choose your level (Beginner, Medium, Expert): ").strip().lower()
    if level == "beginner":
        quiz.run_quiz(quiz.beginner_questions)
    elif level == "medium":
        quiz.run_quiz(quiz.medium_questions)
    elif level == "expert":
        quiz.run_quiz(quiz.expert_questions)
    else:
        print("Invalid level! Please choose from Beginner, Medium, or Expert.")
