from flask import Flask, render_template, request
import requests
app = Flask(__name__)
API_KEY = 'KEY'
BASE_URL = 'http://api.currencylayer.com/live'
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['from_currency'].upper()
    to_currency = request.form['to_currency'].upper()
    amount = float(request.form['amount'])
    if from_currency == 'USD':
        from_rate = 1 
    else:
        params = {
            'access_key': API_KEY,
            'currencies': from_currency,
            'format': 1
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if not data['success']:
            return f"Error: {data['error']['info']}"
        from_rate = data['quotes'][f'USD{from_currency}']

    if to_currency == 'USD':
        to_rate = 1 
    else:
        params = {
            'access_key': API_KEY,
            'currencies': to_currency,
            'format': 1
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if not data['success']:
            return f"Error: {data['error']['info']}"
        to_rate = data['quotes'][f'USD{to_currency}']
    converted_amount = (amount / from_rate) * to_rate

    return render_template('result.html', amount=amount, from_currency=from_currency, to_currency=to_currency, result=converted_amount)
if __name__ == '__main__':
    app.run(debug=True)
