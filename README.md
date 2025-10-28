# Steps to Run the Command-Line Stock Info App

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
     pip install yfinance
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
     Mon Oct 10 17:23:48 PDT 2016
     Adobe Systems Incorporated (ADBE)
     109.24 +0.60 (+0.55%)
     ```
   - Type `q` and press Enter to quit.

---