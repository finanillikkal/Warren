# Warren

This Python script analyzes stock data using multiple trading strategies and sends notifications via Telegram. It can be scheduled to run whenever you want.

---

## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Setup](#setup)
4. [Configuration](#configuration)
5. [Running the Script](#running-the-script)
6. [Scheduling the Script](#scheduling-the-script)
7. [Contributing](#contributing)

---

## Features
- Fetches stock data using the `yfinance` library.
- Applies multiple trading strategies:
  - Moving Average Crossover
  - RSI (Relative Strength Index)
  - Bollinger Bands
  - MACD (Moving Average Convergence Divergence)
  - VWAP (Volume Weighted Average Price)
  - Stochastic Oscillator
  - OBV (On-Balance Volume)
  - ATR (Average True Range)
  - Parabolic SAR
  - Ichimoku Cloud
  - Fibonacci Retracement
  - Volume Profile
  - ADX (Average Directional Index)
  - MFI (Money Flow Index)
  - ROC (Rate of Change)
  - Williams %R
  - CMF (Chaikin Money Flow)
- Sends notifications via Telegram.
- Can be scheduled to run daily or whatever basis you need.

---

## Prerequisites
Before running the script, ensure you have the following:
- Python 3.7 or higher installed.
- A Telegram bot token and chat ID.
- Required Python libraries installed.

---

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/minecraftmuselk/warren.git
cd warren
```
### 1. Install Required Libraries  
Use the following command to install the necessary Python libraries:

```bash
pip install -r requirements.txt
```

---

## Configuration

### 1. Telegram Credentials  
- Create a Telegram bot using **BotFather**.
- Retrieve your **bot token** and **chat ID**.
- Open the `main.py` file and replace the placeholders:

```python
TELEGRAM_BOT_TOKEN = 'your_bot_token'
TELEGRAM_CHAT_ID = 'your_chat_id'
```

### 2. Stock Symbols  
By default, the script analyzes all available stocks. To analyze specific stocks, update the `STOCKS` list in `main.py`:

```python
STOCKS = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']  # Add desired stocks here
```

---

## Running the Script  

### 1. Run Manually  
Execute the following command:

```bash
python main.py
```

### 2. Check Notifications  
You should receive Telegram notifications with stock analysis results.

---

## Scheduling the Script  

### 1. Windows: Using Task Scheduler  
1. Open **Task Scheduler**.  
2. Click **Create Basic Task**.  
3. Name the task (e.g., "Run Stock Script") and click **Next**.  
4. Select **Daily** and click **Next**.  
5. Set the start time to **Your time** and click **Next**.  
6. Select **Start a Program** and click **Next**.  
7. In the **Program/script** field, enter the path to your Python executable (e.g., `C:\Python39\python.exe`).  
8. In the **Add arguments** field, enter the path to your script (e.g., `C:\path\to\your\main.py`).  
9. In the **Start in** field, enter the directory containing your script (e.g., `C:\path\to\your`).  
10. Click **Finish**.  

### 2. macOS/Linux: Using cron  
1. Open **Terminal**.  
2. Edit the crontab file:

```bash
crontab -e
```

3. Add the following line to schedule the script to run at **9:30 AM daily**:

```bash
30 9 * * * /usr/bin/python3 /path/to/your/main.py >> /path/to/your/log.txt 2>&1
```

4. Save and exit the editor.

---

## Contributing  
Contributions are welcome! Follow these steps to contribute:

1. **Fork** the repository.  
2. Create a new branch:

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. Commit your changes:

   ```bash
   git commit -m 'Add some feature'
   ```

4. Push to the branch:

   ```bash
   git push origin feature/YourFeatureName
   ```

5. Open a **pull request**.

---

## Support  
If you encounter any issues or have questions, please **open an issue** on GitHub or contact me: finani007@gmail.com.
