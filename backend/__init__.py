"""
SiuBiu-AI-Quant-System Backend Package

This is the main backend package that includes all components of the quant system.
"""

# Import all components from lib
from .lib import (
    calculate_macd,
    calculate_rsi,
    calculate_bollinger_bands,
    calculate_returns,
    calculate_volatility,
    calculate_sharpe_ratio,
    perform_backtest
)

# Import all agents with aliases
from .agents import (
    AgentCoordinator as Coordinator,
    DataAgent,
    MACDStrategyAgent as MACDAgent,
    DecisionAgent,
    ExecutionAgent,
    RiskManagementAgent as RiskAgent
)

# Import packages
from . import agents
from . import lib
from . import api

__all__ = [
    # Core packages
    'agents', 
    'lib', 
    'api',
    
    # Technical indicators
    'calculate_macd',
    'calculate_rsi',
    'calculate_bollinger_bands',
    
    # Analysis tools
    'calculate_returns',
    'calculate_volatility',
    'calculate_sharpe_ratio',
    'perform_backtest',
    
    # Agents
    'Coordinator',
    'DataAgent',
    'MACDAgent',
    'DecisionAgent',
    'ExecutionAgent',
    'RiskAgent'
]

# Backend version
__version__ = '0.1.0'

# System configurations
DEBUG = True
LOG_LEVEL = 'INFO'

# Import commonly used components for convenience
