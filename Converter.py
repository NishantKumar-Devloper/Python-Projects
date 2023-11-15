from tkinter import *

window=Tk()
window.title("Decimal To BINARY ")

Label(window, text="Converter", font=('Calibri',40)).grid(row=0, sticky=N)
Label(window, text="Decimal", font=('Calibri', 20)).grid(row=1,sticky=W, padx=5)
Label(window, text="Binary", font=('Calibri', 20)).grid(row=3,sticky=W, padx=5)

temp_Binary=StringVar()
temp_decimal=IntVar();temp_decimal.set(0)

DecimalEntry = Entry(window,font=('Calibri', 15), textvariable = temp_decimal)
DecimalEntry.grid(row=2,ipadx=28,column=0)
BinEntry = Entry(window,font=('Calibri', 15), textvariable = temp_Binary)
BinEntry.grid(row=4,ipadx=28,column=0)

def decimal_to_binary():
    decimal = temp_decimal.get()
    try:
        binary = bin(decimal)[2:]
        temp_Binary.set(binary)
    except ValueError:
        print("Please enter a valid decimal number")

def binary_to_decimal():
    binary = temp_Binary.get()
    try:
        decimal = int(binary, 2)
        temp_decimal.set(decimal)
    except ValueError:
        print("Please enter a valid binary number")

def convert(): 
    decimal = temp_decimal.get() 
    binary = temp_Binary.get() 
    if decimal == 0: 
        binary_to_decimal() 
    elif binary == "": 
        decimal_to_binary() 
    else: print('Please enter a value in only one entry')
Button(window, text = "Covert",font=('Calibri', 20), command = convert).grid(row=7,   sticky=W,  pady=30, padx=30)
window.mainloop()