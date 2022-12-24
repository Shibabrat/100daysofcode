from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for i in range(len(question_data)):
    question_bank.append(
        Question(question_data[i]["text"], question_data[i]["answer"])
    )

# print(question_bank[0].text)
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()


print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{len(question_bank)}")

# TODO: 1. Explore Open trivia database to collate questions for a Harry Potter trivia game
