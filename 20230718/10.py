#파이썬으로 GUI 계산기 프로그램 만들기
#계산기 프로그램을 만들어보자. 이번에는 GUI를 사용하여 계산기 프로그램을 만들어보자.
#Tkinter 모듈을 사용하여 GUI를 만들 수 있다. Tkinter는 파이썬에서 기본적으로 제공하는 GUI 라이브러리이다.
#Tkinter를 사용하여 간단한 계산기 프로그램을 만들어보자.
#Tkinter 모듈을 사용하기 위해서는 다음과 같이 import하여 사용한다.
from tkinter import *

#계산기 버튼을 눌렀을 때 실행되는 함수
def keyIn(key):
    if key == "=":
        result = eval(display.get())
        display.insert(END, "=" + str(result))
    else:
        display.insert(END, key)
        
#Tk 객체 인스턴스 생성
window = Tk()
window.title("계산기")
#윈도우 크기 조절 불가능
window.resizable(False, False)

#엔트리 위젯 생성
display = Entry(window, width=33, bg="yellow")
display.grid(row=0, column=0, columnspan=5)

#버튼 생성
buttonList = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

rowIndex = 1
colIndex = 0
for button in buttonList:
    def process(t=button):
        keyIn(t)
    Button(window, text=button, width=5, command=process).grid(row=rowIndex, column=colIndex)
    colIndex += 1
    if colIndex > 3:
        rowIndex += 1
        colIndex = 0

#윈도우 객체를 생성하고 윈도우 창을 윈도우 시스템에 표시
window.mainloop()


