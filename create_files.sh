#!/bin/bash

# Create directories first
mkdir -p backend/agents backend/lib backend/api
mkdir -p frontend/public frontend/src/components frontend/src/styles
mkdir -p rust_modules/src

# Create backend files
touch backend/agents/{__init__.py,coordinator.py,base_agent.py,data_agent.py,macd_agent.py,decision_agent.py,execution_agent.py,risk_agent.py}
touch backend/lib/{__init__.py,indicators.py,analysis.py}
touch backend/api/{__init__.py,main.py}
touch backend/config.py

# Create frontend files
touch frontend/src/{App.js,index.js}
touch frontend/src/components/{Dashboard.js,ControlPanel.js,TradeHistory.js,Portfolio.js}
touch frontend/{package.json,README.md}

# Create rust modules files
touch rust_modules/Cargo.toml
touch rust_modules/src/lib.rs

# Create root files
touch requirements.txt setup.py

echo "File structure created successfully!"