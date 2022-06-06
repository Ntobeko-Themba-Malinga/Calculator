import tkinter

equation_calculation = ''
equation_text = ''
equation_display_label = None


def button_press(num):
    global equation_calculation, equation_text, equation_display_label

    equation_calculation += num

    if num == '**':
        equation_text += '^'
    elif num == '*':
        equation_text += 'x'
    else:
        equation_text += num
    equation_display_label.set(equation_text)


def clear():
    global equation_calculation, equation_text, equation_display_label

    equation_calculation = ''
    equation_text = ''
    equation_display_label.set(equation_text)


def equal():
    global equation_calculation, equation_text, equation_display_label

    try:
        equation_calculation = str(eval(equation_calculation))
        equation_text = equation_calculation
        equation_display_label.set(equation_text)
    except SyntaxError:
        equation_display_label.set('Syntax error')
    except ZeroDivisionError:
        equation_display_label.set("Arithmetic error")


def backspace():
    global equation_calculation, equation_text, equation_display_label
    equation_calculation = equation_calculation[:-1]
    equation_text = equation_text[:-1]
    equation_display_label.set(equation_text)


def main():
    window = tkinter.Tk()
    window.title("Calculator")

    # <a href="https://www.flaticon.com/free-icons/calculator" title="calculator icons">Calculator icons created by Freepik - Flaticon</a>
    icon_image = tkinter.PhotoImage(file="images/calculate.png")
    window.iconphoto(True, icon_image)

    global equation_display_label

    equation_display_label = tkinter.StringVar()

    display_label = tkinter.Label(
        master=window,
        fg='red',
        bg='black',
        font=('Arial', 30),
        width=13,
        textvariable=equation_display_label
    )
    display_label.pack(pady=5)

    frame = tkinter.Frame(master=window)
    frame.pack()

    left_parenthesis = tkinter.Button(master=frame, text="(", command=lambda: button_press("("), width=10, height=3)
    left_parenthesis.grid(row=0, column=0)

    right_parenthesis = tkinter.Button(master=frame, text=")", command=lambda: button_press(")"), width=10, height=3)
    right_parenthesis.grid(row=0, column=1)

    clear_b = tkinter.Button(master=frame, text="clear", command=clear, width=10, height=3)
    clear_b.grid(row=0, column=2)

    power = tkinter.Button(master=frame, text="^", command=lambda: button_press("**"), width=10, height=3)
    power.grid(row=0, column=3)

    button7 = tkinter.Button(master=frame, text="7", command=lambda: button_press("7"), width=10, height=3)
    button7.grid(row=1, column=0)

    button8 = tkinter.Button(master=frame, text="8", command=lambda: button_press("8"), width=10, height=3)
    button8.grid(row=1, column=1)

    button9 = tkinter.Button(master=frame, text="9", command=lambda: button_press("9"), width=10, height=3)
    button9.grid(row=1, column=2)

    multiply = tkinter.Button(master=frame, text="x", command=lambda: button_press("*"), width=10, height=3)
    multiply.grid(row=1, column=3)

    button4 = tkinter.Button(master=frame, text="4", command=lambda: button_press("4"), width=10, height=3)
    button4.grid(row=2, column=0)

    button5 = tkinter.Button(master=frame, text="5", command=lambda: button_press("5"), width=10, height=3)
    button5.grid(row=2, column=1)

    button6 = tkinter.Button(master=frame, text="6", command=lambda: button_press("6"), width=10, height=3)
    button6.grid(row=2, column=2)

    minus = tkinter.Button(master=frame, text="-", command=lambda: button_press("-"), width=10, height=3)
    minus.grid(row=2, column=3)

    button1 = tkinter.Button(master=frame, text="1", command=lambda: button_press("1"), width=10, height=3)
    button1.grid(row=3, column=0)

    button2 = tkinter.Button(master=frame, text="2", command=lambda: button_press("2"), width=10, height=3)
    button2.grid(row=3, column=1)

    button3 = tkinter.Button(master=frame, text="3", command=lambda: button_press("3"), width=10, height=3)
    button3.grid(row=3, column=2)

    plus = tkinter.Button(master=frame, text="+", command=lambda: button_press("+"), width=10, height=3)
    plus.grid(row=3, column=3)

    button0 = tkinter.Button(master=frame, text="0", command=lambda: button_press("0"), width=10, height=3)
    button0.grid(row=4, column=0)

    point = tkinter.Button(master=frame, text=".", command=lambda: button_press("."), width=10, height=3)
    point.grid(row=4, column=1)

    equal_b = tkinter.Button(master=frame, text="=", command=equal, width=10, height=3)
    equal_b.grid(row=4, column=2)

    division = tkinter.Button(master=frame, text="/", command=lambda: button_press("/"), width=10, height=3)
    division.grid(row=4, column=3)

    backspace_b = tkinter.Button(master=frame, text="delete", command=backspace, width=44, height=3)
    backspace_b.grid(row=5, column=0, columnspan=4)

    window.mainloop()


if __name__ == '__main__':
    main()
