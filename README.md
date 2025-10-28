# Stock Price Information App - Submission

## Quick Start (Recommended)

Simply run the provided script:
```bash
./run.sh
```

This will automatically fetch and display AAPL (Apple) stock information. The script will:
- Check Python installation
- Set up virtual environment if needed
- Install dependencies
- Fetch and display stock information
- Exit automatically

To fetch a different stock symbol:
```bash
./run.sh MSFT    # Microsoft
./run.sh GOOGL   # Google
./run.sh TSLA    # Tesla
```

## Manual Installation

1. **Ensure Python is Installed**  
   - Verify you have Python 3.9 or later installed:
     ```bash
     python3 --version
     ```

2. **Set Up Virtual Environment and Install Dependencies**  
   - Create a virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     ```bash
     source venv/bin/activate
     ```
   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Script**  
   - Execute the Python file using:
     ```bash
     python stockPrice.py
     ```

4. **Use the Program**  
   - When prompted, enter a stock symbol (e.g., `AAPL`, `ADBE`).  
   - The program will display the current stock information in the format:
     ```
     Mon Oct 27 17:33:41 PDT 2025
     Apple Inc. (AAPL)
     268.81 +5.99 (+2.28%)
     ```
   - Type `q` and press Enter to quit.

---