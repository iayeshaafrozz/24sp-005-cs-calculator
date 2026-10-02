import tkinter as tk


def press(value):
    if value == "C":
        display.delete(0, tk.END)

    elif value == "=":
        try:
            expression = display.get()
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(0, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")

    else:
        display.insert(tk.END, value)


# Main window
window = tk.Tk()
window.title("Ashly's Calculator")
window.geometry("800x950")
window.resizable(False, False)
window.configure(bg="#f7e6f2")

# Title
title = tk.Label(
    window,
    text="Ashly's Calculator",
    font=("Arial", 24, "bold"),
    bg="#f7e6f2",
    fg="#7a3e65"
)
title.pack(pady=20)

# Display
display = tk.Entry(
    window,
    font=("Arial", 28),
    justify="right",
    bd=3,
    relief="solid"
)
display.pack(
    padx=25,
    pady=10,
    fill="x",
    ipady=12
)

# Calculator buttons
button_frame = tk.Frame(window, bg="#f7e6f2")
button_frame.pack(padx=20, pady=20)

buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("C", 3, 0), ("0", 3, 1), (".", 3, 2), ("+", 3, 3),
]

for text, row, column in buttons:
    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 18, "bold"),
        width=5,
        height=2,
        command=lambda value=text: press(value)
    )
    button.grid(
        row=row,
        column=column,
        padx=6,
        pady=6
    )

# Equal button
equal_button = tk.Button(
    button_frame,
    text="=",
    font=("Arial", 18, "bold"),
    width=23,
    height=2,
    command=lambda: press("=")
)

equal_button.grid(
    row=4,
    column=0,
    columnspan=4,
    padx=6,
    pady=6
)

window.mainloop()