
'''
from IPython.core.display import HTML
HTML("""
[style]
.container { width: 100% !important;}
[/style]
""")
'''

import numpy as np
import pandas as pd
import datetime
import scipy.optimize as opt
import math

from ib_async import *

#util.startLoop() # enable this line when in notebook
ib = IB()
ib.connect(port=4002, timeout=30)

#https://nbviewer.org/github/erdewit/ib_insync/blob/master/notebooks/option_chain.ipynb
spx = Index('SPX', 'CBOE')
ib.qualifyContracts(spx)
ib.reqMarketDataType(4)
[ticker] = ib.reqTickers(spx)
spxValue = ticker.marketPrice()

print(f"symbol: {spx.symbol}, spxValue: {spxValue}")

chains = ib.reqSecDefOptParams(spx.symbol, '', spx.secType, spx.conId)

util.df(chains)

print(chains[0].expirations)

ib.disconnect()



