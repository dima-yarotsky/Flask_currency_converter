from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    amount = float(request.form['amount'])
    c = CurrencyRates()
    result = c.convert(from_currency, to_currency, amount)
    rate = c.get_rate(from_currency, to_currency)
    return render_template('result.html', result=result, from_currency=from_currency, to_currency=to_currency, amount=amount, CurrencyRates=rate)


if __name__ == '__main__':
    app.run(debug=True)
