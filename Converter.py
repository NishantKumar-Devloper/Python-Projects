# Converter.py

import tkinter as tk

class ConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Binary to Decimal Converter")
        self.geometry("300x250")

        self.binary_var = tk.StringVar()
        self.decimal_var = tk.IntVar()

        self.create_widgets()

    def create_widgets(self):
        # Label for binary input
        self.binary_label = tk.Label(self, text="Binary: ")
        self.binary_label.pack(padx=5, pady=5)

        # Entry for binary input
        self.binary_entry = tk.Entry(self, textvariable=self.binary_var)
        self.binary_entry.pack(padx=5, pady=5)

        # Button to convert binary to decimal
        self.convert_button = tk.Button(self, text="Convert", command=self.convert)
        self.convert_button.pack(padx=5, pady=5)

        # Label for decimal output
        self.decimal_label = tk.Label(self, text="Decimal: ")
        self.decimal_label.pack(padx=5, pady=5)

        # Entry for decimal output
        self.decimal_entry = tk.Entry(self, textvariable=self.decimal_var)
        self.decimal_entry.pack(padx=5, pady=5)
        
        self.convert_button = tk.Button(self, text="Reset", command=self.reset)
        self.convert_button.pack(padx=5, pady=5)

    def binary_to_decimal(self):
        binary_string = self.binary_var.get()
        decimal_number = int(binary_string, 2)
        self.decimal_var.set(decimal_number)
    def decimal_to_binary(self):
        decimal = self.decimal_var.get()
        try:
            binary = bin(decimal)[2:]
            self.binary_var.set(binary)
            self.reset
        except ValueError:
            print("Please enter a valid decimal number")
    
    def convert(self):  
        if self.decimal_var.get()  == 0: 
            self.binary_to_decimal()
        elif self.binary_var.get()  == "": 
            self.decimal_to_binary()
    def reset(self):
        self.decimal_var.set(0)
        self.binary_var.set('')
if __name__=='__main__':
    app=ConverterApp().mainloop()