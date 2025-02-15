import yfinance as yf
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Load environment variables from .env file (for API keys)
load_dotenv()

COINGECKO_API = "https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"

ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY") # get it from personal .env file
ALPHA_VANTAGE_URL = "https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={symbol}&time_from={time_from}&time_to={time_to}&apikey=" + ALPHA_VANTAGE_KEY

def get_stock_price(symbol):
    """Fetches real-time stock price."""
    try:
        stock = yf.Ticker(symbol)
        history = stock.history(period="1d")
        if history.empty:
            return f"Error: No stock data available for {symbol}."
        price = history.iloc[-1]['Close']
        return f"{symbol.upper()} Price: ${price:.2f}"
    except Exception as e:
        return f"Error fetching {symbol}: {e}"

def get_crypto_price(crypto_id):
    """Fetches real-time crypto price."""
    try:
        response = requests.get(COINGECKO_API.format(ids=crypto_id))
        data = response.json()
        if crypto_id not in data:
            return f"Error: Invalid cryptocurrency ID '{crypto_id}'."
        price = data[crypto_id]['usd']
        return f"{crypto_id.capitalize()} Price: ${price:.2f}"
    except Exception as e:
        return f"Error fetching {crypto_id}: {e}"

def get_news(symbol):
    """Fetches latest stock news headlines from Alpha Vantage."""
    try:
        time_from = (datetime.now() - timedelta(days=7)).strftime('%Y%m%dT%H%M')
        time_to = datetime.now().strftime('%Y%m%dT%H%M')
        response = requests.get(ALPHA_VANTAGE_URL.format(symbol=symbol, time_from=time_from, time_to=time_to))
        data = response.json()

        # Debugging: Print the raw response data
        print("API Response:", data)

        if "feed" not in data:
            return [(f"Error fetching news: {data.get('Note', 'Unknown error')}", "")]

        articles = data["feed"]
        headlines = [(article["title"], article["url"]) for article in articles[:3]]
        return headlines if headlines else [("No recent news found.", "")]
    except Exception as e:
        return [(f"Error fetching news: {e}", "")]

def get_historical_data(symbol, period="1mo"):
    """Fetches historical data for a given stock symbol."""
    try:
        stock = yf.Ticker(symbol)
        history = stock.history(period=period)
        if history.empty:
            return f"Error: No historical data available for {symbol}."
        return history
    except Exception as e:
        return f"Error fetching historical data for {symbol}: {e}"

def get_moving_average(symbol, window=20):
    """Calculates the moving average for a given stock symbol."""
    try:
        stock = yf.Ticker(symbol)
        history = stock.history(period="1mo")
        if history.empty:
            return f"Error: No historical data available for {symbol}."
        moving_average = history['Close'].rolling(window=window).mean().iloc[-1]
        return f"{symbol.upper()} {window}-Day Moving Average: ${moving_average:.2f}"
    except Exception as e:
        return f"Error calculating moving average for {symbol}: {e}"

def display_help():
    """Displays the help menu with available commands."""
    help_text = """
Available commands:
1. stock <symbol> - Fetches real-time stock price.
   Example: stock AAPL

2. crypto <id> - Fetches real-time cryptocurrency price.
   Example: crypto bitcoin

3. news <symbol> - Fetches the latest stock news headlines for the specified symbol.
   Example: news AAPL

4. history <symbol> [period] - Fetches historical data for the specified symbol.
   Example: history AAPL 1mo

5. ma <symbol> [window] - Calculates the moving average for the specified symbol.
   Example: ma AAPL 20

6. exit - Exits the program.
   Example: exit

7. help - Displays this help menu.
   Example: help
"""
    return help_text

def main():
    while True:
        command = input("StockBot -> ").strip()
        
        if command.startswith("stock"):
            symbol = command.split()[1].upper()
            print(get_stock_price(symbol))
        
        elif command.startswith("crypto"):
            crypto_id = command.split()[1].lower()
            print(get_crypto_price(crypto_id))
        
        elif command.startswith("news"):
            symbol = command.split()[1].upper()
            print(f"News for {symbol}:")
            for headline, url in get_news(symbol):
                print(f"- {headline} ({url})")
            print()
        
        elif command.startswith("history"):
            symbol = command.split()[1].upper()
            period = command.split()[2] if len(command.split()) > 2 else "1mo"
            print(get_historical_data(symbol, period))

        elif command.startswith("ma"):
            symbol = command.split()[1].upper()
            window = int(command.split()[2]) if len(command.split()) > 2 else 20
            print(get_moving_average(symbol, window))

        elif command == "help":
            print(display_help())

        elif command == "":
            continue

        elif command == "exit":
            break
        
        else:
            print(f"Invalid command: \"{command}\", Please type 'help' to see available commands.")

if __name__ == "__main__":
    main()