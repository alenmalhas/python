import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
import datetime as dt

import yfinance as yfin
yfin.pdr_override()


def read_from_file():
    prices_symbols_tr = pd.read_csv(r'C:\temp5\prices\prices-20230101-20230419-symbols_tr_1.csv')
    prices = prices_symbols_tr['Adj Close']
    returns = prices.pct_change()
    noOfPeriods = returns.shape[0]
    return_avg = (returns+1).prod() / noOfPeriods
    return_annualized = return_avg*np.sqrt(252)
    volatility_daily = returns.std()
    volatility_annualized = volatility_daily*np.sqrt(252)
    print(f"noOfPeriods: {noOfPeriods} \nreturn_day_avg: {return_avg} return_annual: {return_annualized} \nvol_day: {volatility_daily} vol_annual: {volatility_annualized}")


def get_data_from_yf():
    symbols_tr_1 = "TUPRS.IS"
    endDate = dt.datetime.today().strftime('%Y-%m-%d')
    startDate = (dt.datetime.today()-dt.timedelta(7)).strftime('%Y-%m-%d')
    prices_all_cols = pdr.get_data_yahoo(symbols_tr_1, start=startDate, end=endDate)
                                            #start="2023-01-01", end="2023-04-19")
    #prices_all_cols.to_csv (r'C:\temp5\prices\prices-20230101-20230419-symbols_tr_2.csv')
    prices_all_cols.head(5)
    #prices_symbols_tr_fromDisk = pd.read_csv(r'C:\temp5\prices\prices-20230101-20230419-symbols_tr_1.csv')
    prices = prices_all_cols['Adj Close']
    returns = prices.pct_change()

    noOfPeriods = returns.shape[0]
    return_avg = (returns+1).prod() / noOfPeriods
    return_annualized = return_avg*np.sqrt(252)

    volatility_daily = returns.std()
    volatility_annualized = volatility_daily*np.sqrt(252)

    outString = f"noOfPeriods: {noOfPeriods} \nreturn_day_avg: {return_avg} return_annual: {return_annualized} \nvol_day: {volatility_daily} vol_annual: {volatility_annualized}"

    print(outString)

def get_test_data_spy():
    endDate = dt.datetime.today().strftime('%Y-%m-%d')
    startDate = (dt.datetime.today()-dt.timedelta(7)).strftime('%Y-%m-%d')
    spy = pdr.get_data_yahoo('SPY', start=startDate, end=endDate)
                             #start='2022-10-24', end='2022-12-23')
    print(spy)

get_test_data_spy()
#get_data_from_yf()