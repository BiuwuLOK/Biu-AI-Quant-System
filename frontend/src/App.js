// src/App.js
import React, { useState, useEffect } from "react";
import Dashboard from "./components/Dashboard";
import ControlPanel from "./components/ControlPanel";
import "./App.css";

function App() {
  const [systemStatus, setSystemStatus] = useState("stopped");
  const [agents, setAgents] = useState([]);
  const [trades, setTrades] = useState([]);
  const [portfolio, setPortfolio] = useState({});

  // 从API获取系统状态
  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const response = await fetch("/api/system/status");
        const data = await response.json();
        setSystemStatus(data.status);
        setAgents(data.agents);
      } catch (error) {
        console.error("Error fetching system status:", error);
      }
    };

    fetchStatus();
    const interval = setInterval(fetchStatus, 5000);
    return () => clearInterval(interval);
  }, []);

  // 从API获取交易历史
  useEffect(() => {
    const fetchTrades = async () => {
      try {
        const response = await fetch("/api/trades");
        const data = await response.json();
        setTrades(data);
      } catch (error) {
        console.error("Error fetching trades:", error);
      }
    };

    fetchTrades();
    const interval = setInterval(fetchTrades, 10000);
    return () => clearInterval(interval);
  }, []);

  // 从API获取投资组合
  useEffect(() => {
    const fetchPortfolio = async () => {
      try {
        const response = await fetch("/api/portfolio");
        const data = await response.json();
        setPortfolio(data);
      } catch (error) {
        console.error("Error fetching portfolio:", error);
      }
    };

    fetchPortfolio();
    const interval = setInterval(fetchPortfolio, 10000);
    return () => clearInterval(interval);
  }, []);

  // 启动系统
  const handleStart = async () => {
    try {
      const response = await fetch("/api/system/start", { method: "POST" });
      const data = await response.json();
      setSystemStatus(data.status);
    } catch (error) {
      console.error("Error starting system:", error);
    }
  };

  // 停止系统
  const handleStop = async () => {
    try {
      const response = await fetch("/api/system/stop", { method: "POST" });
      const data = await response.json();
      setSystemStatus(data.status);
    } catch (error) {
      console.error("Error stopping system:", error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>投资代理系统</h1>
        <div className="system-status">
          系统状态:{" "}
          <span className={`status-${systemStatus}`}>{systemStatus}</span>
        </div>
      </header>

      <main>
        <Dashboard trades={trades} portfolio={portfolio} agents={agents} />

        <ControlPanel
          systemStatus={systemStatus}
          onStart={handleStart}
          onStop={handleStop}
        />
      </main>
    </div>
  );
}

export default App;
