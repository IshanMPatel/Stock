# Stock & Crypto Watcher

This script allows you to fetch real-time stock and cryptocurrency prices and retrieve the latest news headlines for specific assets.

## Features
- Fetch stock prices using `yfinance`.
- Fetch crypto prices using the CoinGecko API.
- Retrieve the latest stock news headlines using the Alpha Vantage API.

## Installation

Ensure you have Python installed (Python 3.x recommended).

1. Install dependencies:
   ```sh
   pip install yfinance requests
   ```
2. Get your Alpha Vantage API key by signing up [here](https://www.alphavantage.co/support/#api-key):
Sign up at Alpha Vantage to get your free API key. After signing up, you can find your API key in the "My Account" section.

3. Create a `.env` file in the project directory and add your API key:
    ```sh
    ALPHA_VANTAGE_KEY=your_alpha_vantage_api_key
    ```

4. Run the script:
   ```sh
   python main.py
   ```

## Usage

### Commands:
- `stock <symbol>` → Fetches real-time stock price.
    - Example: `stock AAPL`
- `crypto <id>` → Fetches real-time cryptocurrency price.
    - Example: `crypto bitcoin`
- `news <symbol>` → Fetches the latest stock news headlines for the specified symbol.
    - Example: `news AAPL`
- `exit` → Exits the program.
    - Example: `exit`
- `help` → Displays the help menu with available commands.
    - Example: `help`

### Example Session

```sh
StockBot -> stock AAPL
AAPL Price: $150.00

StockBot -> crypto bitcoin
Bitcoin Price: $45000.00

StockBot -> news AAPL
News for AAPL:
- Softbank-Backed Arm Holdings 155% Post-IPO Surge Bolstered by AI Growth and Smartphone Integration (https://www.benzinga.com/media/25/02/43676475/softbank-backed-arm-holdings-155-post-ipo-surge-bolstered-by-ai-growth-and-smartphone-integration)
- Decoding Apple's Options Activity: What's the Big Picture? (https://www.benzinga.com/insights/options/25/02/43671869/decoding-apples-options-activity-whats-the-big-picture)
- Why The MAGS ETF Has Remained Flat Year-to-Date Despite Some Strong Performers (https://www.benzinga.com/insights/options/25/02/43671869/why-the-mags-etf-has-remained-flat-year-to-date-despite-some-strong-performers)

StockBot -> exit
```


## Troubleshooting

### `ModuleNotFoundError: No module named 'yfinance'`
If you installed `yfinance` but still get an error:
- Ensure you are using the correct Python interpreter in VS Code:
  - Press **Ctrl + Shift + P** → Select **Python: Select Interpreter**.
- Try reinstalling `yfinance`:
  ```sh
  pip install --upgrade yfinance
  ```
- Restart VS Code after installing dependencies.

## Notes
- Stock prices are fetched via yfinance.
- Crypto prices are fetched via CoinGecko.
- News updates are retrieved from Alpha Vantage.
- To avoid API spam, the script adds a short delay when checking for news.

