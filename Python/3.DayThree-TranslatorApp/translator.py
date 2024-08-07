import tkinter as tk
from tkinter import font as tkFont

def gui():
    root = tk.Tk()
    root.title("Translator")
    root.geometry("800x600")
    root.resizable(False, False)
    root.configure(background="#afdde5")

    # Creating a text widget
    bold_font = tkFont.Font(family="Arial", size=35, weight="bold")
    TitleLable = tk.Label(text="Translator Application", font=bold_font, fg="#003135", bg="#afdde5")
    TitleLable.pack(pady=(20,0))

    # Creaating two text boxes
    editable_text = tk.Entry(root, width=50, height=20)
    editable_text.pack(side="left")

    non_editable_text = tk.Entry(root)
    non_editable_text.configure(state="disabled")
    non_editable_text.pack(side="right")


    root.mainloop()


if __name__ == "__main__":
    gui()