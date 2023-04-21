'''
Protect the API with keycloak

https://pythonawesome.com/keycloak-integration-for-python-fastapi/#:~:text=Welcome%20to%20fastapi-keycloak.%20This%20projects%20goal%20is%20to,method%20accepts%20any%20JWT%20that%20was%20signed%20using

https://fastapi-keycloak.code-specialist.com/

https://www.coursera.org/learn/introduction-portfolio-construction-python/lecture/PM6k4/lab-session-risk-adjusted-returns
'''


from jose import ExpiredSignatureError
import uvicorn
from typing import Annotated, Union, Optional
from fastapi_keycloak import FastAPIKeycloak, OIDCUser
from fastapi import FastAPI, Depends, Body, Header, Query, Request, HTTPException
from fastapi.testclient import TestClient
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi


from utils.mysqlHelper1 import mysqlHelper1

import numpy as np
import pandas as pd
import pandas_ta as ta
from pandas_datareader import data as pdr
import datetime as dt


# below lines are necessary otherwise the code throws error: get_data_yahoo TypeError: string indices must be integers, not 'str'
import yfinance as yfin
yfin.pdr_override()

def remove_request_body_for_get(endpoints):
    for route in endpoints:
        if route.methods == ["GET"]:
            for content_type in route.content_types:
                if content_type.get("schema"):
                    content_type["schema"] = None
    return endpoints

app = FastAPI(    
        title="FastAPI App1",          
        description="python with fastapi",
        version="0.0.1",
        terms_of_service="http://example.com/terms/",
        contact={
            "name": "veni vidi vici",
            "url": "https://www.coursera.org/learn/introduction-portfolio-construction-python/lecture/PM6k4/lab-session-risk-adjusted-returns",
            "email": "email@test.com",
        },
        license_info={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
    )

idp = FastAPIKeycloak(
    server_url="http://xps15:8085/auth",
    client_id="python-api-client1",
    client_secret="2pUzuY341JtmvN995dUkPR8WFIrd6ajC",
    admin_client_secret="BIcczGsZ6I8W5zf0rZg5qSexlloQLPKB",
    realm="Test",
    callback_uri="http://localhost:8081/callback"
)
idp.add_swagger_config(app)


@app.exception_handler(ExpiredSignatureError)
async def expired_signature_error_handler(request, exc):
    #raise HTTPException(status_code=401, detail="Expired Signature")
    resp = JSONResponse(content= f"{exc}", status_code=401)
    return resp

@app.get("/admin")
def admin(user: OIDCUser = Depends(idp.get_current_user(required_roles=["admin"]))):
    return f'Hi premium user {user}'

@app.get("/user/roles")
def user_roles(
        #user: OIDCUser = Depends(idp.get_current_user)):
        user: OIDCUser = Depends(idp.get_current_user(required_roles=["api-user"]))):
    try:
        outObj = {
            'preferred_username': user.preferred_username,
            'email': user.email,
            'given_name' : user.given_name,
            'family_name' : user.family_name,
            'roles' : user.realm_access['roles']
        }
        resp = JSONResponse(content=outObj, status_code=200)
    except Exception as e:
        resp = JSONResponse(content= f"error: " + e.__str__(), status_code=400)
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Expired Signature")

    return resp


from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    roles: list

# @app.get("/user/me", response_model=User)
# async def read_users_me(user: User = Depends(idp.get_current_user)):
#     return user

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/user/me")
#async def read_items(token: str = Depends(oauth2_scheme)):
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


@app.get("/public/db")
def connect_to_db():
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
    uvicorn.run('app1:app', host="127.0.0.1", port=8081, reload=True)

@app.get("/mytest1/")
def read_items(q: list[int] = Query(None)):
    return {"q": q}

@app.get("/public/test/{item_id}")
def read_item(item_id: Union[int, None] = None, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/user/prices/ticker")
def get_ret_vol_by_ticker(
    ticker: str = "SPY"
    #, user: OIDCUser = Depends(idp.get_current_user)
    ):
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



@app.get("/public/moving-average")
def calc_moving_average(tickers: str = 'BTC-USD ETH-USD XRP-USD XEM-USD'):
    tickersArr = tickers.split(' ')

    technicals = ['sma10', 'sma25', 'vwma']

    endDate = dt.datetime.today().strftime('%Y-%m-%d')
    startDate = (dt.datetime.today()-dt.timedelta(60)).strftime('%Y-%m-%d')

    df = yfin.download(tickersArr, start=startDate, end=endDate, interval='1d',)
    
    for ticker in tickersArr:
        for tech in technicals:
            if tech[:2] == 'sma':
                noOfDays = int(tech[3:])
                df[(tech, ticker)] = ta.sma(df.loc[:,('Close', ticker)], length=noOfDays)
            else:
                df[(tech, ticker)] = ta.vwma(df.loc[:,('Close', ticker)], df.loc[:,('Volume', ticker)])
    
    return df.to_json()

