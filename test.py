from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = '92907336c3916cd9ae7fc0b968ee3a7e'
BASE_URL = 'http://api.currencylayer.com/live'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    try:
        from_currency = request.form['from_currency'].upper()
        to_currency = request.form['to_currency'].upper()
        amount = float(request.form['amount'])
        currencies = f'{from_currency},{to_currency}'
        params = {
            'access_key': API_KEY,
            'currencies': currencies,
            'format': 1
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if not data['success']:
            return f"Error: {data['error']['info']}"
        rates = data['quotes']
        from_rate = 1 if from_currency == 'USD' else rates.get(
            f'USD{from_currency}', None)
        to_rate = 1 if to_currency == 'USD' else rates.get(
            f'USD{to_currency}', None)
        if not from_rate or not to_rate:
            return f"Error: Invalid currency code or rates not found."
        converted_amount = (amount / from_rate) * to_rate
        return render_template('result.html', amount=amount, from_currency=from_currency, to_currency=to_currency, result=converted_amount)
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to fetch conversion rates. {str(e)}"
    except ValueError:
        return "Error: Invalid amount entered."


if __name__ == '__main__':
    app.run(debug=True)
