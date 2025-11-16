import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel

euro =  1.32
dollars = 1.13

currencies = ['Euros','Dollars']

def convert():
    amount = float(root2_entry.get())
    
    if currency == 'Euros':
        result = (euro * amount)
    elif currency == 'Dollars':
        result = (dollars * amount)

    converted = Toplevel()
    converted.geometry('215x100')
    converted.minsize(215,100)
    converted.maxsize(215,108)

    converted_title = tk.Label(
        converted,
        text=(f'Pounds to {currency}'),
        font=('Arial',15,'bold')
    )
    converted_title.grid(
        row=1,
        column=1,
        columnspan=2
    )

    pounds_label = tk.Label(
        converted,
        text='Pounds:',
        font=('Arial',15),
    )
    pounds_label.grid(
        row=2,
        column=1,
    )

    pounds_converted = tk.Label(
        converted,
        text=amount,
        font=('Arial',15)
    )
    pounds_converted.grid(
        row=2,
        column=2
    )

    currency_label = tk.Label(
        converted,
        text=f'{currency}:',
        font=('Arial',15),
    )
    currency_label.grid(
        row=3,
        column=1,
    )

    currency_converted = tk.Label(
        converted,
        text=f'{result:.2f}',
        font=('Arial',15)
    )
    currency_converted.grid(
        row=3,
        column=2
    )

    back_button = tk.Button(
        converted,
        text='Back',
        width=20,
        command=converted.destroy
    )
    back_button.grid(
        row=4,
        column=1,
        columnspan=2
    )
        
def checkcurrency():
    global currency
    currency = root_entry.get()


    if currency in currencies:
        convert()
    else:
        messagebox.showinfo('Error','Unfortunately, this currency is not supported')

root = tk.Tk()
root.title('Currency Converter')
root.geometry('270x140')
root.minsize(270,140)
root.maxsize(270,140)

root_title = tk.Label(
    root,
    text='Currency Converter',
    font=('Arial',15,'bold')
)
root_title.grid(
    row=1,
    column=1,
    columnspan=2
)

root_label = tk.Label(
    root,
    text='Pounds to',
    font=('Arial',15)
)
root_label.grid(
    row=2,
    column=1
)

root_entry = tk.Entry(root)
root_entry.grid(
    row=2,
    column=2,
)

root2_label = tk.Label(
    root,
    text='Amount £',
    font=('Arial',15)
)
root2_label.grid(
    row=3,
    column=1
)

root2_entry = tk.Entry(root)
root2_entry.grid(
    row=3,
    column=2,
)

root_button = tk.Button(
    root,
    text='Convert',
    width=20,
    command=checkcurrency
)
root_button.grid(
    row=4,
    column=1,
    columnspan=2
)

exit_button = tk.Button(
    root,
    text='Exit',
    width=20,
    command=sys.exit
)
exit_button.grid(
    row=5,
    column=1,
    columnspan=2
)

root.mainloop()