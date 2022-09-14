bitcoin_price = int(input('What is Bitcoin price today? '))

dollar_input = int(input('How much $ do you have? '))

result = dollar_input/bitcoin_price

buy_bitcoin = f"You can buy {result} BTC".format(result)

print(buy_bitcoin)