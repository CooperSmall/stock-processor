from json import load
import os
import requests

REQUEST_ADDRESS = 'https://www.alphavantage.co/query?'
PATH = os.getcwd()


def main():
    stocks = batch_request(['ATVI', 'PYPL', 'OKTA'])
    print(stocks['Stock Batch Quotes'])


def batch_request(symbols, datatype=None):

    address = REQUEST_ADDRESS

    address += ('function=BATCH_QUOTES_US&')
    address += ('symbols=')

    for i, symbol in enumerate(symbols):
        address += (symbol)
        if i != len(symbols) - 1:
            address += (',')
        else:
            address += ('&')

    api_key = None

    try:
        with open(f'{PATH}/creds/api_key.json', 'r') as f:
            creds = load(f)
        api_key = creds['api_key']

    except:
        print('Missing API Key!!!')
        return None

    if api_key:
        address += (f'apikey={api_key}')

    if datatype:
        address += (f'&datatype={datatype}')

    json = connect(address)
    return json


def connect(address):

    try:
        request = requests.get(address)

        if request.status_code == 200 or request.status_code == 201:
            json = request.json()
            return json

        else:
            print('Error Fetching Request!!!')

    except:
        print('Invalid Address!!!')

    return None


main()
