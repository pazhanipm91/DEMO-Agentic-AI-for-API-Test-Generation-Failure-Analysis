# DEMO-Agentic-AI-for-API-Test-Generation-Failure-Analysis
Planner Agent code, Failure Analyzer Agent code and a complete runnable demo structure.
# Agentic AI for API Test Generation & Failure Analysis

This project demonstrates an **Agentic AI system** that autonomously:
- Parses OpenAPI specifications
- Plans API test strategies
- Generates executable pytest tests
- Executes tests
- Analyzes failures using reasoning-based agents

## 🧠 Architecture
Planner Agent → Test Generator Agent → Test Executor → Failure Analyzer Agent

## 🔍 Why Agentic AI?
Traditional test automation is static.
This system adapts, reasons, and explains failures using agent collaboration.

## 🚀 Features
- Risk-based test planning
- Autonomous test generation
- Failure classification & root cause analysis
- Designed using Planner–Executor–Evaluator pattern

## 🧪 Example Failure Analysis Output
```json
{
  "failure_type": "ASSERTION_ERROR",
  "confidence": 0.85,
  "recommended_action": "Update expected response or validate API regression"
}

