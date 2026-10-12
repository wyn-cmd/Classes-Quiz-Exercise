# Simple command line quiz application using basic object oriented python.

import ast


# Represents a single quiz question with text, choices, and the correct answer index.
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def check_answer(self, user_answer):
        return user_answer == self.answer


# Manages the quiz state, flow, questions, and final score.
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.__current_index = 0
        self.score = 0

    def display_question(self):
        current_question = self.questions[self.__current_index]
        print(f"Question {self.__current_index + 1}: {current_question.text}")
        for i, choice in enumerate(current_question.choices, start=1):
            print(f"{i}. {choice}")
        
        while True:
            try:
                user_answer = int(input("Enter your choice (1 to 4): "))
                if 1 <= user_answer <= len(current_question.choices):
                    break
                print("Invalid choice range. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

        self.check_answer(user_answer)

    def check_answer(self, user_answer):
        current_question = self.questions[self.__current_index]
        if current_question.check_answer(user_answer):
            print("\nCorrect!\n")
            self.score += 1
        else:
            print("\nIncorrect.\n")
    
        self.__current_index += 1

    def display_score(self):
        print("Your score is:")
        print(f"Questions answered: {self.__current_index}")
        print(f"Score: {self.score}")


# Reads questions from a text file where each line is parsed safely via literal eval.
def load_questions_from_file(file_path):
    questions = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                text, choices, answer = ast.literal_eval(line)
                questions.append(Question(text, choices, answer))
    return questions


if __name__ == "__main__":
    file_path = "questions.txt"
    
    try:
        raw_questions = load_questions_from_file(file_path)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        raw_questions = []

    if raw_questions:
        quiz = Quiz(raw_questions)
        print("Welcome to the Quiz!\n")
        
        for _ in range(len(quiz.questions)):
            quiz.display_question()
            
        quiz.display_score()