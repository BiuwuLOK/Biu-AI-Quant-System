"""
SiuBiu-AI-Quant-System API Module

This package provides the REST API interface for the quant system.
"""

from .main import (
    create_app,
    setup_routes,
    setup_middleware
)

__all__ = [
    'create_app',
    'setup_routes',
    'setup_middleware'
]

# API version
__version__ = '0.1.4'

# API configurations
DEFAULT_HOST = '0.0.0.0'
DEFAULT_PORT = 8000
DEBUG_MODE = True
