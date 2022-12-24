class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        elif user_answer.lower() == correct_answer[0].lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was {correct_answer}.")

        print(f"Your current score is {self.score}/{self.question_number}")

    def still_has_questions(self):
        if self.question_number >= len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        correct_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question} "
                       f"(True/False)?: ")
        self.check_answer(answer, correct_answer)

