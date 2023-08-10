import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.interpolate as interpolate

!pip install yahoo_fin
from yahoo_fin.stock_info import get_data

daily_data = get_data("ongc.ns", start_date="01/01/2013", end_date="12/31/2022", index_as_date=True, interval="1d")
ongc_daily_closing = daily_data['close']
ongc_monthly_close = ongc_daily_closing.loc[ongc_daily_closing.index.day == 1]
plt.scatter(ongc_monthly_close.index, ongc_monthly_close, s=2)
plt.xlabel('Timestamp')
plt.ylabel('Stock Price')
plt.show()

#Interpolation
x_data = [date.timestamp() for date in ongc_monthly_close.index]
print(x_data)
f = interpolate.interp1d(x_data, ongc_monthly_close)

import datetime
dates_to_check = [(date + datetime.timedelta(days = 14)).timestamp() for date in ongc_monthly_close.index]
dates_to_check.pop()

interpolated_values = f(dates_to_check)
plt.scatter(dates_to_check, interpolated_values, s=2, c="r")
plt.scatter(x_data, ongc_monthly_close, s=2, c="g")
plt.xlabel("Timestamp")
plt.ylabel("Stock Price")
plt.show()

model = np.poly1d(np.polyfit(dates_to_check, interpolated_values, 3))
train_data = model(dates_to_check)
plt.scatter(dates_to_check, interpolated_values, s=2, c="r")
plt.plot(dates_to_check, train_data, c="black")
plt.show()
#Extrapolation
actual_stock_data = get_data("ongc.ns", start_date = "01/01/2023", end_date = "02/28/2023", index_as_date = True, interval = "1d")
actual_stock_data = actual_stock_data["close"]
len(actual_stock_data)
start_date = datetime.datetime(2022,12,31,0,0,0)
end_date = datetime.datetime(2023,2,28,0,0,0)
forecast_dates = []
for date in actual_stock_data.index:
  forecast_dates.append(date.timestamp())
  start_date += datetime.timedelta(days=1)
print(len(forecast_dates))
prediction = model(forecast_dates)
prediction
plt.scatter(dates_to_check, interpolated_values, s=2, c="r")
plt.plot(dates_to_check, train_data, c= "black")
plt.plot(forecast_dates, prediction, c="green")
plt.show()
#t-test
import scipy.stats as stats
stats.ttest_ind(a = actual_stock_data, b = prediction, equal_var = False)
