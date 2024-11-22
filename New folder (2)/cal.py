import tkinter as tk
from math import *

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set(screen.get()[:-1])  # Remove the last character
    elif text == "AC":
        screen.set("")  # Clear everything
    else:
        screen.set(screen.get() + text)

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")

screen = tk.StringVar()
screen.set("")

# Entry widget for display
entry = tk.Entry(root, textvar=screen, font="Arial 24", bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=10, pady=10)

# Button layout
button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["AC", "sin", "cos", "tan"],
    ["sqrt", "log", "ln", "^"],
    ["="]
]

for row in button_texts:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill=tk.BOTH)
    for button_text in row:
        button = tk.Button(frame, text=button_text, font="Arial 18", relief=tk.GROOVE)
        button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)
        button.bind("<Button-1>", click)

# Bindings for scientific operations
def scientific_ops(event):
    text = event.widget.cget("text")
    try:
        if text == "sin":
            screen.set(sin(radians(float(screen.get()))))
        elif text == "cos":
            screen.set(cos(radians(float(screen.get()))))
        elif text == "tan":
            screen.set(tan(radians(float(screen.get()))))
        elif text == "sqrt":
            screen.set(sqrt(float(screen.get())))
        elif text == "log":
            screen.set(log10(float(screen.get())))
        elif text == "ln":
            screen.set(log(float(screen.get())))
        elif text == "^":
            screen.set(float(screen.get()) ** 2)
    except Exception:
        screen.set("Error")

# Bind scientific operation buttons
for widget in root.winfo_children():
    if isinstance(widget, tk.Frame):
        for btn in widget.winfo_children():
            if btn.cget("text") in ["sin", "cos", "tan", "sqrt", "log", "ln", "^"]:
                btn.bind("<Button-1>", scientific_ops)

# Run the main loop
root.mainloop()
