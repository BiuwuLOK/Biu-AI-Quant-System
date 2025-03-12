from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import json
from typing import List, Dict, Any

def create_app() -> FastAPI:
  return FastAPI(title="Investment Agent System API")

def setup_routes(app: FastAPI) -> None:
  pass  # Routes are defined using decorators

def setup_middleware(app: FastAPI) -> None:
  pass  # Add middleware setup if needed

app = create_app()

# 全局状态
system_coordinator = None

# 启动系统


@app.post("/api/system/start")
async def start_system():
  global system_coordinator
  if system_coordinator is None:
    # 初始化系统
    from agents.coordinator import AgentCoordinator
    from agents.data_agent import DataAgent
    from agents.macd_agent import MACDStrategyAgent
    from agents.decision_agent import DecisionAgent
    from agents.execution_agent import ExecutionAgent
    from agents.risk_agent import RiskManagementAgent

    system_coordinator = AgentCoordinator()

    # 创建代理
    data_agent = DataAgent("data_agent", symbols=[
                           "AAPL", "MSFT", "GOOG", "AMZN"])
    macd_agent = MACDStrategyAgent("macd_agent")
    decision_agent = DecisionAgent("decision_agent")
    execution_agent = ExecutionAgent("execution_agent", paper_trading=True)
    risk_agent = RiskManagementAgent("risk_agent")

    # 注册代理
    system_coordinator.register_agent("data_agent", data_agent)
    system_coordinator.register_agent("macd_agent", macd_agent)
    system_coordinator.register_agent("decision_agent", decision_agent)
    system_coordinator.register_agent("execution_agent", execution_agent)
    system_coordinator.register_agent("risk_agent", risk_agent)

    # 启动系统
    system_coordinator.start()

  return {"status": "running"}

# 停止系统


@app.post("/api/system/stop")
async def stop_system():
  global system_coordinator
  if system_coordinator is not None:
    system_coordinator.stop()
    system_coordinator = None
  return {"status": "stopped"}

# 获取系统状态


@app.get("/api/system/status")
async def get_system_status():
  global system_coordinator
  if system_coordinator is None:
    return {"status": "stopped", "agents": []}

  agents = []
  for name, agent in system_coordinator.agents.items():
    agents.append({
        "name": name,
        "status": "running" if agent.running else "stopped"
    })

  return {"status": "running", "agents": agents}

# 获取交易历史


@app.get("/api/trades")
async def get_trades():
  global system_coordinator
  if system_coordinator is None:
    return []

  execution_agent = system_coordinator.agents.get("execution_agent")
  if execution_agent is None:
    return []

  return execution_agent.orders

# 获取投资组合


@app.get("/api/portfolio")
async def get_portfolio():
  global system_coordinator
  if system_coordinator is None:
    return {}

  execution_agent = system_coordinator.agents.get("execution_agent")
  if execution_agent is None:
    return {}

  return {
      "cash": execution_agent.cash,
      "positions": execution_agent.portfolio
  }

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
