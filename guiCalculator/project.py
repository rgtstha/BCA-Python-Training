from tkinter import *
from tkinter import ttk

def operation(value1,value2, fakeoperator):
    global lastResult

    if(type(value1)==float or type(value1)==int and type(value2)==float or type(value2)==int ):
        print(value1)
        print(value2)
        print(fakeoperator)
        match fakeoperator:
            case "+":
                return  value1 + value2
            case "-": 
                return value1 - value2
            case "*":
                return value1 * value2
            case "/":   
                return  value1 / value2
            case default:
                return 


def clearButton():
    global currentValue
    global lastResult
    currentValue = 0
    lastResult = 0
    screenUpdate(0)


root = Tk()
root.geometry("700x700")

lastResult = 0
currentValue = 0
temporaryValue = 0
operator = ""

lastresultBox = ttk.Label(text="Samundra is Code God",borderwidth=5,relief='solid',foreground="gray",font=24,width=20)
lastresultBox.grid(row=1,column=1,columnspan=7,pady=5)

displayBox = ttk.Label(text="0",borderwidth=5,relief='solid',foreground="red",font=24,width=20)
displayBox.grid(row=2,column=1,columnspan=7,pady=5)

def screenUpdate(clickedValue):
    global currentValue 
    currentValue = currentValue * 10 + clickedValue
    displayBox.configure(text=currentValue)
    lastresultBox.configure(text=lastResult)
    

def EqualUpdate():
    global lastResult
    global currentValue
    global operator

    lastResult = operation(lastResult,currentValue,operator)
    lastresultBox.configure(text=lastResult)

    currentValue = 0
    displayBox.configure(text=currentValue)

def OperatorsClicked(sign):
    global operator
    global lastResult
    global currentValue

    if(lastResult!=0):
        lastResult = operation(lastResult,currentValue,operator)
    else:
        lastResult = currentValue

    operator = sign    
    currentValue = 0
    screenUpdate(0)


button1 = ttk.Button(text="1",width=5,command=lambda:screenUpdate(1))
button1.grid(row=5,column=1)
button2 = ttk.Button(text="2",width=5,command=lambda:screenUpdate(2))
button2.grid(row=5,column=3)
button3 = ttk.Button(text="3",width=5,command=lambda:screenUpdate(3))
button3.grid(row=5,column=5)
buttonClear = ttk.Button(text="C",width=5,command=lambda:clearButton())
buttonClear.grid(row=5,column=7)

button4 = ttk.Button(text="4",width=5,command=lambda:screenUpdate(4))
button4.grid(row=7,column=1)
button5 = ttk.Button(text="5",width=5,command=lambda:screenUpdate(5))
button5.grid(row=7,column=3)
button6 = ttk.Button(text="6",width=5,command=lambda:screenUpdate(6))
button6.grid(row=7,column=5)
buttonPlus = ttk.Button(text="+",width=5, command= lambda:OperatorsClicked("+"))
buttonPlus.grid(row=7,column=7)

button7 = ttk.Button(text="7",width=5,command=lambda:screenUpdate(7))
button7.grid(row=9,column=1)
button8 = ttk.Button(text="8",width=5,command=lambda:screenUpdate(8))
button8.grid(row=9,column=3)
button9 = ttk.Button(text="9",width=5,command=lambda:screenUpdate(9))
button9.grid(row=9,column=5)
buttonMultiply = ttk.Button(text="*",width=5,command=lambda:OperatorsClicked("*"))
buttonMultiply.grid(row=9,column=7)

button0 = ttk.Button(text="0",width=13,command=lambda:screenUpdate(0))
button0.grid(row=11,column=1,columnspan=4)
buttonSubtract = ttk.Button(text="-",width=5,command= lambda:OperatorsClicked("-"))
buttonSubtract.grid(row=11,column=5)
buttonDivide = ttk.Button(text="/",width=5,command= lambda:OperatorsClicked("/"))
buttonDivide.grid(row=11,column=7)


buttonEquals = Button(text="=",foreground='red',width=5,borderwidth=2, relief="groove",command=EqualUpdate)
buttonEquals.grid(row=13,column=7)



root.mainloop()

