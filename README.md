# 📈 Indian Stock Market Auto Scanner - BUY/WAIT Signal Generator

> **Automated Stock Analysis Tool** for Indian Stock Market (NSE) - Smart Buy/Sell Signals with Technical Analysis, News Sentiment & Volume Detection

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![yfinance](https://img.shields.io/badge/yfinance-Latest-green.svg)](https://pypi.org/project/yfinance/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 Overview

**Indian Stock Market Auto Scanner** is a Python-based automated stock analysis tool that helps investors make data-driven decisions in the Indian stock market. This scanner analyzes **50+ stocks** across multiple sectors including Pharma, Defence, Electronics, Infrastructure, IT, Banking, and Auto, providing real-time **BUY**, **WAIT**, or **AVOID** signals based on:

- ✅ **Technical Analysis** - Automatic support level detection
- 📰 **News Sentiment Analysis** - Real-time negative news filtering
- 📊 **Volume Analysis** - Unusual trading volume detection
- 💹 **Price Action** - Percentage change tracking

Perfect for day traders, swing traders, and long-term investors looking for **automated stock screening** and **algorithmic trading signals** in NSE (National Stock Exchange of India).

## 🎯 Key Features

### Automated Trading Signals

- **BUY ✅** - Strong buy signal when price drops ≥3% and support holds
- **BUY SMALL ⚠️** - Cautious buy signal for 1-3% drops with support
- **WAIT ⏸️** - Hold position when conditions aren't favorable
- **AVOID ❌** - Skip stocks with long-term negative news

### Multi-Sector Coverage (50+ Stocks)

> **⚠️ IMPORTANT DISCLAIMER**: The stocks listed below are **EXAMPLES ONLY** for demonstration purposes. They are **NOT recommendations, suggestions, or investment advice**. These are sample stocks used to showcase the scanner's functionality across different sectors.

- 💊 **Pharma Stocks**: SunPharma, Dr Reddy's, Cipla, Divis Lab, Biocon, and more
- 🛡️ **Defence Stocks**: HAL, BEL, BDL, Mazagon Dock, Cochin Shipyard
- 🔌 **Electronics**: Dixon Technologies, Kaynes Technology, Amber Enterprises
- ⚡ **Power & Infrastructure**: NTPC, PowerGrid, Tata Power, ABB, Siemens
- 🚗 **Automobile**: Tata Motors, Motherson Sumi
- 💻 **IT Sector**: TCS, Infosys, Route Mobile
- 🏦 **Banking**: HDFC Bank, ICICI Bank
- 💊 **Penny Pharma**: Natco Pharma, FDC, Neuland Laboratories

### Technical Indicators

- **Auto Support Calculation** - 20-day rolling average of lows
- **Volume Spike Detection** - Identifies 1.5x average volume
- **Price Change Analysis** - Percentage-based decision making
- **6-Month Historical Data** - Reliable trend analysis

### News Integration

- Real-time news sentiment from **Reuters, Bloomberg, WSJ**
- Filters stocks with negative keywords (ban, fraud, shutdown, etc.)
- 3-day lookback period for recent developments

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- News API Key (free from [newsapi.org](https://newsapi.org/))

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/arunkumar1997/DipSense.git
cd DipSense
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages:

- `yfinance` - Yahoo Finance data
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `newsapi-python` - News API client
- `python-dotenv` - Environment variables

### 3. Configure Environment Variables

```bash
cp env.example .env
```

Edit `.env` file and configure all parameters:

```env
# News API Configuration
NEWS_API_KEY="your_news_api_key_here"

# Technical Analysis Parameters
SUPPORT_WINDOW=20
VOLUME_MULTIPLIER=1.5

# Price Drop Thresholds (in percentage)
BUY_THRESHOLD=-3
BUY_SMALL_THRESHOLD=-1

# News Lookback Period (in days)
NEWS_LOOKBACK_DAYS=3
```

Get your free API key from [NewsAPI.org](https://newsapi.org/register)

## 💻 Usage

### Run Python Script

```bash
python dip_sense.py
```

### Run Jupyter Notebook

```bash
jupyter notebook stocks.ipynb
```

### Sample Output

```
==================================================
📊 TECHNICAL ANALYSIS PARAMETERS
==================================================
Support Window:       20 days
Volume Multiplier:    1.5x
Buy Threshold:        -3%
Buy Small Threshold:  -1%
News Lookback:        3 days
Total Stocks:         50
==================================================

SCAN RESULT
----------------------------------------
SUNPHARMA.NS    | Close:  1234.50 | Support:  1200.00 | BUY ✅
DRREDDY.NS      | Close:  5600.25 | Support:  5500.00 | WAIT ⏸️
HAL.NS          | Close:  4200.00 | Support:  4100.00 | BUY SMALL ⚠️
DIXON.NS        | Close: 12500.00 | Support: 12000.00 | AVOID ❌
```

## 🧮 How It Works

### Decision Logic

1. **Data Collection**: Downloads 6 months of historical data from Yahoo Finance
2. **Support Calculation**: Computes 20-day average of low prices
3. **News Check**: Queries latest news for negative sentiment
4. **Volume Analysis**: Detects unusual trading volume
5. **Signal Generation**: Applies decision rules:

```python
if negative_news:
    return "AVOID ❌"
if not support_holds and high_volume:
    return "WAIT ⏸️"
if price_drop >= 3% and support_holds:
    return "BUY ✅"
if 1% < price_drop < 3% and support_holds:
    return "BUY SMALL ⚠️"
else:
    return "WAIT ⏸️"
```

## 📊 Sectors Analyzed

> **⚠️ DISCLAIMER**: All stock names listed below are **examples for demonstration purposes only**. They do **NOT** constitute investment recommendations or advice.

| Sector                 | Number of Stocks | Examples                     |
| ---------------------- | ---------------- | ---------------------------- |
| Pharmaceuticals        | 12               | SunPharma, Dr Reddy's, Cipla |
| Defence                | 9                | HAL, BEL, Mazagon Dock       |
| Electronics            | 8                | Dixon, Kaynes, Amber         |
| Infrastructure & Power | 6                | NTPC, PowerGrid, ABB         |
| Automobile             | 2                | Tata Motors, Motherson       |
| IT Services            | 3                | TCS, Infosys, Route Mobile   |
| Banking                | 2                | HDFC Bank, ICICI Bank        |
| Penny Pharma           | 3                | Natco Pharma, FDC, Neuland   |

## 🛠️ Customization

### Add Your Own Stocks

**IMPORTANT**: Replace the example stocks in `config.py` with your own watchlist. The stocks provided are for demonstration only.

Edit the `STOCKS` list in `config.py`:

```python
STOCKS = [
    "RELIANCE.NS",
    "TATASTEEL.NS",
    # Add more NSE stocks with .NS suffix
]
```

### Adjust Parameters

All scanner parameters can be customized:

**Environment Variables (.env):**

- **SUPPORT_WINDOW**: Change support calculation window (default: 20 days)
- **VOLUME_MULTIPLIER**: Modify volume spike sensitivity (default: 1.5x)
- **BUY_THRESHOLD**: Strong buy signal threshold (default: -3%)
- **BUY_SMALL_THRESHOLD**: Cautious buy signal threshold (default: -1%)
- **NEWS_LOOKBACK_DAYS**: News search period (default: 3 days)

**Direct Configuration (config.py):**

- **NEGATIVE_KEYWORDS**: Customize negative news keywords list for sentiment filtering

Example `.env` configuration:

```env
SUPPORT_WINDOW=30
VOLUME_MULTIPLIER=2.0
BUY_THRESHOLD=-5
BUY_SMALL_THRESHOLD=-2
NEWS_LOOKBACK_DAYS=7
```

Example `config.py` customization:

```python
NEGATIVE_KEYWORDS = [
    "ban",
    "shutdown",
    "fraud",
    "scandal",
    "investigation",
    # Add your own keywords
]
```

## 📈 Best Practices

1. **Run Daily**: Execute scanner before market opens for fresh signals
2. **Cross-Verify**: Always verify signals with your own research
3. **Risk Management**: Use stop-loss orders with buy signals
4. **Position Sizing**: Start with "BUY SMALL" signals before full positions
5. **News Awareness**: Read the actual news articles flagged by scanner

## ⚠️ Disclaimer

**This tool is for educational and informational purposes only.**

- **NOT financial advice or investment recommendation**
- **ALL stocks listed in this project are examples only** - they are for demonstration purposes to show how the scanner works across different sectors
- The inclusion of any stock ticker does NOT constitute a recommendation to buy, sell, or hold
- Past performance doesn't guarantee future results
- Always do your own research (DYOR)
- Consult with certified financial advisors before making investment decisions
- Invest only risk capital - markets can be volatile
- Author is not responsible for any trading losses or investment decisions
- **Use this tool at your own risk** - replace the example stocks with your own watchlist

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects & Resources

- [yfinance Documentation](https://pypi.org/project/yfinance/)
- [NewsAPI Documentation](https://newsapi.org/docs)
- [NSE India](https://www.nseindia.com/)
- [Yahoo Finance](https://finance.yahoo.com/)

## 📧 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/arunkumar1997/DipSense/issues)
- **Discussions**: [GitHub Discussions](https://github.com/arunkumar1997/DipSense/discussions)

## 🌟 Star History

If this project helped you, please consider giving it a ⭐ on GitHub!

## 📱 Keywords

Indian stock market, NSE stocks, automated trading, stock scanner, technical analysis, Python trading bot, yfinance, stock alerts, buy sell signals, algorithmic trading, stock screener, NSE India, pharma stocks, defence stocks, volume analysis, support resistance, news sentiment analysis, swing trading, day trading, investment tools, stock market analysis, trading automation, financial analysis, market scanner, stock signals, Python finance

---

**Made with ❤️ for Indian Stock Market Traders**

_Last Updated: January 2026_
