from tkinter import *

window = Tk()
window.title('Simple Calc')
window.iconbitmap('favicon.ico')

e = Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=5)


def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def buttonClear():
    e.delete(0, END)

def buttonAdd():
    firstNum = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(firstNum)
    e.delete(0, END)

def buttonMinus():
    firstNum = e.get()
    global f_num
    global math
    math = 'substraction'
    f_num = int(firstNum)
    e.delete(0, END)

def buttonMultiple():
    firstNum = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(firstNum)
    e.delete(0, END)

def buttonDivide():
    firstNum = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(firstNum)
    e.delete(0, END)

def buttonEqual():
    secondNum = e.get()
    s_num = int(secondNum)
    e.delete(0, END)

    if math == 'addition':
        out = f_num + s_num
        e.insert(0, out)

    if math == 'multiplication':
        out = f_num * s_num
        e.insert(0, out)

    if math == 'addition':
        out = f_num + s_num
        e.insert(0, out)

    if math == 'division':
        out = f_num / s_num
        e.insert(0, out)

button1 = Button(window, text='1', padx=40, pady=20, command=lambda: buttonClick(1))
button2 = Button(window, text='2', padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(window, text='3', padx=40, pady=20, command=lambda: buttonClick(3))
button4 = Button(window, text='4', padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(window, text='5', padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(window, text='6', padx=40, pady=20, command=lambda: buttonClick(6))
button7 = Button(window, text='7', padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(window, text='8', padx=40, pady=20, command=lambda: buttonClick(8))
button9 = Button(window, text='9', padx=40, pady=20, command=lambda: buttonClick(9))
button0 = Button(window, text='0', padx=40, pady=20, command=lambda: buttonClick(0))
buttonAdd = Button(window, text='+', padx=39, pady=20, command=buttonAdd)
butonEqual = Button(window, text='=', padx=90, pady=20, command=lambda: buttonEqual())
buttonClear = Button(window, text='Clear', padx=79, pady=20, command=buttonClear)
buttonMinus = Button(window, text='-', padx=39, pady=20, command=buttonMinus)
buttonMultiple = Button(window, text='*', padx=39, pady=20, command=buttonMultiple)
buttonDivide = Button(window, text='/', padx=39, pady=20, command=buttonDivide)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonAdd.grid(row=4, column=1)
buttonMinus.grid(row=4, column=2)

buttonMultiple.grid(row=5, column=0)
butonEqual.grid(row=5, column=1,columnspan=2)
#
buttonDivide.grid(row=6, column=0)
buttonClear.grid(row=6, column=1, columnspan=2)


window.mainloop()