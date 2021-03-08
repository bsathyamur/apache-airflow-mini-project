#import fix_yahoo_finance as fyf
#import yfinance as yf
from pandas_datareader import data as pdr
from datetime import date, datetime, timedelta
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pathlib


def stock_yfinance(symbol,execution_dt):
    try:
        date_folder = datetime.today().strftime('%Y-%m-%d')
        start_date = date.today()
        end_date = start_date + timedelta(days=1)

        # fyf.pdr_override()
        #tsla_df = fyf.get_data_yahoo('TSLA', start=start_date, end=end_date)
        #tsla_df = fyf.download('TSLA', start=start_date, end=end_date)

        # initialize data for TSLA and AAPL dataframe
        if symbol == "TSLA":
            data = [['tsla', 10, 12], ['tsla', 15, 16], ['tsla', 17, 18]]

        if symbol == "AAPL":
            data = [['aapl', 10, 12], ['aapl', 15, 16], ['aapl', 17, 18]]

        # Create the pandas DataFrame
        final_df = pd.DataFrame(data, columns=['ticker', 'start_price', 'end_price'])

        full_path = "~/desktop/airflow-prj/tmp/data/" + str(execution_dt) + "/"
        final_df.to_csv(full_path + symbol + "_data.csv",header=False,index = False)
        return True

    except Exception as e:
        print(str(e))
        return False

# def main():
#	if tesla_yfinance():
#		return True
#	else:
#		return False

# if __name__ == "__main__":
#    main()
