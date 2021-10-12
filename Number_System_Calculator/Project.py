from tkinter import *

home = Tk()
home.maxsize(width="440", height="650")
home['bg']="Cyan"
home.title="Number_System_Converter"

title = Label(home, text="Number_System_Converter", font=('Tesla', 16, 'bold'), fg='RoyalBlue', bg='Cyan')
title.pack(fill='x')

inputfield = Entry(home, font=('Cyberway Riders', 20), fg='Gray25', bg='Gray85', relief='sunken', bd=10)
inputfield.pack(fill='x', pady=20)

def key(value):
        inputfield.insert(END, value)

def clear():
    inputfield.delete(0,END)
    display.configure(state='normal')
    display.delete(1.0, END)
    display.configure(state='disabled')

Numeric = LabelFrame(home, text='Numeric Keys', bg='cyan')
Numeric.pack(fill='x', pady=10)
button7 = Button(Numeric, text='7', font=('Arial', 20), fg='Green', bg='Cyan2', width=8, command= lambda : key(7))
button7.grid(row=0, column=0)
button8 = Button(Numeric, text='8', font=('Arial', 20), fg='Green', bg='Cyan2', width=8, command= lambda : key(8))
button8.grid(row=0, column=1)
button9 = Button(Numeric, text='9', font=('Arial', 20), fg='Green', bg='Cyan2', width=8, command= lambda : key(9))
button9.grid(row=0, column=2)
button4 = Button(Numeric, text='4', font=('Arial', 20), fg='Green', bg='Cyan2', width=8, command= lambda : key(4))
button4.grid(row=1, column=0)
button5 = Button(Numeric, text='5', font=('Arial', 20), fg='Green', bg='Cyan2', width=8, command= lambda : key(5))
button5.grid(row=1, column=1)
button6 = Button(Numeric, text='6', font=('Arial', 20), fg='Green', bg='Cyan2', width=8, command= lambda : key(6))
button6.grid(row=1, column=2)
button1 = Button(Numeric, text='1', font=('Arial', 20), fg='Green', bg='Cyan2', width=8, command= lambda : key(1))
button1.grid(row=2, column=0)
button2 = Button(Numeric, text='2', font=('Arial', 20), fg='Green', bg='Cyan2', width=8, command= lambda : key(2))
button2.grid(row=2, column=1)
button3 = Button(Numeric, text='3', font=('Arial', 20), fg='Green', bg='Cyan2', width=8, command= lambda : key(3))
button3.grid(row=2, column=2)
button0 = Button(Numeric, text='0', font=('Arial', 20), fg='Green', bg='Cyan2', width=17, command= lambda : key(0))
button0.grid(row=3, column=0, columnspan=2)
buttonclear = Button(Numeric, text='Clear', font=('Arial', 20), fg='Green', bg='Cyan2', width=8, command= clear)
buttonclear.grid(row=3, column=2)

def Binary():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        val = int(inputfield.get(), 2)
        display.insert(END,'Octal      =  ' + str(oct(val))[2:])
        display.insert(END,'\nDecimal  =  ' + str(val))
        display.insert(END,'\nHexaDec = ' + str(hex(val))[2:])
    except:
        display.insert(END,'Invalid Input')
    display.configure(state='disabled')


def Octal():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        val = int(inputfield.get(), 8)
        display.insert(END,'Binary    =  ' + str(bin(val))[2:])
        display.insert(END,'\nDecimal  =  ' + str(val))
        display.insert(END,'\nHexaDec = ' + str(hex(val))[2:])
    except:
        display.insert(END, 'Invalid Input')
    display.configure(state='disabled')


def Decimal():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        val = int(inputfield.get())
        display.insert(END,'Binary    =  ' + str(bin(val))[2:])
        display.insert(END,'\nOctal      =  ' + str(oct(val))[2:])
        display.insert(END,'\nHexaDec = ' + str(hex(val))[2:])
    except:
        display.insert(END, 'Invalid Input')
    display.configure(state='disabled')


def Hexadecimal():
    display.configure(state='normal')
    display.delete(1.0, END)
    try:
        val = int(inputfield.get(), 16)
        display.insert(END,'Binary   =  ' + str(bin(val))[2:])
        display.insert(END,'\nOctal     =  ' + str(oct(val))[2:])
        display.insert(END,'\nDecimal = ' + str(val))
    except:
        display.insert(END, 'Invalid Input')
    display.configure(state='disabled')

button = LabelFrame(home, text="Input Type Data ", bg='cyan')
button.pack(fill='both', pady=5)
binaryButton = Button(button, text="Binary", font=('Arial', 15), fg='Green', bg='Cyan2', width=18, command=Binary)
binaryButton.grid(row=0, column=0)
octalButton = Button(button, text="Octal", font=('Arial', 15), fg='Green', bg='Cyan2', width=18, command=Octal)
octalButton.grid(row=0, column=1)
decimalButton = Button(button, text="Decimal", font=('Arial', 15), fg='Green', bg='Cyan2', width=18, command=Decimal)
decimalButton.grid(row=1, column=0)
hexaButton = Button(button, text="Hexa Decimal", font=('Arial', 15), fg='Green', bg='Cyan2', width=18, command=Hexadecimal)
hexaButton.grid(row=1, column=1)

display = Text(home, font=('Arial', 18), fg='Gray25', bg='Gray85', relief='raised', bd=5)
display.pack(fill='x')
display.configure(state='disabled')

home.mainloop()

