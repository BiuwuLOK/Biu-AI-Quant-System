"""
SiuBiu-AI-Quant-System Library Module

This package contains utility functions and common tools used across the system.
"""

# Technical indicators
from .indicators import (
    calculate_macd,
    calculate_rsi,
    calculate_bollinger_bands
)

# Analysis tools
from .analysis import (
    calculate_returns,
    calculate_volatility,
    calculate_sharpe_ratio,
    perform_backtest
)

__all__ = [
    # Technical indicators
    'calculate_macd',
    'calculate_rsi',
    'calculate_bollinger_bands',

    # Analysis tools
    'calculate_returns',
    'calculate_volatility',
    'calculate_sharpe_ratio',
    'perform_backtest'
]

# Library version
__version__ = '0.1.0'

# Make sure numpy and pandas are available
try:
    import numpy as np
    import pandas as pd
except ImportError as e:
    print(f"Error importing required packages: {e}")
    print("Please ensure numpy and pandas are installed: pip install numpy pandas")
    raise
