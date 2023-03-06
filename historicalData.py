import yfinance as yf
import pandas as pd

symbols = ["ADA-USD", "ALICE-USD", "ATOM-USD"]


start_date = '2021-09-01'
end_date = '2023-03-06'
# all_data = pd.DataFrame()


for symbol in symbols:
    ticker = yf.Ticker(symbol)

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

    data.to_csv(f'{symbol}.csv', index=False)
