from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz Time')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Question will display here',
            font=('Ariel', 20, 'italic')
        )
        self.canvas.grid(column=1, row=2, columnspan=2, pady=40)

        self.score = Label(text='score : 0', bg=THEME_COLOR, fg='white')
        self.score.grid(column=2, row=1)

        true_image = PhotoImage(file='images/true.png')
        self.true_but = Button(image=true_image, highlightthickness=0, command=self.true_clicked)
        self.true_but.grid(column=1, row=3)
        false_image = PhotoImage(file='images/false.png')
        self.false_but = Button(image=false_image, highlightthickness=0, command=self.false_clicked)
        self.false_but.grid(column=2, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score.config(text=f"score: {self.quiz.score}")
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end")
            self.true_but.config(state='disabled')
            self.false_but.config(state='disabled')

    def true_clicked(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)

    def false_clicked(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, func=self.get_next_question)
