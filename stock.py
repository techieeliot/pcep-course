import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date


disney_stock = yf.download("DIS", start=date(2018, 1, 1), end=date.today())

plt.plot(disney_stock['Close'], label='Disney Stock Price', color='blue')
plt.title('Disney Stock Price Over the Last 5 Years')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid()
plt.show()

df = pd.DataFrame(disney_stock)


pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 5)
pd.set_option('display.width', 1000)


print("DataFrame Head:\n", df.head())

