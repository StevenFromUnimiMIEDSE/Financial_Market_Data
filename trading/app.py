from flask import Flask, render_template, jsonify
import yfinance as yf

app = Flask(__name__)

# Route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to get Forex rate
@app.route('/get_forex_rate')
def get_forex_rate():
    # Fetch Forex data (USD/EUR exchange rate)
    data = yf.download('USDEUR=X', period='1d')
    # Get the latest closing price
    latest_close_price = data['Close'].iloc[-1]
    # Return the latest closing price as the Forex rate
    return jsonify({'forex_rate': latest_close_price})

if __name__ == '__main__':
    app.run(debug=True)
