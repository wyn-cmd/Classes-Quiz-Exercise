import ast


class question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def check_answer(self, user_answer):
        return user_answer == self.answer
    
class quiz:
    def __init__(self, questions):
        self.question = questions
        self.__current_index = 0
        self.score = 0

    def display_question(self):
        current_question = self.question[self.__current_index]
        print(f'Question {self.__current_index + 1}: {current_question[0]}')
        for i, choice in enumerate(current_question[1], start=1):
            print(f'{i}, {choice}')
        user_answer = input('Enter your choice (1 to 4): ')
        self.check_answer(user_answer)

    def check_answer(self, user_answer):
        current_question = self.question[self.__current_index]
        if current_question[2] == int(user_answer):
            print('\nCorrect!')
            self.score += 1
        else:
            print('\nIncorrect.')
    
        self.__current_index += 1

    def display_score(self):
        print('Your score is:')
        print(f'questions: {self.__current_index}')
        print(f'score: {self.score}')
        







def load_questions_from_file(file_path):
  """Loads questions from a text file into a list of tuples.

  Args:
    file_path: The path to the text file containing the questions.

  Returns:
    A list of tuples, where each tuple contains the question, answer choices, and correct answer index.
  """

  questions = []
  with open(file_path, 'r') as file:
    for line in file:
      question, choices, correct_answer = ast.literal_eval(line)
      questions.append((question, choices, correct_answer))
  return questions

# Example usage:
file_path = "questions.txt"  # Replace with the actual file path
questions = load_questions_from_file(file_path)

# Access individual questions:
question1 = questions[0]
question2 = questions[1]
question3 = questions[2]



# Create quiz
quiz = quiz([question1, question2, question3])
    
# Conduct the quiz
print("Welcome to the Quiz!\n")
for _ in range(len(quiz.question)):
    quiz.display_question()
    
# Display final score
quiz.display_score()
