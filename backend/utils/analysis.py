"""
Analysis Module

This module provides financial analysis tools and metrics calculations.
"""

import numpy as np
import pandas as pd
from typing import Union, List, Dict, Optional


def calculate_returns(
  prices: Union[List[float], np.ndarray, pd.Series],
  period: int = 1
) -> np.ndarray:
  """Calculate returns over a specified period."""
  prices = np.array(prices)
  returns = np.diff(prices, period) / prices[:-period]
  return returns


def calculate_volatility(
  returns: Union[List[float], np.ndarray, pd.Series],
  window: int = 252
) -> float:
  """Calculate annualized volatility."""
  returns = np.array(returns)
  return np.std(returns) * np.sqrt(window)


def calculate_sharpe_ratio(
  returns: Union[List[float], np.ndarray, pd.Series],
  risk_free_rate: float = 0.02,
  window: int = 252
) -> float:
  """Calculate the Sharpe ratio."""
  returns = np.array(returns)
  excess_returns = returns - risk_free_rate / window
  volatility = calculate_volatility(returns, window)
  return np.mean(excess_returns) / volatility * np.sqrt(window)


def perform_backtest(
  strategy_returns: Union[List[float], np.ndarray, pd.Series],
  benchmark_returns: Optional[Union[List[float], np.ndarray, pd.Series]] = None
) -> Dict:
  """Perform basic backtest analysis."""
  strategy_returns = np.array(strategy_returns)
  
  results = {
    'total_return': np.prod(1 + strategy_returns) - 1,
    'annualized_return': np.mean(strategy_returns) * 252,
    'volatility': calculate_volatility(strategy_returns),
    'sharpe_ratio': calculate_sharpe_ratio(strategy_returns)
  }
  
  if benchmark_returns is not None:
    benchmark_returns = np.array(benchmark_returns)
    results['benchmark_return'] = np.prod(1 + benchmark_returns) - 1
    results['alpha'] = results['annualized_return'] - np.mean(benchmark_returns) * 252
  
  return results
