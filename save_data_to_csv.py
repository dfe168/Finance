from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import argparse

#http://www.eoddata.com/


def save_dataset(symbol, time_window):
    ts = TimeSeries(key='4HETZQG1BP46TPS4', output_format='pandas')
    if time_window == 'intraday':
        data, meta_data = ts.get_intraday(symbol, interval='1min', outputsize='full')
    elif time_window == 'daily':
        data, meta_data = ts.get_daily(symbol, outputsize='full')
    elif time_window == 'daily_adj':
        data, meta_data = ts.get_daily_adjusted(symbol, outputsize='full')

    pprint(data.head(10))

    #data.to_csv(f'./{data}_{time_window}.csv')
    data.to_csv('savedData.csv')
    print('Data is saved to csv')

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#
#     parser.add_argument('symbol', type=str, help="the stock symbol you want to download")
#     parser.add_argument('time_window', type=str, choices=[
#                         'intraday', 'daily', 'daily_adj'], help="the time period you want to download the stock history for")
#
#     namespace = parser.parse_args()
#     save_dataset(**vars(namespace))