import requests


def get_btc(y):
    url = 'https://poloniex.com/public?command=returnTicker'
    response = requests.get(url).json()
    up = 'usdt' + '_' + str(y)
    price = response[up.upper()]['last']
    return str(price) + " USD"

