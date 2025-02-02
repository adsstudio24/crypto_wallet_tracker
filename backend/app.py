import requests
from flask import Flask, jsonify

app = Flask(__name__)

API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

@app.route('/wallet/<wallet_address>')
def get_balance(wallet_address):
    # У реальному застосунку сюди треба інтегрувати API блокчейн-гаманця
    response = requests.get(API_URL).json()
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
