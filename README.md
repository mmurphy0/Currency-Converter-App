# Currency Converter

## Description
A Python Tkinter App which lets people convert pounds (£) to any of the avaliable currencies as listed below:

- Euro

- United States Dollar

This project uses the Frankfurter API for live exchange rates:

https://api.frankfurter.app

No API key is required.

## Usage

- The welcome window is displayed with the app title and start button.

- The user is presented the currencies they can convert to from GBP.

- The user is prompted to enter in how much they would like to convert. You will be prompted to retry if you have not entered a valid number.

- The program gets the conversion rate from the Frankfurter API, if the API is unavaliable, The user is informed about the issue and returned to the welcome window.

- The amount in the original amount and currency is shown compared to the converted amount and currency.

- The User must click the continue button to be returned to the welcome window.

## Installation
git clone (repo)

cd (repo)

### Windows
python currencyconverter.py

### MacOS & Linux
python3 currencyconverter.py

## Tech Stack
- Python 3

- Tkinter (GUI)

- Requests (HTTP client)

- Frankfurter API (exchange rates)

## Future Updates
- More supported currencies will be added frequently
