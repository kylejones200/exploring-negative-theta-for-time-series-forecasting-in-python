# Description: Short example for Exploring Negative Theta for Time Series Forecasting in Python.



# Load the dataset

from data_io import read_csv
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
data = read_csv(url, parse_dates=['Month'], index_col='Month')
data.rename(columns={'Passengers': 'AirPassengers'}, inplace=True)
# Visualize the dataset
plt.figure(figsize=(10, 6))
plt.plot(data, label="AirPassengers", color="blue")
plt.title("Monthly Air Passengers")
plt.xlabel("Date")
plt.ylabel("Number of Passengers")
plt.legend()
plt.savefig("air_passengers_plot.png")
plt.show()


# Decompose the time series
result = seasonal_decompose(data['AirPassengers'], model='multiplicative')
# Plot the decomposition
result.plot()
plt.tight_layout()
plt.savefig("decomposition_plot.png")
plt.show()

def theta_transform(series, theta=2):
    linear_trend = np.poly1d(np.polyfit(range(len(series)), series, 1))(range(len(series)))
    theta_series = theta * series - (theta - 1) * linear_trend
    return theta_series, linear_trend

# Apply the transformation
theta_series, linear_trend = theta_transform(data['AirPassengers'])
# Visualize the transformed series
plt.figure(figsize=(10, 6))
plt.plot(data['AirPassengers'], label="Original Series", color="blue")
plt.plot(theta_series, label="Theta Series (θ=2)", color="orange")
plt.plot(linear_trend, label="Linear Trend", color="green")
plt.title("Theta Transformation")
plt.xlabel("Time")
plt.ylabel("Passengers")
plt.legend()
plt.savefig("theta_transformation.png")
plt.show()


def forecast_theta(series, forecast_horizon, theta=2):
    # Linear Trend Forecast
    X = np.arange(len(series)).reshape(-1, 1)
    model = LinearRegression()
    model.fit(X, series)
    future_X = np.arange(len(series), len(series) + forecast_horizon).reshape(-1, 1)
    trend_forecast = model.predict(future_X)
    # Theta Series Forecast (using simple naive approach here)
    theta_series, _ = theta_transform(series, theta)
    naive_forecast = np.mean(theta_series[-12:])  # Average of last 12 months
    # Combine forecasts
    combined_forecast = (trend_forecast + naive_forecast) / 2
    return combined_forecast
# Forecast the next 12 months
forecast_horizon = 12
forecast_values = forecast_theta(data['AirPassengers'].values, forecast_horizon)
# Create future time points
future_dates = pd.date_range(data.index[-1], periods=forecast_horizon + 1, freq='M')[1:]
# Visualize the forecast
plt.figure(figsize=(10, 6))
plt.plot(data, label="Historical Data", color="blue")
plt.plot(future_dates, forecast_values, label="Theta Forecast", color="red", linestyle="--")
plt.title("Theta Forecast")
plt.xlabel("Time")
plt.ylabel("Passengers")
plt.legend()
plt.savefig("theta_forecast.png")
plt.show()
