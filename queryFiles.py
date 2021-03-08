import pandas as pd
import os
import fnmatch


def queryData():
    path = '~/desktop/stocksdata/'
    all_files = fnmatch.filter(os.listdir(path), '*.csv')
    final_stocks_df = pd.DataFrame(
        columns=['symbol', 'start_price', 'end_price'])
    for f in all_files:
        df_from_each_file = pd.read_csv(path+f, header=None)
        df_from_each_file.columns = ['symbol', 'start_price', 'end_price']
        final_stocks_df = final_stocks_df.append(
            [df_from_each_file], ignore_index=True)
    final_stocks_df = final_stocks_df.reset_index()
    print(final_stocks_df)
