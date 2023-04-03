#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *

# global variables declaration:
starting_input=1
Operation_Number=1
# functions for number buttons
def myClick(string):
    global starting_input
    if(starting_input==1):
        display_panel.delete(0,END) # this is to clear the resule of the last completed calculation
        display_panel.insert(0,str(string))
        starting_input+=1
    else:
        disp_ini=display_panel.get()
        display_panel.delete(0,END)
        disp_fin=str(disp_ini)+str(string)
        display_panel.insert(0,disp_fin)
        starting_input+=1
def myClickOpr(string):
    global Operation_Number
    if(Operation_Number==1):
        disp_ini=display_panel.get()
        global num1
        global opr
        num1 = disp_ini
        opr = string
        display_panel.delete(0,END)
        Operation_Number+=1
    else:
        global num2
        num2 = display_panel.get()
        display_panel.delete(0,END)
        if(opr=="+"):
            result=float(num1)+float(num2)
        elif(opr=="-"):
            result=float(num1)-float(num2)
        elif(opr=="*"):
            result=float(num1)*float(num2)
        elif(opr=="/"):
            result=float(num1)/float(num2)
        num1=str(result)
        opr=string
        display_panel.delete(0,END)
        Operation_Number+=1
def myClickPercentage():
    global starting_input
    global Operation_Number
    disp_ini=display_panel.get()
    display_panel.delete(0,END)
    global num2
    num2 = disp_ini
    if(opr=="+"):
        result=float(num1)+(float(num1)*float(num2)/100)
    elif(opr=="-"):
        result=float(num1)-(float(num1)*float(num2)/100)
    elif(opr=="*"):
        result=float(num1)*(float(num2)/100)
    elif(opr=="/"):
        result=float(num1)/(float(num2)/100)
    stres=str(result)
    display_panel.insert(0,stres)
    starting_input=1
    Operation_Number=1
def myClickEqual():
    global starting_input
    global Operation_Number
    global num2
    num2 = display_panel.get()
    display_panel.delete(0,END)
    if(opr=="+"):
        result=float(num1)+float(num2)
    elif(opr=="-"):
        result=float(num1)-float(num2)
    elif(opr=="*"):
        result=float(num1)*float(num2)
    elif(opr=="/"):
        result=float(num1)/float(num2)
    stres=str(result)
    display_panel.insert(0,stres)
    starting_input=1
    Operation_Number=1

def myClickClear():
    global starting_input
    global Operation_Number
    starting_input=1
    Operation_Number=1
    display_panel.delete(0,END)
    
# Main Box
root=Tk()
root.title("Simple Calculator")
#LCD Display
display_panel=Entry(root,width=50,borderwidth=2)
display_panel.grid(row=0,column=0,columnspan=5, padx=10,pady=10)

# Buttons Definitions
button_1=Button(root,text="1",width=10,borderwidth=3, command=lambda: myClick("1"))
button_2=Button(root,text="2",width=10,borderwidth=3, command=lambda: myClick("2"))
button_3=Button(root,text="3",width=10,borderwidth=3, command=lambda: myClick("3"))
button_4=Button(root,text="4",width=10,borderwidth=3, command=lambda: myClick("4"))
button_5=Button(root,text="5",width=10,borderwidth=3, command=lambda: myClick("5"))
button_6=Button(root,text="6",width=10,borderwidth=3, command=lambda: myClick("6"))
button_7=Button(root,text="7",width=10,borderwidth=3, command=lambda: myClick("7"))
button_8=Button(root,text="8",width=10,borderwidth=3, command=lambda: myClick("8"))
button_9=Button(root,text="9",width=10,borderwidth=3, command=lambda: myClick("9"))
button_zero=Button(root,text="0",width=10,borderwidth=3, command=lambda: myClick("0"))
button_decimal=Button(root,text=".",width=10,borderwidth=3, command=lambda: myClick("."))

button_add=Button(root,text="+",width=10,borderwidth=3,bg="blue",fg="white", command=lambda: myClickOpr("+"))
button_subtract=Button(root,text="-",width=10,borderwidth=3, command=lambda: myClickOpr("-"))
button_multiplication=Button(root,text="x",width=10,borderwidth=3, command=lambda: myClickOpr("*"))
button_division=Button(root,text="/",width=10,borderwidth=3, command=lambda: myClickOpr("/"))
button_percentage=Button(root,text="%",width=10,borderwidth=3, command=myClickPercentage)
button_equal=Button(root,text="=",width=23,borderwidth=3,bg="blue",fg="white", command=myClickEqual)
button_clear=Button(root,text="Clear",width=23,borderwidth=3,bg="red",fg="black", command=myClickClear)

#Buttons Positioning
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_division.grid(row=1,column=3)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_multiplication.grid(row=2,column=3)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_subtract.grid(row=3,column=3)
button_decimal.grid(row=4,column=0)
button_zero.grid(row=4,column=1)
button_percentage.grid(row=4,column=2)
button_add.grid(row=4,column=3)
button_equal.grid(row=5,column=2, columnspan=2)
button_clear.grid(row=5,column=0, columnspan=2)
root.mainloop()


# In[ ]:




