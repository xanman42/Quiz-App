from tkinter import *

THEME_COLOR = "#375362"


class QuizUI:

    def __init__(self):
        self.window = Tk()
        self.window.title('Quiz Time')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.canvas = Canvas(width=300, height=250)
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
        self.true_but = Button(image=true_image, highlightthickness=0)
        self.true_but.grid(column=1, row=3)
        false_image = PhotoImage(file='images/false.png')
        self.false_but = Button(image=false_image, highlightthickness=0)
        self.false_but.grid(column=2, row=3)




        self.window.mainloop()