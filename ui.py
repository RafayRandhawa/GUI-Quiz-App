from tkinter import *
import tkinter.font
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
RIGHT_COLOR = "#7ABA78"
WRONG_COLOR = "#E72929"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        #Labels
        font_object = tkinter.font.Font(size=20)
        self.score = Label(text="score: 0", background=THEME_COLOR, padx=20, pady=20, foreground="white",
                           font=font_object)
        self.score.grid(row=0, column=0, columnspan=2)
        #Canvas
        self.canvas = Canvas(self.window, width=300, height=250, borderwidth=0, highlightthickness=0)
        self.canvas.config(background="white")
        self.question = self.canvas.create_text(150, 125, text="", width=280, font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        #Buttons
        right_image = PhotoImage(file="D:/Python/Quiz Project/images/true.png")
        wrong_image = PhotoImage(file="D:/Python/Quiz Project/images/false.png")
        self.rightButton = Button(image=right_image, highlightthickness=0, borderwidth=0,
                                  command=self.right_button_func)
        self.rightButton.grid(row=2, column=1)
        self.wrongButton = Button(image=wrong_image, highlightthickness=0, borderwidth=0,
                                  command=self.wrong_button_func)
        self.wrongButton.grid(row=2, column=0)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question, text=self.quiz.next_question())
            self.rightButton.config(state="normal")
            self.wrongButton.config(state="normal")
        else:
            self.canvas.itemconfig(self.question,
                                   text=f"You have reached the end of the QUIZ!!!\n\nYou answered {self.quiz.score}/10 correctly")

    def right_button_func(self):
        if self.quiz.check_answer("True"):
            self.score.config(text=f"score: {self.quiz.score}")
            self.canvas.config(background=RIGHT_COLOR)
        else:
            self.canvas.config(background=WRONG_COLOR)
        self.rightButton.config(state="disabled")
        self.wrongButton.config(state="disabled")
        self.window.after(1000, self.next_question)

    def wrong_button_func(self):
        if self.quiz.check_answer("False"):
            self.score.config(text=f"score: {self.quiz.score}")
            self.canvas.config(background=RIGHT_COLOR)
        else:
            self.canvas.config(background=WRONG_COLOR)
        self.rightButton.config(state="disabled")
        self.wrongButton.config(state="disabled")
        self.window.after(1000, self.next_question)
