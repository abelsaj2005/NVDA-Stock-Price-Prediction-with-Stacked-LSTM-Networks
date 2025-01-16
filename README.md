# Nvidia's Stock Price Prediction Using a Stacked LSTM Model

## Overview  
This project utilizes a stacked Long Short-Term Memory (LSTM) model to predict NVIDIA (NVDA) stock prices based on historical market data. The stacked architecture features three LSTM layers, which enables the model to capture hierarchical temporal patterns and analyze both short-term and long-term stock movement trends. I conducted hyperparameter tuning to optimize factors such as the number of units, dropout rates, and learning rates, ultimately improving accuracy and consistency. The model's performance was assessed using several metrics, including RMSE, MAE, R-squared, and MAPE. Additionally, I created visualizations of predicted versus actual prices using Matplotlib to facilitate intuitive analysis. Detailed notes are written in the Jupyter Notebook.

## Future Improvements (Work in Progress)
- Integrate external features like news headlines and tweets for marker sentiment analysis to enhance prediction accuracy.  
- Expand the model to predict stock prices given any ticker.
- Deploy the model as a web application for real-time predictions.  
