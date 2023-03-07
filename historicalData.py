import yfinance as yf
import pandas as pd
import aiohttp
import asyncio
import csv
import requests




symbols = [
    {"name": "WBTC-USD", "address": "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599"},
    {"name": "WETH-USD", "address": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"},
    {"name": "LINK-USD", "address": "0x514910771AF9Ca656af840dff83E8264EcF986CA"},
    {"name": "MATIC-USD", "address": "0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0"},
    {"name": "UNI-USD", "address": "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984"},
    {"name": "USDC-USD", "address": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"},
    {"name": "USDT-USD", "address": "0xdAC17F958D2ee523a2206206994597C13D831ec7"},
    {"name": "DPI-USD", "address": "0x1494CA1F11D487c2bBe4543E90080AeBa4BA3C2b"},
    {"name": "stETH-USD", "address": "0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84"},
    {"name": "LDO-USD", "address": "0x5A98FcBEA516Cf06857215779Fd812CA3beF1B32"},
    {"name": "KNC-USD", "address": "0xdeFA4e8a7bcBA345F687a2f1456F5Edd9CE97202"},
    {"name": "1INCH-USD", "address": "0x111111111117dC0aa78b770fA6A738034120C302"},
    {"name": "AAVE-USD", "address": "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9"},
    {"name": "BAL-USD", "address": "0xba100000625a3754423978a60c9317c58a424e3D"},
    {"name": "GTC-USD", "address": "0xDe30da39c46104798bB5aA3fe8B9e0e1F348163F"},
    {"name": "COMP-USD", "address": "0xc00e94Cb662C3520282E6f5717214004A7f26888"},
    {"name": "MANA-USD", "address": "0x0F5D2fB29fb7d3CFeE444a200298f468908cC942"},
    {"name": "MKR-USD", "address": "0x9f8F72aA9304c8B593d555F12eF6589cC3A579A2"},
    {"name": "SAND-USD", "address": "0x3845badAde8e6dFF049820680d1F14bD3903a5d0"},
    {"name": "YFI-USD", "address": "0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e"},

]
payload={}
headers = {}

# symbols = json.load(symbols)


start_date = '2021-09-01'
end_date = '2023-03-06'
# all_data = pd.DataFrame()


async def uploadPerformanceV2(filename,address):
        url = f'https://us-central1-xwinstage.cloudfunctions.net/importTokenPriceHistory?contractAddress={address}&collection=performanceUSD'

        
        files=[('file',('file',open( fr"C:\Users\valia\Work\historicalData\{filename}",'rb' ),'application/octet-stream'))]

    

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        print(response.text)




def uploadPerformanceUSD(filename,address):
        url = f'https://us-central1-xwinstage.cloudfunctions.net/importTokenPriceHistory?contractAddress={address}&collection=performanceUSD'

        
        files=[('file',('file',open( fr"C:\Users\valia\Work\historicalData\{filename}",'rb' ),'application/octet-stream'))]

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        print(response.text)


def uploadPerformanceLocal(filename,address):
        url = f'https://us-central1-xwinstage.cloudfunctions.net/importTokenPriceHistory?contractAddress={address}&collection=performanceUSD'

        
        files=[('file',('file',open( fr"C:\Users\valia\Work\historicalData\{filename}",'rb' ),'application/octet-stream'))]

    
        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        print(response.text)



def getHistoricalData():
    for symbol in symbols:
        print(symbol["name"])
        ticker = yf.Ticker(symbol["name"])

        data = ticker.history(start=start_date, end=end_date)

        grouped = data.groupby('Date').mean()
        data = grouped.reset_index()

        # data.groupby(new_index, as_index=False).sum()
        data = data.rename(columns={'Close': 'value'})
        data = data.rename(columns={'Date': 'date'})
        data['date'] = pd.to_datetime(data['date']).dt.strftime('%m/%d/%Y')
        data['value'] = data['value'].round(5)

        data = data.loc[:, ['date', 'value']]

        data = data.dropna()

        print(data)

        data.to_csv(f'{symbol["name"]}-eth.csv', index=False)


def printToken():
    for symbol in symbols:
        print(f'{symbol["name"]}-eth.csv')


async def main():
    getHistoricalData()
    await upload_files()


async def upload_files():
        
        for symbol in symbols:
            token = symbol["name"]
            address = symbol["address"]
            filename = f'{token}-eth.csv' 
            # await uploadPerformanceUSD(filename,address)
            # await uploadPerformanceLocal(filename,address)
            # await uploadPerformanceUSD(filename,address)


            print(filename,token)




   
loop = asyncio.get_event_loop()
loop.run_until_complete(main())    






