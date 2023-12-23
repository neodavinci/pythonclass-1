
import keyboard
from tkinter import *

def key_pressed(event):
    key = event.widget.cget("text")
    if key == "Clear":
        entry.delete(0, END)
    elif key == "Enter":
        process_input()
    else:
        entry.insert(END, key)

def process_input():
    expression = entry.get()
    print("입력된 값:", expression)
    entry.delete(0, END)

def switch_to_hangul():
    keyboard.send('hangul')

window = Tk()
window.title("가상 키보드")

# 입력 창
entry = Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

# 키보드 버튼
keys = [
    ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'],
    ['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ'],
    ['ㅐ', 'ㅔ', 'ㅒ', 'ㅖ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ'],
    ['Clear', 'Enter']
]

row = 1
col = 0

for key_row in keys:
    for key in key_row:
        button = Button(window, text=key, width=5)
        button.grid(row=row, column=col, padx=5, pady=5)
        button.bind("<Button-1>", key_pressed)
        col += 1
    col = 0
    row += 1

hangul_button = Button(window, text="한/영", width=5, command=switch_to_hangul)
hangul_button.grid(row=row, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()

pip install keyboard
