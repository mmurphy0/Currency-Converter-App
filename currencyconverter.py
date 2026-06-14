import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel

import requests

currency_codes = {
    'Euro': 'EUR',
    'United States Dollar': 'USD'
}

def convert_amount(conversion_amount, from_cur, to_cur):
    def reset():
        conversion_results_win.destroy()

    try:
        response = requests.get(
            f"https://api.frankfurter.app/latest?from={from_cur}&to={to_cur}"
        )
        response.raise_for_status()
    except requests.RequestException:
        messagebox.showerror('Error', 'Unable to retrieve exchange rates')
        return

    data = response.json()

    rate = data['rates'][to_cur]

    result = float(conversion_amount) * rate

    conversion_results_win = Toplevel()
    conversion_results_win.title('Currency Converter')
    conversion_results_win.geometry('+0+0')
    conversion_results_win.resizable(False,False)

    conversion_results_win_label = tk.Label(
        conversion_results_win,
        text=f'{conversion_amount} {from_cur} = {result} {to_cur}',
        font=('Arial',20,'bold')
    )
    conversion_results_win_label.pack()

    continue_button = tk.Button(
        conversion_results_win,
        text='Continue',
        font=('Arial'),
        command=reset
    )
    continue_button.pack()


def get_values(from_cur, to_cur):
    def set_conversion_amount(get_values_entry, from_cur, to_cur):

        conversion_amount = get_values_entry.get()
        try:
            amount = float(conversion_amount)
        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid number')
            return
        
        get_values_win.destroy()

        convert_amount(conversion_amount, from_cur, to_cur)

    get_values_win = Toplevel()
    get_values_win.title('Currency Converter')
    get_values_win.geometry('+0+0')
    get_values_win.resizable(False,False)

    get_values_label = tk.Label(
        get_values_win,
        text='Enter Amount',
        font=('Arial',20,'bold')
    )
    get_values_label.pack()

    get_values_entry = tk.Entry(
        get_values_win,
        width=20
    )
    get_values_entry.pack()

    continue_button = tk.Button(
        get_values_win,
        text='Continue',
        font=('Arial'),
        width=20,
        command=lambda: set_conversion_amount(get_values_entry, from_cur, to_cur)
    )
    continue_button.pack()

def choose_currency():
    def set_currencies(from_cur, to_cur):
        from_cur = from_cur
        to_cur = to_cur

        choose_currency_win.destroy()

        get_values(from_cur, to_cur)

    choose_currency_win = Toplevel()
    choose_currency_win.title('Currency Converter')
    choose_currency_win.geometry('+0+0')
    choose_currency_win.resizable(False,False)

    choose_currency_win_title = tk.Label(
        choose_currency_win,
        text='Please choose a currency',
        font=('Arial',20,'bold')
    )
    choose_currency_win_title.pack()

    GBP_EUR_Button = tk.Button(
        choose_currency_win,
        text='GBP 🏴󠁧󠁢󠁥󠁮󠁧󠁿 -> EUR 🇪🇺',
        font=('Arial'),
        width=20,
        command=lambda: set_currencies('GBP','EUR')
    )
    GBP_EUR_Button.pack()

    GBP_USD_Button = tk.Button(
        choose_currency_win,
        text='GBP 🏴󠁧󠁢󠁥󠁮󠁧󠁿 -> USD 🇺🇸',
        font=('Arial'),
        width=20,
        command=lambda: set_currencies('GBP','USD')
    )
    GBP_USD_Button.pack()

root = tk.Tk()
root.title('Currency Converter')
root.geometry('+0+0')
root.resizable(False,False)

root_title = tk.Label(
    root,
    text='Currency Converter',
    font=('Arial',20,'bold')
)
root_title.pack()

continue_button = tk.Button(
    root,
    text='Continue',
    font=('Arial'),
    width=20,
    command=choose_currency
)
continue_button.pack()

root.mainloop()