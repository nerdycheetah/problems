def max_profit_finder(stock_prices):
  min_price = stock_prices[0]
  max_profit = float('-inf')
  for i in range(1, len(stock_prices)):
      current_price = stock_prices[i]
      current_profit = current_price - min_price
      max_profit = max(current_profit, max_profit)
      min_price = min(current_price, min_price)
  return max_profit


test_input = [100, 200, 50, 250, 700]
result = max_profit_finder(test_input)
print(result)
