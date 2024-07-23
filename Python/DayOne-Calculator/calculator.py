import tkinter
from tkinter import *


root=Tk()
root.title("Calculator")
root.geometry('400x600')
root.resizable(False, False)
root.configure(bg="#2E2E2E")


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

label_results = Label(root, width=16, height=2, text="", font=("Helverica", 32), bg="#2e2e2e", fg="ffffff")
label_results.pack(pady=20)

# Button Styling
button_style = {
    "font": ("Helverica", 24, "bold"),
    "bd": 0,
    "fg": "#ffffff",
    "bg": "#4c4c4c",
    "activebackground": "6c6c6c",
    "activeforeground": "ffffff"
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
        btn = Tk.Button(root, text=text, width=5, height=3, command=calculate, **button_style)
    else:
        btn = Tk.Button(root, text=text, width=5, height=2, command=lambda value=text:show(value), **button_style)
    btn.grid(row=row +1, column=column, padx=10, pady=10)

# Clear button
clear_button = Tk.Button(root, text="C", width=5, height=2, command=clear, **button_style)
clear_button.grid(row=1, column=0, padx=10, pady=10)


# Button(root, text="C", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: clear()).place(x=10, y=100)
# Button(root, text="/", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/")).place(x=150, y=100)
# Button(root, text="%", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("%")).place(x=290, y=100)
# Button(root, text="*", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")).place(x=430, y=100)

# Button(root, text="7", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7")).place(x=10, y=200)
# Button(root, text="8", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).place(x=150, y=200)
# Button(root, text="9", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).place(x=290, y=200)
# Button(root, text="-", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-")).place(x=430, y=200)

# Button(root, text="4", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4")).place(x=10, y=300)
# Button(root, text="5", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).place(x=150, y=300)
# Button(root, text="6", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).place(x=290, y=300)
# Button(root, text="+", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+")).place(x=430, y=300)

# Button(root, text="1", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1")).place(x=10, y=400)
# Button(root, text="2", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).place(x=150, y=400)
# Button(root, text="3", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=290, y=400)

# Button(root, text="0", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=10, y=500)


# Button(root, text=".", width=5, height=1, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=290, y=500)
# Button(root, text="=", width=5, height=3, font=("Helvetica", 30, "bold"), bd=1, fg="#fff", bg="#fe9037", command=lambda: calculate()).place(x=430, y=500)


root.mainloop()