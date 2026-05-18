# Exploring Negative Theta for Time Series Forecasting in Python

Published: 2025-01-22
Medium: [https://medium.com/@kyle-t-jones/exploring-negative-theta-for-time-series-forecasting-in-python-0af751445fe2](https://medium.com/@kyle-t-jones/exploring-negative-theta-for-time-series-forecasting-in-python-0af751445fe2)

## Business context

Negative Theta is a time series forecasting technique that combines decomposition, linear extrapolation, and an ensemble. It is particularly useful for time series with strong trends and seasonality.

The Theta method was introduced by Assimakopoulos and Nikolopoulos (2000). It is based on decomposing a time series into two or more components, then forecasting and recombining them. The core idea is to modify the curvature of the time series by applying a "theta coefficient" and use the linear and adjusted components for forecasting.

1. [Decompose the time series into a trend and a seasonality component.] 2. [Apply a theta transformation to adjust the curvature of the trend.] 3. [Forecast each component separately.] 4. [Combine the forecasts to produce the final result.]

## About

Place the code for this article in this repository.
The original article export is saved as `article.md`.

## Files

Add your `.ipynb`, `.py`, `.yaml`, `.js`, `.ts`, or other project files here.

## Disclaimer

Educational/demo code only. Not financial, safety, or engineering advice. Use at your own risk. Verify results independently before any production or operational use.

## License

MIT — see [LICENSE](LICENSE).