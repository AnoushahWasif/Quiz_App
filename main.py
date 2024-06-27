import requests
from quiz import Quiz
from question import Question
from user import User
import html  # Import HTML parser module

def get_questions(amount=3, category=9, difficulty='easy', type='multiple'):
    # Parameters for the Open Trivia Database API
    url = f'https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type={type}'

    # Fetching data from the API
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'results' in data:
            questions = []
            for result in data['results']:
                question_text = html.unescape(result['question'])  # Decode HTML entities
                correct_answer = html.unescape(result['correct_answer'])  # Decode HTML entities
                incorrect_answers = result['incorrect_answers']
                choices = [html.unescape(answer) for answer in incorrect_answers] + [correct_answer]
                # Shuffle choices to randomize the order
                import random
                random.shuffle(choices)
                # Determine the correct index after shuffling
                answer_index = choices.index(correct_answer)
                question = Question(question_text, choices, answer_index)
                questions.append(question)
            return questions
        else:
            print("No results found.")
    else:
        print("Failed to fetch data from API.")
    return []

def take_quiz(quiz):
    print("Welcome to the Quiz!")
    while quiz.current_question_index < len(quiz.questions):
        quiz.display_question()
        user_answer = input("Enter your choice (1, 2, 3, ...): ").strip().lower()
        if user_answer.isdigit():
            user_answer = int(user_answer) - 1
            quiz.check_answer(user_answer)
        else:
            print("Invalid input. Please enter a number.")

    quiz.show_result()

def main():
    # Fetch questions from Open Trivia Database API
    questions_data = get_questions(amount=3, category=9, difficulty='easy', type='multiple')

    if questions_data:
        quiz = Quiz(questions_data)
        username = input("Enter your name: ")
        user = User(username)
        take_quiz(quiz)
    else:
        print("No quiz questions available. Exiting.")

if __name__ == "__main__":
    main()
