from tradingview_ta import TA_Handler, Interval


tesla = TA_Handler(
    symbol="TSLA",
    screener="america", 
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_MINUTE
)


analysis = tesla.get_analysis()


summary = analysis.summary
print("Summary:", summary)


indicators = analysis.indicators
print("All Indicators:", indicators)


rsi = indicators['RSI']
print("RSI:", rsi)
