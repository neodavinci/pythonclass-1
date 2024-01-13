from tkinter import *

def show_message():
    message = entry.get()
    messagebox.showinfo("메시지", message)

# 윈도우 생성
window = Tk()
window.title("VS Code 스타일 윈도우")

# 레이블
label = Label(window, text="메시지 입력:")
label.pack(pady=10)

# 입력 창
entry = Entry(window, width=30)
entry.pack(pady=5)

# 버튼
button = Button(window, text="메시지 보이기", command=show_message)
button.pack(pady=10)
print("Test")

# 윈도우 실행
window.mainloop()
