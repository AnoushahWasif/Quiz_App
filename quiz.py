from question import Question

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0

    def get_question(self):
        return self.questions[self.current_question_index]

    def display_question(self):
        question = self.get_question()
        print(f"Question {self.current_question_index + 1}: {question.text}")
        for i, choice in enumerate(question.choices):
            print(f"{i + 1}. {choice}")

    def check_answer(self, user_answer):
        question = self.get_question()
        if question.check_answer(user_answer):
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect.")
        self.current_question_index += 1

    def show_result(self):
        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")
