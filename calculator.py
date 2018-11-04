"""

GUI Calculator

By Rahul Noulia

"""
from tkinter import *
from functools import partial # optional


value = ""

def click(val):
    global  value
    value = value + str(val)
    eq.set(value)


def clear():
    global value
    value = ""
    eq.set("")



def result():
    global  value
    try:
        answer = eval(value)
        eq.set(str(answer))
        value = str(answer)
    except:
        eq.set("Malformed expression")
        value = ""


if __name__=="__main__":

    root = Tk(className='Calculator')

    root.title("Calculator")

    root.geometry("450x265")
    eq = StringVar()
    root.configure(background="cyan")

    ex = Entry(root, textvariable=eq, width='56').grid(columnspan=7,ipady=20)

    Button(root, text='7', width='6', height='2' ,activebackground='#FF3E4D',command=lambda : click(7)).grid(row=1, column='1')
    Button(root, text='8', width='6', height='2' ,activebackground='#FF3E4D', command=lambda :click(8)).grid(row=1, column='2')
    Button(root, text='9', width='6', height='2',activebackground='#FF3E4D', command=lambda :click(9)).grid(row=1, column='3')

    """
     Here i use Partial function from functools module 
     USAGE :  when button is clicked then only function is called with argument .
    """
    Button(root, text='/', width='6', height='2', activebackground='#FF3E4D',command=partial(click,"/")).grid(row=1, column='4')
    Button(root, text='*', width='6', height='2', activebackground='#FF3E4D',command=lambda :click("*")).grid(row=1, column='5')
    Button(root, text='C', width='6', height='8', activebackground='#BB2CD9',bg='#BB2CD9',command=clear).grid(row=1, column='6',rowspan=3)

    Button(root, text='4', width='6', height='2', activebackground='#FF3E4D',command=lambda :click(4)).grid(row=2, column='1')
    Button(root, text='5', width='6', height='2',activebackground='#FF3E4D', command=lambda :click(5)).grid(row=2, column='2')
    Button(root, text='6', width='6', height='2',activebackground='#FF3E4D', command=lambda :click(6)).grid(row=2, column='3')
    Button(root, text='(', width='6', height='2',activebackground='#FF3E4D', command=lambda :click("(")).grid(row=2, column='4')
    Button(root, text=')', width='6', height='2', activebackground='#FF3E4D',command=lambda :click(")")).grid(row=2, column='5')

    Button(root, text='1', width='6', height='2',activebackground='#FF3E4D',command=lambda :click(1)).grid(row=3, column='1')
    Button(root, text='2', width='6', height='2',activebackground='#FF3E4D',command=lambda :click(2)).grid(row=3, column='2')
    Button(root, text='3', width='6', height='2',activebackground='#FF3E4D',command=lambda :click(3)).grid(row=3, column='3')
    Button(root, text='-', width='6', height='2',activebackground='#FF3E4D',command=lambda :click("-")).grid(row=3, column='4')
    Button(root, text='+', width='6', height='2',activebackground='#FF3E4D',command=lambda :click("+")).grid(row=3, column='5')


    Button(root, text='0', width='6', height='2',activebackground='#FF3E4D',command=lambda :click(0)).grid(row=4, column='1')
    Button(root, text='.', width='6', height='2',activebackground='#FF3E4D',command=lambda :click(".")).grid(row=4, column='2')
    Button(root, text='%', width='6', height='2',activebackground='#FF3E4D',command=lambda :click("%")).grid(row=4, column='3')
    Button(root, text='=', width='25',bg="#3498DB",activebackground="#3498DB", height='2',command=result).grid(row=4, column=4, columnspan=3)

    root.mainloop()



