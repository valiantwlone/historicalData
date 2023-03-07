import yfinance as yf
import pandas as pd
import requests
import aiohttp
import asyncio


symbols = [
    {"name": "ADA-USD", "address": "0x3EE2200Efb3400fAbB9AacF31297cBdD1d435D47"},
    {"name": "ALICE-USD", "address": "0xAC51066d7bEC65Dc4589368da368b212745d63E8"},
    {"name": "ATOM-USD", "address": "0x0Eb3a705fc54725037CC9e008bDede697f62F335"},
    {"name": "AVAX-USD", "address": "0x1CE0c2827e2eF14D5C4f29a091d735A204794041"},
    {"name": "BTC-USD", "address": "0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c"},
    {"name": "CAKE-USD", "address": "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82"},
    {"name": "DOGE-USD", "address": "0xbA2aE424d960c26247Dd6c32edC70B295c744C43"},
    {"name": "DOT-USD", "address": "0x7083609fCE4d1d8Dc0C979AAb8c869Ea2C873402"},
    {"name": "ETH-USD", "address": "0x2170Ed0880ac9A755fd29B2688956BD959F933F8"},
    {"name": "FIL-USD", "address": "0x0D8Ce2A99Bb6e3B7Db580eD848240e4a0F9aE153"},
    {"name": "LINK-USD", "address": "0xF8A0BF9cF54Bb92F17374d9e9A321E6a111a51bD"},
    {"name": "LTC-USD", "address": "0x4338665CBB7B2485A8855A139b75D5e34AB0DB94"},
    {"name": "MATIC-USD", "address": "0xCC42724C6683B7E57334c4E856f4c9965ED682bD"},
    {"name": "TWT-USD", "address": "0x4B0F1812e5Df2A09796481Ff14017e6005508003"},
    {"name": "UNI-USD", "address": "0xBf5140A22578168FD562DCcF235E5D43A02ce9B1"},
    {"name": "USDC-USD", "address": "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d"},
    {"name": "USDT-USD", "address": "0x55d398326f99059fF775485246999027B3197955"},
    {"name": "WBNB-USD", "address": "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"},
    {"name": "XRP-USD", "address": "0x1D2F0da169ceB9fC7B3144628dB156f3F6c60dBE"},
    {"name": "XVS-USD", "address": "0xcF6BB5389c92Bdda8a3747Ddb454cB7a64626C63"},
    {"name": "XWIN-USD", "address": "0xd88ca08d8eec1E9E09562213Ae83A7853ebB5d28"},
    {"name": "BSW-USD", "address": "0x965F527D9159dCe6288a2219DB51fc6Eef120dD1"},
    {"name": "Banana-USD", "address": "0x603c7f932ED1fc6575303D8Fb018fDCBb0f39a95"},

]

# symbols = json.load(symbols)


start_date = '2021-09-01'
end_date = '2023-03-06'
# all_data = pd.DataFrame()


def uploadPerformanceV2():
    for symbol in symbols:
        token = symbol["name"]
        address = symbol["address"]
        url = f'https://us-central1-xwinstage.cloudfunctions.net/importTokenPriceHistory?contractAddress={address}&collection=performanceV2'
        filename = f'{token}.csv'
        print(filename, url)


def uploadPerformanceUSD():
    for symbol in symbols:
        token = symbol["name"]
        address = symbol["address"]
        url = f'https://us-central1-xwinstage.cloudfunctions.net/importTokenPriceHistory?contractAddress={address}&collection=performanceUSD'
        filename = f'{token}.csv'
        print(filename, url)


def uploadPerformanceLocal():
    for symbol in symbols:
        token = symbol["name"]
        address = symbol["address"]
        url = f'https://us-central1-xwinstage.cloudfunctions.net/importTokenPriceHistory?contractAddress={address}&collection=performancelocal'
        filename = f'{token}.csv'
        print(filename, url)


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


def main():
    getHistoricalData()
    uploadPerformanceV2()
    uploadPerformanceUSD()
    uploadPerformanceLocal()


# printToken()
main()
