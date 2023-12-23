import tkinter
from math import *

window=tkinter.Tk()
window.title("Nllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
window.geometry("450x550+100+100")
window.resizable(False, False)



#def keyin(argment1):

entry=tkinter.Entry(window, width=30)
# entry.pack()
entry.grid(row=0, column=0, columnspan=20)



button2 = tkinter.Button(window, text="9",overrelief="solid", width=10, height=6,command='', repeatdelay=1000, repeatinterval=100)
#button2.pack()
button2.grid(row=3, column=4)
button3 = tkinter.Button(window, text="8",overrelief="solid", width=10, height=6,command='', repeatdelay=1000, repeatinterval=100)
#button3.pack()
button3.grid(row=3, column=3)
button4 = tkinter.Button(window, text="7",overrelief="solid", width=10, height=6,command='', repeatdelay=1000, repeatinterval=100)
#button4.pack()
button4.grid(row=3, column=2)
buttondiv = tkinter.Button(window, text="/",overrelief="solid", width=10, height=6,command='', repeatdelay=1000, repeatinterval=100)
#button4.pack()
buttondiv.grid(row=3, column=5)


button5 = tkinter.Button(window, text="6",overrelief="solid", width=10, height=6,command='', repeatdelay=1000, repeatinterval=100)
#button5.pack()
button5.grid(row=4, column=4)
button6 = tkinter.Button(window, text="5",overrelief="solid", width=10, height=6,command='', repeatdelay=1000, repeatinterval=100)
#button6.pack()
button6.grid(row=4, column=3)
button6 = tkinter.Button(window, text="4",overrelief="solid", width=10, height=6,command='', repeatdelay=1000, repeatinterval=100)
#button6.pack()
button6.grid(row=4, column=2)


button7 = tkinter.Button(window, text="3",overrelief="solid", width=10, height=6,command='', repeatdelay=1000, repeatinterval=100)
#button7.pack()
button7.grid(row=5, column=4)
button8 = tkinter.Button(window, text="2",overrelief="solid", width=10, height=6,command='', repeatdelay=1000, repeatinterval=100)
#button8.pack()
button8.grid(row=5, column=3)
button9 = tkinter.Button(window, text="1",overrelief="solid", width=10, height=6,command='', repeatdelay=1000, repeatinterval=100)
#button9.pack()
button9.grid(row=5, column=2)


button1 = tkinter.Button(window, text="0",overrelief="solid", width=10, height=6,command='', repeatdelay=1000, repeatinterval=100)
#button1.pack()
button1.grid(row=7, column=3)


button1 = tkinter.Button(window, text="=",overrelief="solid", width=10, height=6,command='', repeatdelay=1000, repeatinterval=100)
#button1.pack()
button1.grid(row=8, column=3)

#A136C2











window.mainloop()