# XiaoBiu-AI-Quant-System

一個模組化、可擴展的 AI 量化交易系統，結合多代理架構與現代前後端技術。

---

## 系統架構

![系統架構圖](public/x-biu-ai-quant-full-mmd.png)

---

## 主要目錄結構

```
backend/      # 後端核心（代理、API、工具）
frontend/     # 前端 React 應用
rust_modules/ # Rust 擴展（可選）
```

---

## 核心組件簡介

- **Coordinator**：協調各代理溝通與調度
- **DataAgent**：數據收集與預處理
- **StrategyAgent**：交易策略與分析
- **DecisionAgent**：決策生成
- **ExecutionAgent**：下單執行
- **RiskAgent**：風險監控
- **前端（React）**：用戶操作介面、儀表盤、報告

---

## 快速開始

1. 安裝 Python 依賴：
   ```bash
   pip install -r requirements.txt
   ```
2. 前端安裝依賴並啟動：
   ```bash
   cd frontend
   npm install && npm start
   ```

---

## 其他

- 詳細開發、部署與使用說明請見各子目錄 README。
- 歡迎 PR 與 issue。
