import yfinance as yf
import requests
from strategies import apply_all_strategies

# Telegram credentials
TELEGRAM_BOT_TOKEN = '___'
TELEGRAM_CHAT_ID = '___'

# List of stocks to analyze
STOCKS = ['GOOGL', 'MSFT', 'AMZN', 'TSLA', 'NVDA', 'PANW', 'TEM', 'VST', 'GME', 'INTC', 'TSM', 'AMAT']


# Function to fetch stock data
def fetch_stock_data(ticker, period='60d', interval='1d'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    return data


# Function to send notification via Telegram
def send_telegram_notification(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, json=payload)
    return response.status_code


# Function to analyze a single stock
def analyze_stock(ticker):
    data = fetch_stock_data(ticker)
    strategies = apply_all_strategies(data)

    # Count BUY and SELL signals
    buy_count = list(strategies.values()).count("BUY")
    sell_count = list(strategies.values()).count("SELL")

    # Make final decision
    if buy_count > sell_count:
        final_decision = "BUY"
    elif sell_count > buy_count:
        final_decision = "SELL"
    else:
        final_decision = "HOLD"

    # Prepare message
    message = f"Stock Alert: {ticker}\n\nFinal Decision: {final_decision}"
    for strategy, decision in strategies.items():
        message += f"- {strategy}: {decision}\n"
    return message


# Main function
def main():
    for ticker in STOCKS:
        try:
            message = analyze_stock(ticker)
            print(message)
            send_telegram_notification(message)
        except Exception as e:
            print(f"Error analyzing {ticker}: {e}")


if __name__ == "__main__":
    main()