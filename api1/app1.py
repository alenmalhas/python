'''
Protect the API with keycloak

https://pythonawesome.com/keycloak-integration-for-python-fastapi/#:~:text=Welcome%20to%20fastapi-keycloak.%20This%20projects%20goal%20is%20to,method%20accepts%20any%20JWT%20that%20was%20signed%20using

https://fastapi-keycloak.code-specialist.com/
'''


import uvicorn
from typing import Union, Optional
from fastapi_keycloak import FastAPIKeycloak, OIDCUser
from fastapi import FastAPI, Depends, Body, Header
from fastapi.testclient import TestClient
from fastapi.responses import JSONResponse

from utils.mysqlHelper1 import mysqlHelper1

import numpy as np
import pandas as pd
from pandas_datareader import data as pdr

# below lines are necessary otherwise the code throws error: get_data_yahoo TypeError: string indices must be integers, not 'str'
import yfinance as yfin
yfin.pdr_override()

app = FastAPI()
idp = FastAPIKeycloak(
    #server_url="https://auth.some-domain.com/auth",
    # http://xps15:8180/realms/master/account/
    server_url="http://xps15:8085/auth",
    client_id="python-api-client1",
    client_secret="2pUzuY341JtmvN995dUkPR8WFIrd6ajC",
    admin_client_secret="BIcczGsZ6I8W5zf0rZg5qSexlloQLPKB",
    realm="Test",
    callback_uri="http://localhost:8081/callback"
)
idp.add_swagger_config(app)

@app.get("/admin")
def admin(user: OIDCUser = Depends(idp.get_current_user(required_roles=["admin"]))):
    return f'Hi premium user {user}'

@app.get("/user/roles")
def user_roles(user: OIDCUser = Depends(idp.get_current_user)):
    return f'{user.roles}'

@app.get("/public/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/public/db")
def connect_to_db(
    user_agent: Optional[str] = Header(None, include_in_schema=False), 
    size: Optional[int] = Body(None) ):

    queryPrice = """
        SELECT p.AsOfDate, i.ISIN, p.ClosePrice, i.PriceCurrency, i.LegalName
        FROM fundprices p 
        LEFT JOIN fundinfos i on i.Id=p.FundInfoId
        WHERE year(p.AsOfDate)='2023' AND month(p.AsOfDate)='4' and day(p.AsOfDate)='12' AND HOUR(p.AsOfDate) > 0
            AND i.LegalName LIKE '%equity%'
        ORDER BY i.LegalName
        LIMIT 10;
        """
    h1 = mysqlHelper1(queryPrice)
    resList = h1.exec()
    #return Response(content=None, media_type="application/json")
    objArray = []
    for res in resList:
        #print(res)
        objArray.append({
            'asOfDate' : res[0].strftime('%Y-%m-%d'),
            'isin' : res[1],
            'closePrice' : res[2],
            'currency' : res[3],
            'legalName' : res[4]
        })
    return JSONResponse(content=objArray)

if __name__ == '__main__':
    uvicorn.run('app1:app', host="127.0.0.1", port=8081)


@app.get("/user/prices/{ticker}")
def user_roles(ticker: str = "TUPRS.IS", user: OIDCUser = Depends(idp.get_current_user)):
    symbols_tr_1 = ticker
    prices_all_cols = pdr.get_data_yahoo(symbols_tr_1, start="2023-01-01", end="2023-04-19")
    #prices_all_cols.to_csv (r'C:\temp5\prices\prices-20230101-20230419-symbols_tr_2.csv')
    prices_all_cols.head(5)
    #prices_symbols_tr_fromDisk = pd.read_csv(r'C:\temp5\prices\prices-20230101-20230419-symbols_tr_1.csv')
    prices = prices_all_cols['Adj Close']
    returns = prices.pct_change()

    noOfPeriods = returns.shape[0]
    nreturn_day_avg = (returns+1).prod() / noOfPeriods
    return_annualized = nreturn_day_avg*np.sqrt(252)

    volatility_daily = returns.std()
    volatility_annualized = volatility_daily*np.sqrt(252)

    outString = f"noOfPeriods: {noOfPeriods} \nreturn_day_avg: {nreturn_day_avg} return_annualized: {return_annualized} \nvolatility_daily: {volatility_daily} volatility_annualized: {volatility_annualized}"
    outObj = {
        'ticker' : ticker,
        'noOfPeriods': noOfPeriods,
        'nreturn_day_avg' : nreturn_day_avg, 
        'return_annualized': return_annualized,
        'volatility_daily': volatility_daily,
        'volatility_annualized': volatility_annualized,
    }

    print(outObj)
    return JSONResponse(content=outObj)

