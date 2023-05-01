from helper.trend import calculate_trend_slope
import streamlit as st
import yfinance as yf


st.markdown("# Stock Trend for LQ45")

# define stock code
stock = ['ACES', 'BBRI', 'EXCL', 'ITMG', 'SMGR', 'ADRO', 'BBTN', 'GOTO', 'JPFA', 'SRTG', 'AKRA', 'BMRI', 'HRUM', 'KLBF', 'TBIG', 'AMRT', 'BRIS', 'ICBP', 'MDKA', 'TINS', 'ANTM', 'BRPT', 'INCO', 'MEDC', 'TLKM', 'ARTO', 'BUKA', 'INDF', 'PGAS', 'TOWR', 'ASII', 'CPIN', 'INDY', 'PTBA', 'TPIA', 'BBCA', 'EMTK', 'INKP', 'SCMA', 'UNTR', 'BBNI', 'ESSA', 'INTP', 'SIDO', 'UNVR']

# result
result = []

for s in stock:

    # get stock data
    ticker = yf.Ticker(f'{s}.JK')
    data = ticker.history(period="7d", interval="15m").iloc[-20:, :]

    x1 = 0
    x2 = len(data) - 1
    y1 = data['Close'][x1]
    y2 = data['Close'][x2]

    # predict slope
    preds = calculate_trend_slope(x1, y1, x2, y2)

    # append results
    result.append({
        "Code": s,
        "Trend Score": preds,
        "Trend Type": "Bulish" if preds > 0 else "Bearish"
    })

st.table(sorted(result, key=lambda x: x["Trend Score"]))