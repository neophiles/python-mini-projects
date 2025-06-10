# Simple Tkinter Calculator
# Created by Marc Neil Tagle, June 2025
# For educational purposes

import tkinter as tk
from tkinter import font

class Calculator(tk.Tk):

    def __init__(self):
        super().__init__()

        # window settings
        self.title('Calculator')
        self.geometry('400x500+0+0')
        self.resizable(0, 0)

        # define window grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.create_containers()
        self.create_display_widgets()
        self.create_button_widgets()

        self.is_answered = False

    def create_containers(self):

        # create main containers/frames
        self.display_frame = tk.Frame(bg='lightgray', width=400, height=100, padx=5, pady=5)
        self.buttons_frame = tk.Frame(bg='black', width=400, height=400, padx=5, pady=5)

        # position containers
        self.display_frame.grid(row=0, column=0, sticky='nsew')
        self.buttons_frame.grid(row=1, column=0, sticky='nsew')

        # keep frame sizes / disable automatic resizing
        self.display_frame.grid_propagate(False)
        self.buttons_frame.grid_propagate(False)

        # define button frame grid
        for r in range(5):
            self.buttons_frame.rowconfigure(r, weight=1, uniform='row')
            for c in range(5):
                 self.buttons_frame.columnconfigure(c, weight=1, uniform='col')

    def on_configure(self, event):
        # update scrollable area of canvas to encompass entire scrollable_frame
        self.display_canvas.configure(scrollregion=self.display_canvas.bbox("all"))

    def create_display_widgets(self):

        # define font for display text
        text_font = font.Font(family="Helvetica", size=20)

        # create canvas where display label will be drawn
        self.display_canvas = tk.Canvas(self.display_frame, width=400, height=75, bg='lightgray')
        self.display_canvas.pack(side='top', expand=True)

        # create horizontal scrollbar for canvas
        self.display_scroll = tk.Scrollbar(self.display_frame, orient="horizontal", command=self.display_canvas.xview)
        self.display_scroll.pack(side="bottom", fill="x")

        # link scrollbar to canvas
        self.display_canvas.configure(xscrollcommand=self.display_scroll.set)

        # create frame inside canvas to hold display label
        self.scrollable_frame = tk.Frame(self.display_canvas)
        self.canvas_window = self.display_canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')

        # create label that will display calculator text
        self.display_text = ''
        self.display_label = tk.Label(self.scrollable_frame, text=self.display_text, font=text_font, bg='lightgray')
        self.display_label.pack(side="left", anchor='w')

        # bind resize/configure event of scrollable frame to update scroll region when size changes
        self.scrollable_frame.bind("<Configure>", self.on_configure)
        
    def create_button_widgets(self):

        # define font for button text
        button_font = font.Font(family="Helvetica", size=16)

        # define button layout where each sublist is a row
        button_texts = [
            ['7', '8', '9', 'DEL', 'AC'],
            ['4', '5', '6', '+', '-'],
            ['1', '2', '3', '*', '/'], 
            ['0', '.', '^', '(', ')'],
            ['ANS', '=']
        ]
    
        # create buttons
        for r, row in enumerate(button_texts):
            for c, text in enumerate(row):

                # positions the last row of buttons to the right of the grid
                if r == 4:
                    c += 3

                # assign button commands based on button type
                if text.isdigit():
                    cmd = lambda t=text: self.number_pressed(t)
                elif text in ['+', '-', '*', '/', '^', '.', '(', ')']:
                    cmd = lambda t=text: self.operator_pressed(t)
                else:
                    cmd = lambda t=text: self.function_pressed(t)

                btn = tk.Button(self.buttons_frame, text=text, font=button_font, 
                                borderwidth=3, cursor='hand2', command=cmd)
                btn.grid(row=r, column=c, sticky='nsew')
                    
    def clear_display(self):
        self.display_text = ''
        self.change_display()
        self.is_answered = False
        print(f"Answered State: {self.is_answered}")

    def change_display(self):
        self.display_label.config(text=self.display_text)

    def number_pressed(self, str_num):
        if self.is_answered: self.clear_display()
        self.display_text += str_num
        self.change_display()

    def operator_pressed(self, str_op):
        if self.is_answered: self.clear_display()
        self.display_text += str_op
        self.change_display()
    
    def function_pressed(self, str_func):

        if str_func == 'DEL' and not self.is_answered:
            self.display_text = self.display_text[:-1]
            self.change_display()

        if str_func == 'AC':
            self.clear_display()

        if str_func == 'ANS':
            if self.is_answered: self.clear_display()
            answer = self.retrieve_answer()
            self.display_text += answer
            self.change_display()

        if str_func == '=':
            try:
                result = str(eval(self.display_text.replace('^', '**')))
                self.display_text = result
                self.save_answer(result)
            except:
                self.display_text = 'Error'
            self.change_display()
            self.is_answered = True
            print(f"Answered State: {self.is_answered}")

    def save_answer(self, answer):
        # stores recent previous answer to answer.txt
        with open('answer.txt', 'w') as file:
            file.write(answer)

    def retrieve_answer(self):
        # gets recent previous answer from answer.txt
        with open('answer.txt', 'r') as file:
            answer = file.read()
        return answer

app = Calculator()
app.mainloop()