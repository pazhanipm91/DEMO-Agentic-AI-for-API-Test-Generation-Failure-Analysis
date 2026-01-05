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


Each agent has a **single responsibility** and communicates via structured outputs, making the system explainable, extensible, and production-ready.

---

## 🧩 Core Agents

### 🧠 Planner Agent
- Parses OpenAPI specifications
- Identifies endpoints and risk areas
- Creates a structured test strategy (happy path, negative, boundary)

### 🧪 Test Generator Agent
- Generates executable `pytest` API tests
- Converts abstract plans into real test code

### 🔍 Failure Analyzer Agent
- Analyzes pytest execution logs
- Classifies failures (assertion, schema mismatch, server error, etc.)
- Produces root cause explanations with confidence scoring

---

## 🔍 Why Agentic AI?
Traditional LLM-based automation stops at content generation.

This system:
- Uses **reasoning-based agents**
- Separates planning, execution, and evaluation
- Avoids prompt-only workflows
- Enables deterministic behavior with explainability

This architecture is inspired by **real-world GenAI systems deployed in production**.

---

## 🚀 Features
- Risk-based API test planning
- Autonomous pytest generation
- Failure classification & root cause analysis
- Modular agent design
- CI/CD-friendly execution model

---

## 🧪 Example Failure Analysis Output

```json
{
  "failure_type": "ASSERTION_ERROR",
  "confidence": 0.85,
  "explanation": "Expected status code mismatch detected",
  "recommended_action": "Validate API regression or update expected response"
}

## How TO Run Locally"
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt

python app.py


• Built a production-grade Agentic AI framework for autonomous API test generation and intelligent failure analysis using GenAI and multi-agent orchestration.


### Credits
### 👤 Author

Lead AI Engineer with 7+ years of experience building production-grade AI systems,
specializing in GenAI, Agentic AI, API platforms, and intelligent test automation.

LinkedIn: https://www.linkedin.com/in/pazhanichamy-pandi-77a60b2bb/
