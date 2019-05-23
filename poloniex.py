import requests


def get_btc(y):
    url = 'https://poloniex.com/public?command=returnTicker'
    response = requests.get(url).json()
    up = 'usdt' + '_' + str(y)
    price = response[up.upper()]['last']
    return str(price) + " USD"
'''
{
      "-350806052 399585957": {
            "id": 399585957,
            "first_name": "Eugene",
            "last_name": "Inlakesh",
            "username": null,
            "score": 1
      },
      "409068251 409068251": {
            "id": 409068251,
            "first_name": "Костя",
            "last_name": "Яременко",
            "username": "H1Username",
            "score": 0
      },
      "399585957 399585957": {
            "id": 399585957,
            "first_name": "Eugene",
            "last_name": "Inlakesh",
            "username": null,
            "score": 0
      },
      "-350806052 232144066": {
            "id": 232144066,
            "first_name": "Vlad",
            "last_name": "S",
            "username": "v_shmyhlo",
            "score": 2
      },
      "-350806052 415630721": {
            "id": 415630721,
            "first_name": "Alenka",
            "last_name": "Biduha",
            "username": null,
            "score": 3
      },
      "-350806052 409068251": {
            "id": 409068251,
            "first_name": "Костя",
            "last_name": "Яременко",
            "username": "H1Username",
            "score": 12
      }
}
'''