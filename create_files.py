import os

files = [
    # Backend files
    "backend/agents/__init__.py",
    "backend/agents/coordinator.py",
    "backend/agents/base_agent.py",
    "backend/agents/data_agent.py",
    "backend/agents/macd_agent.py",
    "backend/agents/decision_agent.py",
    "backend/agents/execution_agent.py",
    "backend/agents/risk_agent.py",
    "backend/utils/__init__.py",
    "backend/utils/indicators.py",
    "backend/utils/analysis.py",
    "backend/api/__init__.py",
    "backend/api/main.py",
    "backend/config.py",

    # Frontend files
    "frontend/src/App.js",
    "frontend/src/index.js",
    "frontend/src/components/Dashboard.js",
    "frontend/src/components/ControlPanel.js",
    "frontend/src/components/TradeHistory.js",
    "frontend/src/components/Portfolio.js",
    "frontend/package.json",
    "frontend/README.md",

    # Rust modules
    "rust_modules/Cargo.toml",
    "rust_modules/src/lib.rs",

    # Root files
    "requirements.txt",
    "setup.py"
]

for file_path in files:
  # Create directory if it doesn't exist
  os.makedirs(os.path.dirname(file_path), exist_ok=True)
  # Create empty file if it doesn't exist
  if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
      pass
