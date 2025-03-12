"""
Technical Indicators Module

This module provides implementations of various technical indicators used in trading strategies.
"""

import numpy as np
import pandas as pd
from typing import Union, List, Tuple


def calculate_macd(
    prices: Union[List[float], np.ndarray, pd.Series],
    fast_period: int = 12,
    slow_period: int = 26,
    signal_period: int = 9
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
  """
  Calculate the MACD (Moving Average Convergence Divergence) indicator.

  Args:
      prices: Price data
      fast_period: Period for the fast EMA (default: 12)
      slow_period: Period for the slow EMA (default: 26)
      signal_period: Period for the signal line (default: 9)

  Returns:
      Tuple containing (macd_line, signal_line, histogram)
  """
  prices = np.asarray(prices, dtype=np.float64)
  
  # Calculate EMAs
  fast_ema = pd.Series(prices).ewm(span=fast_period, adjust=False).mean().to_numpy()
  slow_ema = pd.Series(prices).ewm(span=slow_period, adjust=False).mean().to_numpy()
  
  # Calculate MACD line
  macd_line = fast_ema - slow_ema
  
  # Calculate signal line
  signal_line = pd.Series(macd_line).ewm(span=signal_period, adjust=False).mean().to_numpy()
  
  # Calculate histogram
  histogram = macd_line - signal_line
  
  return macd_line, signal_line, histogram


def calculate_rsi(
    prices: Union[List[float], np.ndarray, pd.Series],
    period: int = 14
) -> np.ndarray:
  """
  Calculate the RSI (Relative Strength Index) indicator.

  Args:
      prices: Price data
      period: RSI period (default: 14)

  Returns:
      numpy array containing RSI values
  """
  prices = np.asarray(prices, dtype=np.float64)
  deltas = np.diff(prices)
  seed = deltas[:period+1]
  up = seed[seed >= 0].sum()/period
  down = -seed[seed < 0].sum()/period
  rs = up/down
  rsi = np.zeros_like(prices)
  rsi[period] = 100. - 100./(1. + rs)

  for i in range(period+1, len(prices)):
    delta = deltas[i-1]
    if delta > 0:
      upval = delta
      downval = 0.
    else:
      upval = 0.
      downval = -delta

    up = (up*(period-1) + upval)/period
    down = (down*(period-1) + downval)/period
    rs = up/down
    rsi[i] = 100. - 100./(1. + rs)

  return rsi


def calculate_bollinger_bands(
    prices: Union[List[float], np.ndarray, pd.Series],
    period: int = 20,
    num_std: float = 2.0
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
  """
  Calculate Bollinger Bands.

  Args:
      prices: Price data
      period: Moving average period (default: 20)
      num_std: Number of standard deviations (default: 2.0)

  Returns:
      Tuple containing (upper_band, middle_band, lower_band)
  """
  prices = np.asarray(prices, dtype=np.float64)
  middle_band = pd.Series(prices).rolling(window=period).mean().to_numpy()
  std = pd.Series(prices).rolling(window=period).std().to_numpy()
  
  upper_band = middle_band + (std * num_std)
  lower_band = middle_band - (std * num_std)
  
  return upper_band, middle_band, lower_band
