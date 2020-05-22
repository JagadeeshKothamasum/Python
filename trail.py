import tkinter
from tkinter import *
expression = ""
win = Tk()
win.geometry("400x600")
win.title("Calculator")
win.configure(bg='lightskyblue' )
equation = StringVar()
input_field=Entry(win, textvariable=equation)
input_field.place(x=20,y=80,height=50,width=350)
equation.set("                              Enter here")
def input_number(number,equation):
    global expression
    expression = expression + str(number)
    equation.set(expression)
def clear_input_field(equation):
    global expression
    expression = ""
    equation.set("                              Enter here")
def evaluate(equation):
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression=""
    except:
           expression = ""

b1 = Button(win,text = 1,padx='25',pady='25',command=lambda:input_number(1,equation))
b1.place(x=10,y=250)
b2 = Button(win,text = 2,padx='25',pady='25',command=lambda:input_number(2,equation))
b2.place(x=90,y=250)
b3 = Button(win,text = 3,padx='25',pady='25',command=lambda:input_number(3,equation))
b3.place(x=170,y=250)
b4 = Button(win,text = 4,padx='25',pady='25',command=lambda:input_number(4,equation))
b4.place(x=10,y=335)
b5 = Button(win,text = 5,padx='25',pady='25',command=lambda:input_number(5,equation))
b5.place(x=90,y=335)
b6 = Button(win,text = 6,padx='25',pady='25',command=lambda:input_number(6,equation))
b6.place(x=170,y=335)
b7 = Button(win,text = 7,padx='25',pady='25',command=lambda:input_number(7,equation))
b7.place(x=10,y=420)
b8 = Button(win,text = 8,padx='25',pady='25',command=lambda:input_number(8,equation))
b8.place(x=90,y=420)
b9 = Button(win,text = 9,padx='25',pady='25',command=lambda:input_number(9,equation))
b9.place(x=170,y=420)
b0 = Button(win,text = 0,padx='25',pady='25',command=lambda:input_number(0,equation))
b0.place(x=10,y=505)
b10 = Button(win,text = 00,padx='25',pady='25',command=lambda:input_number(00,equation))
b10.place(x=90,y=505)
bq = Button(win,text = '=',padx='25',pady='25',command=lambda:evaluate(equation))
bq.place(x=170,y=505)
ba = Button(win,text = 'AC',padx='23',pady='23',command=lambda:clear_input_field(equation))
ba.place(x=10,y=165)
o1 = Button(win,text = "+",padx='25',pady='25',command=lambda:input_number('+',equation))
o1.place(x=250,y=250)
o2 = Button(win,text = '-',padx='25',pady='25',command=lambda:input_number('-',equation))
o2.place(x=250,y=335)
o3 = Button(win,text = 'x',padx='25',pady='25',command=lambda:input_number('*',equation))
o3.place(x=250,y=420)
o4 = Button(win,text = '/',padx='25',pady='25',command=lambda:input_number('/',equation))
o4.place(x=250,y=505)
win.mainloop()
