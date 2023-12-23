from tkinter import *

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

window = Tk()
window.title("계산기")

entry = Entry(window, width=25)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        btn = Button(window, text=button, width=10, command=calculate)
        btn.grid(row=row, column=col, padx=5, pady=5)
    else:
        btn = Button(window, text=button, width=5, command=lambda x=button: entry.insert(END, x))
        btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()
