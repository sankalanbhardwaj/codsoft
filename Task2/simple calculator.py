from tkinter import*

root=Tk()

root.title("Simple Calculator")

e = Entry(root, width=15, borderwidth=5, font=("Arial", 20), justify='right')
e.grid(row=0, column=0, columnspan=4, ipady=10, padx=10, pady=10)


def button_click(number):

    

    current=e.get()

    e.delete(0,END)

    e.insert(0,str(current)+str(number))
 
 
def button_clear():

    e.delete(0,END)

def operation(op):

    global f_num,math_op

    f_num=float(e.get())

    math_op=op

    e.delete(0,END)

def button_equal():

    global f_num,math_op

    second_number=float(e.get())

    e.delete(0,END)


    result=0

    if math_op=="+":

      result=f_num+second_number

    elif math_op=="-":

      result=f_num-second_number

    elif math_op=="*":

      result=f_num*second_number

    elif math_op=="/":

        if second_number!=0:

            result=f_num/second_number

        else:

            result="error"

    e.insert(0,result)


 
 
button_1=Button(root,text="1",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(1))

button_2=Button(root,text="2",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(2))

button_3=Button(root,text="3",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(3))

button_4=Button(root,text="4",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(4))

button_5=Button(root,text="5",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(5))

button_6=Button(root,text="6",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(6))

button_7=Button(root,text="7",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(7))

button_8=Button(root,text="8",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(8))

button_9=Button(root,text="9",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(9))

button_0=Button(root,text="0",padx=20,pady=20,font=("Arial",14),command=lambda:button_click(0))

button_add=Button(root,text="+",padx=20,pady=20,font=("Arial",14),command=lambda:operation("+"))

button_sub=Button(root,text="-",padx=22,pady=20,font=("Arial",14),command=lambda:operation("-"))

button_mul=Button(root,text="*",padx=20,pady=20,font=("Arial",14),command=lambda:operation("*"))

button_div=Button(root,text="/",padx=24,pady=20,font=("Arial",14),command=lambda:operation("/"))

button_equal=Button(root,text="=",padx=20,pady=20,font=("Arial",14),command=button_equal)

button_crear=Button(root,text="Clr",padx=16,pady=24,font=("Arial",13),command=button_clear)



button_1.grid(row=3,column=0)

button_2.grid(row=3,column=1)

button_3.grid(row=3,column=2)         

button_4.grid(row=2,column=0)

button_5.grid(row=2,column=1)

button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)

button_8.grid(row=1,column=1)

button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_crear.grid(row=1,column=3)

button_add.grid(row=2,column=3)

button_sub.grid(row=3,column=3)

button_mul.grid(row=4,column=1)

button_div.grid(row=4,column=2)
 
button_equal.grid(row=4,column=3)
 
 
root.mainloop()
 