
def MeanReversionStrategy(prices): 
    days = 5 # 5 day moving average
    buy_or_sell = 0 # 0 meanas not holding, 1 means holding
    profit = 0.0 # the profit
    buy_price = 0.0 # price we're buying at

    for i in range(days, len(prices)): #looping through our prices
        five_days = prices[i - days : i] # taking our five days
        avg = sum(five_days) / days # average of last 5 days
        price = prices[i] # current price

        if buy_or_sell == 0 and price < avg * 0.98: # us buying because its below the 2% threshold
            print(f"Buy at: {price}, the average was: {avg}")
            buy_price = price
            buy_or_sell = 1

        elif buy_or_sell == 1 and price > avg * 1.02:
            print(f"Sell at {price:.2f}, the average was {avg:.2f}")
            trade_profit = price - buy_price
            profit += trade_profit
            buy_or_sell = 0
        else:
            pass  #don't buy or sell

    if buy_or_sell == 1: # if we're holding then this is us selling at the last price
        final_price = prices[-1]
        profit += final_price - buy_price

    first_buy = prices[days] # calculating our percent return
    percent_return = (profit / first_buy) * 100

    return profit, percent_return

def SimpleMovingAverageStrategy(prices):
    days = 5
    buy_or_sell = 0
    buy_price = 0.0
    profit = 0.0

    for i in range(days, len(prices)):
        five_days = prices[i - days : i]
        avg = sum(five_days) / days
        price = prices[i]

        if buy_or_sell == 0 and price > avg: # if the price is above average then buy
            print(f"Moving average, buy at: {price}, avg = {avg}")
            buy_price = price
            buy_or_sell = 1

        elif buy_or_sell == 1 and price < avg: # if the prie is below average then sell
            print(f"Moving average, sell at: {price}, avg = {avg}")
            profit += price - buy_price
            buy_or_sell = 0

    if buy_or_sell == 1: # if you're still holding
        profit += prices[-1] - buy_price

    first_buy = prices[days]
    percent_return = (profit / first_buy) * 100

    return profit, percent_return
 
def saveResults(results):
    import json
    with open("results.json", "w") as file:
        json.dump(results, file, indent=4)

tickers = ["AAPL", "GOOGL", "ADBE", "AMC", "AMD", "MSFT", "NVDA", "ORCL", "PECO", "SOFI"]

results = {}

for t in tickers:
    file = open(f"/workspaces/DATA_3500_trevor_wilkinson/Homework5/{t}.txt")
    lines = file.readlines()
    prices = [float(line.strip()) for line in lines]

    results[f"{t}_prices"] = prices # storing the price results

    mean_rev_profit, mean_rev_return = MeanReversionStrategy(prices) #running the mean reversion strategy
    results[f"{t}_mean_rev_profit"] = mean_rev_profit
    results[f"{t}_mean_rev_return"] = mean_rev_return

    sma_profit, sma_return = SimpleMovingAverageStrategy(prices) #running the SMA strategy
    results[f"{t}_sma_profit"] = sma_profit
    results[f"{t}_sma_return"] = sma_return

# save everything to JSON
saveResults(results)
        
