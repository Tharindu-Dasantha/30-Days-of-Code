import customtkinter as ctk

# Set appearance mode and color theme
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

# Create the main application window
root = ctk.CTk()
root.title("Calculator")
root.geometry('400x500')
root.resizable(False, False)

equation = ""

def show(value):
    global equation
    equation += value
    label_results.config(text=equation)

def clear():
    global equation
    equation = ""
    label_results.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = str(eval(equation))
            equation = result
            label_results.config(text=equation)
        except Exception as e:
            label_results.config(text="Error")

# Create label for displaying results
label_results = ctk.CTkLabel(root, width=160, height=2, text="", font=("Helvetica", 32), bg_color="#2e2e2e", text_color="#ffffff")
label_results.grid(row=0, column=0, columnspan=4, pady=20)

# Button styling
button_style = {
    "font": ("Helvetica", 24, "bold"),
    "fg_color": "#4c4c4c",
    "hover_color": "#6c6c6c",
    "text_color": "#ffffff",
    "corner_radius": 500,
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
        btn = ctk.CTkButton(root, text=text, width=5, height=3, command=calculate, **button_style)
    else:
        btn = ctk.CTkButton(root, text=text, width=5, height=2, command=lambda value=text: show(value), **button_style)
    btn.grid(row=row + 1, column=column, padx=10, pady=10)

# Clear button
clear_button = ctk.CTkButton(root, text="C", width=5, height=2, command=clear, **button_style)
clear_button.grid(row=1, column=0, padx=10, pady=10)

# Start the application
root.mainloop()
