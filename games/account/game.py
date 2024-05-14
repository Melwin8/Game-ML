import streamlit as st
import random


questions = [
    {
        'question': 'Which sentence is grammatically correct?',
        'options': ['a. She don\'t like pizza.', 'b. She doesn\'t like pizza.', 'c. She don\'t likes pizza.', 'd. She isn\'t liking pizza.'],
        'answer': 1,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': 'Which word is a pronoun?',
        'options': ['a. Run', 'b. Beautiful', 'c. They', 'd. Quickly'],
        'answer': 3,  # Index of the correct option (c)
        'mark': 1
    },
    {
        'question': "What is the correct form of the plural for 'child'?",
        'options': ['a. Childs', "b. Childs'", 'c. Children', 'd. Childers'],
        'answer': 3,  # Index of the correct option (c)
        'mark': 1
    },
    {
        'question': "Identify the conjunction in the following sentence: 'I wanted to go to the party, but I had to finish my homework.'",
        'options': ['a. wanted', 'b. and', 'c. but', 'd. had'],
        'answer': 2,  # Index of the correct option (c)
        'mark': 1
    },
    {
        'question': "Which of the following is a preposition?",
        'options': ['a. Quickly', 'b. Under', 'c. Singing', 'd. Happy'],
        'answer': 1,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': "What is the comparative form of the adjective 'good'?",
        'options': ['a. Gooder', 'b. Better', 'c. Best', 'd. Goodest'],
        'answer': 2,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': "Which sentence is in the past tense?",
        'options': ['a. I am running.', 'b. I will run.', 'c. I run.', 'd. I ran.'],
        'answer': 4,  # Index of the correct option (d)
        'mark': 1
    },
    {
        'question': "Choose the correct possessive form: 'The car belongs to Sarah and John.'",
        'options': ["a. Sarah's and John car", "b. Sarah's and John's car", "c. Sarah and John car", "d. Sarah and John's car"],
        'answer': 2,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': "What is the antonym of 'vivid'?",
        'options': ['a. Dull', 'b. Bright', 'c. Colorful', 'd. Vivacious'],
        'answer': 1,  # Index of the correct option (a)
        'mark': 1
    },
    {
        'question': "Identify the adverb in the following sentence: 'She sang beautifully.'",
        'options': ['a. She', 'b. Beautifully', 'c. Sang', 'd. Song'],
        'answer': 2,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': "What is a synonym for 'happy'?",
        'options': ['a. Sad', 'b. Joyful', 'c. Angry', 'd. Tired'],
        'answer': 2,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': "Choose the synonym for 'abundant.'",
        'options': ['a. Scarce', 'b. Plentiful', 'c. Limited', 'd. Sparse'],
        'answer': 2,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': "Which word is a synonym for 'brave'?",
        'options': ['a. Fearful', 'b. Courageous', 'c. Timid', 'd. Shy'],
        'answer': 2,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': "Identify the synonym for 'knowledge.'",
        'options': ['a. Wisdom', 'b. Ignorance', 'c. Confusion', 'd. Stupidity'],
        'answer': 1,  # Index of the correct option (a)
        'mark': 1
    },
    {
        'question': "What is a synonym for 'celebrate'?",
        'options': ['a. Mourn', 'b. Commemorate', 'c. Lament', 'd. Bemoan'],
        'answer': 2,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': "Choose the correctly phrased sentence: 'Between you and me, the decision was made.'",
        'options': ["a. Between you and I, the decision was made.", "b. Between you and me, the decision was made.", "c. Between I and you, the decision was made.", "d. Between me and you, the decision was made."],
        'answer': 2,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': "Select the properly phrased sentence: 'I have never been to that city before.'",
        'options': ["a. I haven't never been to that city before.", "b. I haven't ever been to that city before.", "c. I never haven't been to that city before.", "d. I have never been to that city before."],
        'answer': 4,  # Index of the correct option (d)
        'mark': 1
    },
    {
        'question': "Identify the correctly phrased sentence: 'The dog ran quickly through the yard.'",
        'options': ["a. The dog quickly ran through the yard.", "b. Quickly the dog ran through the yard.", "c. The quickly dog ran through the yard.", "d. The dog ran quickly through the yard."],
        'answer': 4,  # Index of the correct option (d)
        'mark': 1
    },
    {
        'question': "Choose the properly phrased sentence: 'She sings well.'",
        'options': ["a. She sings good.", "b. She sings well.", "c. She sings goodly.", "d. She sings gooder."],
        'answer': 2,  # Index of the correct option (b)
        'mark': 1
    },
    {
            'question': "Identify the correctly phrased sentence: 'The meeting was attended by both Peter and me.'",
        'options': ["a. The meeting was attended by both Peter and I.", "b. The meeting was attended by both Peter and me.", "c. The meeting was attended by both me and Peter.", "d. The meeting was attended by both I and Peter."],
        'answer': 2,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': "Convert the sentence 'The cake was baked by Mary' to the active voice.",
        'options': ["a. Mary was baking the cake.", "b. Mary baked the cake.", "c. The cake baked Mary.", "d. Mary has been baking the cake."],
        'answer': 2,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': "Rewrite the sentence 'A story was told by the teacher' in the active voice.",
        'options': ["a. The teacher telling a story.", "b. The teacher told a story.", "c. A story was telling the teacher.", "d. The teacher was telling a story."],
        'answer': 2,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': "Change the sentence 'The letter has been written by him' to the active voice.",
        'options': ["a. He has written the letter.", "b. He wrote the letter.", "c. The letter wrote him.", "d. Written by him is the letter."],
        'answer': 1,  # Index of the correct option (a)
        'mark': 1
    },
    {
        'question': "Transform the sentence 'The prize will be awarded by the principal' into the active voice.",
        'options': ["a. The principal awarded the prize.", "b. The prize being awarded by the principal.", "c. The principal was awarding the prize.", "d. The prize will award the principal."],
        'answer': 1,  # Index of the correct option (a)
        'mark': 1
    },
    {
        'question': "Convert the sentence 'The movie was watched by millions of people' to the active voice.",
        'options': ["a. Millions of people watched the movie.", "b. The movie was watching millions of people.", "c. The movie watched millions of people.", "d. Watching by millions of people was the movie."],
        'answer': 1,  # Index of the correct option (a)
        'mark': 1
    },
    {
        'question': "Change the sentence 'She eats lunch at 12:00 every day' to the past tense.",
        'options': ["a. She ate lunch at 12:00 every day.", "b. She eats lunch at 12:00 every day.", "c. She eating lunch at 12:00 every day.", "d. She will eat lunch at 12:00 every day."],
        'answer': 1,  # Index of the correct option (a)
        'mark': 1
    },
    {
        'question': "Rewrite the sentence 'They will visit the museum next week' in the present continuous tense.",
        'options': ["a. They visited the museum next week.", "b. They will be visiting the museum next week.", "c. They visit the museum next week.", "d. They are visiting the museum next week."],
        'answer': 2,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': "Convert the sentence 'I am studying for my exams' to the future tense.",
        'options': ["a. I studied for my exams.", "b. I will study for my exams.", "c. I study for my exams.", "d. I will be studying for my exams."],
        'answer': 2,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': "Transform the sentence 'He has finished his homework' into the present perfect continuous tense.",
        'options': ["a. He finishes his homework.", "b. He has been finishing his homework.", "c. He finished his homework.", "d. He will finish his homework."],
        'answer': 2,  # Index of the correct option (b)
        'mark': 1
    },
    {
        'question': "Change the sentence 'The sun rises in the east' to the future tense.",
        'options': ["a. The sun will rise in the east.", "b. The sun rises in the east.", "c. The sun is rising in the east.", "d. The sun will be rising in the east."],
        'answer': 1,  # Index of the correct option (a)
        'mark': 1
    },

    # Add more questions...
]


def section():
    st.session_state.finish_button_clicked = False
    st.session_state.clicked_buttons = []
    st.session_state.total_marks = 0
    st.session_state.total_attempts = 0
    st.session_state.random_questions = None


def main():
    random_questions = st.session_state.get('random_questions')
    if not random_questions:
        random_questions = random.sample(questions, 5)
        st.session_state.random_questions = random_questions
    st.title("Quiz Game")
    total_marks = getattr(st.session_state, 'total_marks', 0)
    total_questions = len(random_questions)  # Use the randomly selected questions
    max_marks = sum(question_data['mark'] for question_data in random_questions)

    clicked_buttons = st.session_state.get('clicked_buttons', [False] * total_questions)

    finish_button_clicked = st.session_state.get('finish_button_clicked', False)

    if not finish_button_clicked:
        for i, question_data in enumerate(random_questions):
            question = question_data['question']
            options = question_data['options']
            marks = question_data['mark']

            st.write(f"Question {i+1}: {question}")
            if 'code' in question_data:
                st.code(question_data['code'], language='python')

            user_answer = st.radio(f"Select an answer for Question {i+1}:", options)

            button_state_key = f"button_{i}_state"
            if i >= len(clicked_buttons):
                clicked_buttons.append(False)  # Ensure clicked_buttons has the correct length

            check_answer_button_state = clicked_buttons[i]
            check_answer_button = st.button(f"Check Answer for Question {i+1}", key=button_state_key,
                                            disabled=check_answer_button_state)

            if check_answer_button:
                clicked_buttons[i] = True

                correct_answer_index = question_data['answer']
                correct_answer = options[correct_answer_index - 1]

                if user_answer == correct_answer:
                    st.success("Correct!")
                    total_marks += marks
                    st.session_state.total_marks = total_marks

                else:
                    st.error(f"Wrong. The correct answer is: {correct_answer}")

        st.session_state.clicked_buttons = clicked_buttons

        percentage = (total_marks / max_marks) * 100 if total_questions > 0 else 0

        st.write(f"Total Marks Obtained: {total_marks}")
        st.write(f"Percentage: {percentage}%")

        # Add "Finish" button
        finish_button_clicked = st.button("Finish")
        if finish_button_clicked:
            st.session_state.finish_button_clicked = True

    else:
        # Display only the total score for basic level
        st.write(f"Your Score is {total_marks}")

        # Add "Ready to take test again" button
        ready_button_clicked = st.button("Ready to take test again")
        if ready_button_clicked:
            section()
            st.experimental_rerun()  # Restart the test

            

if __name__ == "__main__":
    main()


