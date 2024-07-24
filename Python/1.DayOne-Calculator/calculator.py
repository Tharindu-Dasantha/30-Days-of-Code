import customtkinter as ctk

# Set appearance mode and color theme
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("dark-blue")  

# Create the main application window
root = ctk.CTk()
root.title("Calculator")
root.geometry('350x500')
root.resizable(False, False)

equation = ""

# Custom colors and fonts
background_color = "#282828"
button_color = "#383838"
text_color = "#ffffff"
font = ("Helvetica", 22, "bold")

def show(value):
    global equation
    equation += value
    label_results.configure(text=equation)

def clear():
    global equation
    equation = ""
    label_results.configure(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = str(eval(equation))
            equation = result
            label_results.configure(text=equation)
        except Exception as e:
            label_results.configure(text="Error")

# Create label for displaying results
label_results = ctk.CTkLabel(root, text="", font=font, bg_color=background_color, text_color=text_color, height=70, width=300)
label_results.grid(row=0, column=0, columnspan=4, pady=20, padx=15, sticky="nsew")

# Configure grid layout
# root.columnconfigure(0, weight=1) 

# Button styling
button_style = {
    "font": font,
    "fg_color": button_color,
    "hover_color": "#484848",
    "text_color": text_color,
    "corner_radius": 10,
}

# Create buttons using a grid
buttons = [
    ('/', 0, 1), ('%', 0, 2), ('*', 0, 3),
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('-', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('+', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('=', 3, 3),
    ('0', 4, 0), ('.', 4, 1)
]

for (text, row, column) in buttons:
    if text == "=":
        btn = ctk.CTkButton(root, text=text, width=65, height=65, command=calculate, **button_style)
    else:
        btn = ctk.CTkButton(root, text=text, width=65, height=65, command=lambda value=text: show(value), **button_style)
    btn.grid(row=row + 1, column=column, padx=5, pady=5)

# Clear button
clear_button = ctk.CTkButton(root, text="C", width=65, height=65, command=clear, **button_style)
clear_button.grid(row=1, column=0, padx=3, pady=3)

# Set background color
root.configure(bg=background_color)

# Start the application
root.mainloop()
