from tkinter import *

equation_text= "" #I have declaring a variable has equation_text as a empty string
def press(num):
    global equation_text#It allows you to change a variable value outside of its current scope

    equation_text = equation_text + str(num)

    x.set(equation_text)

def equal():
    try:
        global equation_text

        #it will eval it which was given in equation_text
        total= str(eval(equation_text))

        x.set(total)

        #reusing the total
        equation_text=total
    except ZeroDivisionError:
        x.set("Arithmetic error")
        #once epo artimetic error vanthchi na apram ne type panamothu ne pota antha example(5/0)
        #apiya erkum athu cleear pana than again equation_text="" empty strig ha podranga
        equation_text=""
    except SyntaxError:
        x.set("Syntax Error")
        equation_text=""

def clear():
    global equation_text
    x.set("")
    equation_text=""


window=Tk()
window.title("Calculator")
window.geometry("500x500")

#we were declaring 'x' has a stringvariable
x=StringVar()

val_label=Label(window,textvariable=x,font=25,height=3,width=24,fg="black",bg="white",
                relief=SUNKEN,bd=5,padx=2,pady=3)
val_label.pack()

frame=Frame(window,relief=SUNKEN,bd=5)
frame.pack()

button1=Button(frame,font=35,text=1,height=2,width=5,fg="green",bg="black",
               activebackground="black",activeforeground="green",
               command=lambda : press(1))
button1.grid(row=0,column=0)

button2=Button(frame,font=35,text=2,height=2,width=5,fg="green",bg="black",
               activebackground="black",activeforeground="green",
               command= lambda:press(2))
button2.grid(row=0,column=1)

button3=Button(frame,font=35,text=3,height=2,width=5,fg="green",bg="black",
               activebackground="black",activeforeground="green",
               command=lambda:press(3))
button3.grid(row=0,column=2)

plus_button=Button(frame,text="+",font=35,height=2,width=5,fg="green",bg="black",
            activebackground="black",activeforeground="green",
            command=lambda:press("+"))
plus_button.grid(row=0,column=3)

button4=Button(frame,text=4,font=35,height=2,width=5,fg="green",bg="black",
               activebackground="black",activeforeground="green",
               command=lambda:press(4))
button4.grid(row=1,column=0)

button5=Button(frame,text=5,font=35,height=2,width=5,fg="green",bg="black",
               activebackground="black",activeforeground="green",
               command=lambda:press(5))
button5.grid(row=1,column=1)

button6=Button(frame,text=6,font=35,height=2,width=5,fg="green",bg="black",
               activebackground="black",activeforeground="green",
               command=lambda:press(6))
button6.grid(row=1,column=2)

minus_button=Button(frame,text="-",font=35,height=2,width=5,fg="green",bg="black",
             activebackground="black",activeforeground="green",
             command=lambda:press("-"))
minus_button.grid(row=1,column=3)

button7=Button(frame,text=7,font=35,height=2,width=5,fg="green",bg="black",
               activebackground="black",activeforeground="green",
               command=lambda:press(7))
button7.grid(row=2,column=0)

button8=Button(frame,text=8,font=35,height=2,width=5,fg="green",bg="black",
               activebackground="black",activeforeground="green",
               command=lambda:press(8))
button8.grid(row=2,column=1)

button9=Button(frame,text=9,font=35,height=2,width=5,fg="green",bg="black",
               activebackground="black",activeforeground="green",
               command=lambda:press(9))
button9.grid(row=2,column=2)

multiply=Button(frame,text="*",font=35,height=2,width=5,fg="green",bg="black",
                activebackground="black",activeforeground="green",
                command=lambda:press("*"))
multiply.grid(row=2,column=3)

dot_button=Button(frame,text=".",font=35,height=2,width=5,fg="green",bg="black",
           activebackground="black",activeforeground="green",
           command=lambda:press("."))
dot_button.grid(row=3,column=0)

button0=Button(frame,text=0,font=35,height=2,width=5,fg="green",bg="black",
               activebackground="black",activeforeground="green",
               command=lambda:press(0))
button0.grid(row=3,column=1)

divide_button=Button(frame,text="/",font=35,height=2,width=5,fg="green",bg="black",
              activebackground="black",activeforeground="green",
              command=lambda:press("/"))
divide_button.grid(row=3,column=2)

equal_button=Button(frame,text="=",font=35,height=2,width=5,fg="green",bg="black",
             activebackground="black",activeforeground="green",
             command=equal)
equal_button.grid(row=3,column=3)

clear_button=Button(frame,text="clear",font=(20),height=2,width=8,command=clear,
             relief=RAISED,bd=5)
clear_button.grid(row=4,column=2,columnspan=2)

window.mainloop()

