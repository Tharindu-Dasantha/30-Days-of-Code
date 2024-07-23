import customtkinter
from customtkinter import *


root=Tk()
root.title("Calculator")
root.geometry('570x700')
root.resizable(False, False)


equation = ""

def show(value):
    global equation
    equation+=value
    label_results.config(text=equation)

def clear():
    global equation
    equation=""
    label_results.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = str(eval(equation))
            equation = result
            label_results.config(text=equation)
        except:
            label_results.config(text="")

label_results = Label(root, width=16, height=2, text="", font=("Helverica", 32), bg="#2e2e2e", fg="#ffffff")
label_results.grid(row=0, column=0, columnspan=4, pady=20)

# Button Styling
button_style = {
    "font": ("Helverica", 24, "bold"),
    "bd": 0,
    "fg": "#ffffff",
    "bg": "#4c4c4c",
    "activebackground": "#6c6c6c",
    "activeforeground": "#ffffff",
}

# Create buttons using a grid
buttons = [
    ('C', 0, 0), ('/', 0, 1), ('%', 0, 2), ('*', 0, 3),
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('-', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('+', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('=', 3, 3),
    ('0', 4, 0), ('.', 4, 1)
]

for (text, row, column) in buttons:
    if text == "=":
        btn = Button(root, text=text, width=5, height=3, command=calculate, **button_style)
    else:
        btn = Button(root, text=text, width=5, height=2, command=lambda value=text:show(value), **button_style)
    btn.grid(row=row + 1, column=column, padx=10, pady=10)

# Clear button
clear_button = Button(root, text="C", width=5, height=2, command=clear, **button_style)
clear_button.grid(row=1, column=0, padx=10, pady=10)


root.mainloop()