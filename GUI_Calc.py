
from tkinter import *

BG_MAIN = "#000000"
BG_DISPLAY = "#121212"
BG_NUM = "#262626"
BG_NUM_ACTIVE = "#414141"
BG_ORANGE = "#FF9500"
BG_ORANGE_ACTIVE = "#FFB143"
FG_WHITE = "#FFFFFF"

equation_text = ""

def button_press(num):
    global equation_text

    if equation_text in ("Syntax Error", "Math Error"):
        equation_text = ""

    equation_text += str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text

    if not equation_text:
        return

    try:
        expression = equation_text.replace("×", "*").replace("÷", "/")
        total = str(eval(expression, {"__builtins__": None}, {}))

        if isinstance(total, float):
            pass

        equation_label.set(total)
        equation_text = total

    except ZeroDivisionError:
        equation_label.set("Math Error")
        equation_text = ""

    except Exception:
        equation_label.set("Syntax Error")
        equation_text = ""


def clear_calculator():
    global equation_text
    equation_text = ""
    equation_label.set("")


def delete_last():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)


window = Tk()
window.title("Calculator")
window.geometry("420x600")
window.resizable(False, False)
window.configure(bg=BG_MAIN)

equation_label = StringVar()

display_frame = Frame(
    window,
    bg=BG_DISPLAY,
    padx=20,
    pady=30
)
display_frame.pack(fill=X, padx=15, pady=(15, 12))

label = Label(
    display_frame,
    textvariable=equation_label,
    font=("Arial", 30, "bold"),
    bg=BG_DISPLAY,
    fg=FG_WHITE,
    anchor="e",
    height=2
)
label.pack(fill=X)

frame = Frame(window, bg=BG_MAIN, padx=15, pady=10)
frame.pack(expand=True, fill=BOTH)

for r in range(5):
    frame.rowconfigure(r, weight=1)

for c in range(4):
    frame.columnconfigure(c, weight=1)

num_style = {
    "font": ("Arial", 19, "bold"),
    "bg": BG_NUM,
    "fg": FG_WHITE,
    "activebackground": BG_NUM_ACTIVE,
    "activeforeground": FG_WHITE,
    "bd": 0,
    "relief": FLAT,
    "cursor": "hand2"
}

op_style = {
    "font": ("Arial", 19, "bold"),
    "bg": BG_ORANGE,
    "fg": BG_MAIN,
    "activebackground": BG_ORANGE_ACTIVE,
    "activeforeground": BG_MAIN,
    "bd": 0,
    "relief": FLAT,
    "cursor": "hand2"
}


def make_button(text, row, col, command, style, colspan=1):
    btn = Button(
        frame,
        text=text,
        command=command,
        **style
    )

    btn.grid(
        row=row,
        column=col,
        columnspan=colspan,
        padx=6,
        pady=6,
        sticky="nsew"
    )

    return btn


make_button("C", 0, 0, clear_calculator, num_style)
make_button("DEL", 0, 1, delete_last, num_style)
make_button("÷", 0, 2, lambda: button_press("÷"), op_style)
make_button("×", 0, 3, lambda: button_press("×"), op_style)

make_button("7", 1, 0, lambda: button_press(7), num_style)
make_button("8", 1, 1, lambda: button_press(8), num_style)
make_button("9", 1, 2, lambda: button_press(9), num_style)
make_button("-", 1, 3, lambda: button_press("-"), op_style)

make_button("4", 2, 0, lambda: button_press(4), num_style)
make_button("5", 2, 1, lambda: button_press(5), num_style)
make_button("6", 2, 2, lambda: button_press(6), num_style)
make_button("+", 2, 3, lambda: button_press("+"), op_style)

make_button("1", 3, 0, lambda: button_press(1), num_style)
make_button("2", 3, 1, lambda: button_press(2), num_style)
make_button("3", 3, 2, lambda: button_press(3), num_style)
make_button("0", 4, 0, lambda: button_press(0), num_style, colspan=2)

make_button(".", 4, 2, lambda: button_press("."), num_style)
make_button("=", 4, 3, equals, op_style)


def key_handler(event):
    char = event.char

    if char in "0123456789+-*/.":
        button_press(char)

    elif event.keysym in ("Return", "KP_Enter"):
        equals()

    elif event.keysym == "BackSpace":
        delete_last()

    elif event.keysym == "Escape":
        clear_calculator()


window.bind("<Key>", key_handler)

window.mainloop()
