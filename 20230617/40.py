import tkinter
from math import *

window=tkinter.Tk()
window.title("Nllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
window.geometry("500x600+100+100")
window.resizable(False, False)

entry=tkinter.Entry(window)
# entry.pack()
entry.grid(row=2, column=2)

button1 = tkinter.Button(window, text="1", overrelief="solid", width=15, command='', repeatdelay=1000, repeatinterval=100)
#button1.pack()
button1.grid(row=3, column=1)

button2 = tkinter.Button(window, text="2",overrelief="solid", width=15, command='', repeatdelay=1000, repeatinterval=100)
#button2.pack()
button2.grid(row=3, column=2)

button3 = tkinter.Button(window, text="3",overrelief="solid", width=15, command='', repeatdelay=1000, repeatinterval=100)
#button3.pack()
button3.grid(row=3, column=3)

button4 = tkinter.Button(window, text="4", overrelief="solid", width=15, command='', repeatdelay=1000, repeatinterval=100)
#button4.pack()
button4.grid(row=4, column=1)

button5 = tkinter.Button(window, text="5",overrelief="solid", width=15, command='', repeatdelay=1000, repeatinterval=100)
#button5.pack()
button5.grid(row=4, column=2)

button6 = tkinter.Button(window, text="6",overrelief="solid", width=15, command='', repeatdelay=1000, repeatinterval=100)
#button6.pack()
button6.grid(row=4, column=3)

button6 = tkinter.Button(window, text="7", overrelief="solid", width=15, command='', repeatdelay=1000, repeatinterval=100)
#button6.pack()
button6.grid(row=5, column=1)

button7 = tkinter.Button(window, text="8",overrelief="solid", width=15, command='', repeatdelay=1000, repeatinterval=100)
#button7.pack()
button7.grid(row=5, column=2)

button8 = tkinter.Button(window, text="9",overrelief="solid", width=15, command='', repeatdelay=1000, repeatinterval=100)
#button8.pack()
button8.grid(row=5, column=3)

button9 = tkinter.Button(window, text="0",overrelief="solid", width=15, command='', repeatdelay=1000, repeatinterval=100)
#button9.pack()
button9.grid(row=6, column=2)

button100 = tkinter.Button(window, text="0",overrelief="solid", width=15, command='', repeatdelay=1000, repeatinterval=100)
#button100.pack()
button100.grid(row=6, column=2)


window.mainloop()
