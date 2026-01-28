import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# News API Configuration
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Technical Analysis Parameters
SUPPORT_WINDOW = int(os.getenv("SUPPORT_WINDOW", 20))
VOLUME_MULTIPLIER = float(os.getenv("VOLUME_MULTIPLIER", 1.5))

# Price Drop Thresholds (in percentage)
BUY_THRESHOLD = float(os.getenv("BUY_THRESHOLD", -3))
BUY_SMALL_THRESHOLD = float(os.getenv("BUY_SMALL_THRESHOLD", -1))

# News Lookback Period (in days)
NEWS_LOOKBACK_DAYS = int(os.getenv("NEWS_LOOKBACK_DAYS", 3))

# News Sentiment - Negative Keywords
NEGATIVE_KEYWORDS = [
    "ban",
    "shutdown",
    "fraud",
    "collapse",
    "regulatory action",
    "permanent",
    "demand destruction",
]

# Stock List
STOCKS = [
    # Pharma
    "SUNPHARMA.NS",
    "DRREDDY.NS",
    "CIPLA.NS",
    "DIVISLAB.NS",
    "AUROPHARMA.NS",
    "LUPIN.NS",
    "GLENMARK.NS",
    "ALKEM.NS",
    "TORNTPHARM.NS",
    "BIOCON.NS",
    # Defence
    "HAL.NS",
    "BEL.NS",
    "BDL.NS",
    "MAZDOCK.NS",
    "COCHINSHIP.NS",
    "GRSE.NS",
    "DATAPATTNS.NS",
    "ZENTEC.NS",
    "ASTRAMICRO.NS",
    "DCXINDIA.NS",
    "PARAS.NS",
    # Electronics
    "DIXON.NS",
    "KAYNES.NS",
    "AMBER.NS",
    "PGEL.NS",
    "SYRMA.NS",
    "ELIN.NS",
    "AVALON.NS",
    "TEJASNET.NS",
    # Infra / Power
    "NTPC.NS",
    "POWERGRID.NS",
    "TATAPOWER.NS",
    "ABB.NS",
    "SIEMENS.NS",
    "CGPOWER.NS",
    # Auto
    "TATAMOTORS.NS",
    "MOTHERSON.NS",
    # IT
    "TCS.NS",
    "INFY.NS",
    "ROUTE.NS",
    # Banks
    "HDFCBANK.NS",
    "ICICIBANK.NS",
    # Penny Pharma
    "NATCOPHARM.NS",
    "FDC.NS",
    "NEULANDLAB.NS",
]
