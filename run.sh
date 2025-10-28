#!/bin/bash
# Run script for Stock Price Information App
# Usage: ./run.sh [STOCK_SYMBOL]
# Example: ./run.sh AAPL
# Default: Runs with AAPL if no symbol provided

# Get stock symbol from argument, default to AAPL
SYMBOL="${1:-AAPL}"

echo "Running Stock Price Information App with symbol: $SYMBOL"
echo "========================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed. Please install Python 3.9 or later."
    exit 1
fi

# Check Python version (require 3.9+ for zoneinfo)
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Python version: $PYTHON_VERSION"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
else
    echo "Virtual environment not found. Creating one..."
    python3 -m venv venv
    source venv/bin/activate
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

# Run the stock price application with the symbol
echo ""
echo "Fetching stock information for $SYMBOL..."
echo "============================================"
echo -e "$SYMBOL\nq" | python3 stockPrice.py

