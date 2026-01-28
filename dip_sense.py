"""
AUTO BUY / WAIT SCANNER
Runs auto-support + news + volume logic
for 20 diversified Indian stocks
"""

import yfinance as yf
import numpy as np
from newsapi import NewsApiClient
from datetime import datetime, timedelta
from config import (
    STOCKS,
    NEWS_API_KEY,
    SUPPORT_WINDOW,
    VOLUME_MULTIPLIER,
    BUY_THRESHOLD,
    BUY_SMALL_THRESHOLD,
    NEWS_LOOKBACK_DAYS,
    NEGATIVE_KEYWORDS,
)


# -------- AUTO SUPPORT --------
def auto_support(df, window=None):
    if window is None:
        window = SUPPORT_WINDOW
    return df["Low"].tail(window).mean()


# -------- BAD NEWS CHECK --------
def has_long_term_bad_news(stock):
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    from_date = (datetime.now() - timedelta(days=NEWS_LOOKBACK_DAYS)).strftime(
        "%Y-%m-%d"
    )

    articles = newsapi.get_everything(
        q=stock.split(".")[0],
        sources="reuters,bloomberg,wsj",
        from_param=from_date,
        language="en",
        page_size=5,
    )

    for a in articles["articles"]:
        text = (a["title"] + str(a["description"])).lower()
        if any(w in text for w in NEGATIVE_KEYWORDS):
            return True
    return False


# -------- DECISION --------
def decide(df, stock):
    today = df.iloc[-1]
    yesterday = df.iloc[-2]

    # Extract scalar values using .item() for Series
    close_today = (
        today["Close"].item() if hasattr(today["Close"], "item") else today["Close"]
    )
    close_yesterday = (
        yesterday["Close"].item()
        if hasattr(yesterday["Close"], "item")
        else yesterday["Close"]
    )
    volume_today = (
        today["Volume"].item() if hasattr(today["Volume"], "item") else today["Volume"]
    )

    change_pct = ((close_today - close_yesterday) / close_yesterday) * 100

    support = auto_support(df)
    avg_vol = df["Volume"].tail(20).mean()
    high_vol_result = volume_today > VOLUME_MULTIPLIER * avg_vol
    high_vol = (
        high_vol_result.item() if hasattr(high_vol_result, "item") else high_vol_result
    )

    support_holds_result = close_today >= support
    support_holds = (
        support_holds_result.item()
        if hasattr(support_holds_result, "item")
        else support_holds_result
    )

    if has_long_term_bad_news(stock):
        return "AVOID ❌"

    if not support_holds and high_vol:
        return "WAIT ⏸️"

    if change_pct <= BUY_THRESHOLD and support_holds:
        return "BUY ✅"

    if BUY_THRESHOLD < change_pct < BUY_SMALL_THRESHOLD and support_holds:
        return "BUY SMALL ⚠️"

    return "WAIT ⏸️"


# -------- RUN SCAN --------
print("\n" + "=" * 50)
print("📊 TECHNICAL ANALYSIS PARAMETERS")
print("=" * 50)
print(f"Support Window:       {SUPPORT_WINDOW} days")
print(f"Volume Multiplier:    {VOLUME_MULTIPLIER}x")
print(f"Buy Threshold:        {BUY_THRESHOLD}%")
print(f"Buy Small Threshold:  {BUY_SMALL_THRESHOLD}%")
print(f"News Lookback:        {NEWS_LOOKBACK_DAYS} days")
print(f"Total Stocks:         {len(STOCKS)}")
print("=" * 50)
print("\nSCAN RESULT\n" + "-" * 40)

for stock in STOCKS:
    try:
        df = yf.download(stock, period="6mo", interval="1d", progress=False)
        if len(df) < 25:
            continue

        action = decide(df, stock)

        # Extract scalar values for clean output
        close = df.iloc[-1]["Close"]
        close = close.item() if hasattr(close, "item") else close
        close = round(close, 2)

        support_val = auto_support(df)
        support_val = (
            support_val.item() if hasattr(support_val, "item") else support_val
        )
        support = round(support_val, 2)

        print(f"{stock:15} | Close: {close:8} | Support: {support:8} | {action}")

    except Exception as e:
        print(e)
        print(f"{stock} ERROR")
