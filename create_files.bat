@echo off
REM Create directories
mkdir backend\agents backend\lib backend\api
mkdir frontend\public frontend\src\components frontend\src\styles
mkdir rust_modules\src

REM Create backend files
type nul > backend\agents\__init__.py
type nul > backend\agents\coordinator.py
type nul > backend\agents\base_agent.py
type nul > backend\agents\data_agent.py
type nul > backend\agents\macd_agent.py
type nul > backend\agents\decision_agent.py
type nul > backend\agents\execution_agent.py
type nul > backend\agents\risk_agent.py
type nul > backend\lib\__init__.py
type nul > backend\lib\indicators.py
type nul > backend\lib\analysis.py
type nul > backend\api\__init__.py
type nul > backend\api\main.py
type nul > backend\config.py

REM Create frontend files
type nul > frontend\src\App.js
type nul > frontend\src\index.js
type nul > frontend\src\components\Dashboard.js
type nul > frontend\src\components\ControlPanel.js
type nul > frontend\src\components\TradeHistory.js
type nul > frontend\src\components\Portfolio.js
type nul > frontend\package.json
type nul > frontend\README.md

REM Create rust modules files
type nul > rust_modules\Cargo.toml
type nul > rust_modules\src\lib.rs

REM Create root files
type nul > requirements.txt
type nul > setup.py

echo File structure created successfully!
pause 