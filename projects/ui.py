from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")

        # GUI
        self.window.config(width = 340, height = 500,
                           bg = THEME_COLOR, padx = 20, pady = 20)

        # Score label
        self.score_label = Label(text = "Score: 0", bg = THEME_COLOR, fg = "white")
        self.score_label.grid(column = 1, row = 0)

        # Display question text
        self.canvas = Canvas(width = 300, height = 250, bg = "white", highlightthickness = 0)
        self.question_text = self.canvas.create_text(150, 125, width = 280,
                                                     text = "Are you ready?",
                                                     fill = THEME_COLOR,
                                                     font = ("Ariel", 20, "italic"))
        self.canvas.grid(column = 0, columnspan = 2, row = 1, pady = 50)

        # Buttons
        false_img = PhotoImage(file = "images/false.png")
        self.false_button = Button(image = false_img, width = 90, height = 85,
                              bg = THEME_COLOR, command = self.player_says_false)
        self.false_button.grid(column = 0, row = 2)

        true_img = PhotoImage(file = "images/true.png")
        self.true_button = Button(image = true_img, width = 90, height = 85,
                             bg = THEME_COLOR, command = self.player_says_true)
        self.true_button.grid(column = 1, row = 2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text = "You have reached the end of the quiz.")
            self.true_button.config(state = "disabled")
            self.false_button.config(state = "disabled")

    def player_says_false(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def player_says_true(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")

        self.window.after(1000, self.get_next_question)









