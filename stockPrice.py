"""
Simple Command-Line Stock Info App using yfinance

Features:
- Prompts user for a stock symbol (e.g., AAPL, ADBE)
- Displays:
  * Current date/time
  * Company name
  * Stock price
  * Value change (+ / -)
  * Percentage change (+ / -)
- Handles errors for invalid symbols and network issues.

Run:
    python stockPrice.py

Or use the run script:
    ./run.sh
"""

import yfinance as yf
from datetime import datetime
from zoneinfo import ZoneInfo


def get_stock_info(symbol: str):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.get_info()

        # Company name
        name = info.get("longName", symbol)

        # Get recent price data
        hist = ticker.history(period="2d")
        if hist.empty:
            print(f"No data found for symbol: {symbol}")
            return

        # Current and previous close prices
        current_price = hist["Close"].iloc[-1]
        previous_close = hist["Close"].iloc[-2] if len(hist) > 1 else current_price

        # Calculate change and percentage change
        change = current_price - previous_close
        percent_change = (change / previous_close) * 100 if previous_close else 0

        # Format output
        now = datetime.now(ZoneInfo("America/Los_Angeles"))
        timestamp = now.strftime("%a %b %d %H:%M:%S %Z %Y")

        sign = "+" if change >= 0 else "-"

        print(f"\n{timestamp}")
        print(f"{name} ({symbol.upper()})")
        print(f"{current_price:.2f} {sign}{abs(change):.2f} ({sign}{abs(percent_change):.2f}%)\n")

    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")


def main():
    while True:
        symbol = input("Please enter a symbol (or 'q' to quit): ").strip()
        if symbol.lower() == 'q':
            break
        elif not symbol:
            continue
        get_stock_info(symbol)


if __name__ == "__main__":
    main()
