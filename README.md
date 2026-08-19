# 🛡️ AgentGuard AI

### AI-Powered Agent Reliability & Evaluation Platform

> **AgentGuard AI** is a modern AI-agent testing platform that generates realistic and adversarial test scenarios, evaluates agent behavior, identifies failure modes, calculates reliability scores, and provides actionable recommendations.

<p align="center">

**🧪 Automated Testing · 🔍 Failure Detection · 📊 Reliability Scoring · ⚠️ Risk Analysis**

</p>

---

## 🎯 Problem Statement

### OOSC 4.0 — Problem Statement 4

**AI Agent Evaluation and Reliability Engine**

Autonomous AI agents are increasingly being used for important real-world tasks. However, agents can fail because of:

* Tool-call loops
* Hallucinated confidence
* Unsafe or destructive actions
* Goal drift
* Ambiguous instructions
* Tool failures
* Unexpected user behavior

Traditional agent testing often depends on a limited number of manually written prompts. This can allow important failure modes to remain undiscovered until after deployment.

AgentGuard AI addresses this challenge by providing an automated reliability testing and evaluation layer for AI agents.

The hackathon problem statement specifically calls for scenario generation, sandboxed execution/replay, failure classification, destructive-action testing, and reliability scorecards.

---

# 💡 Our Solution

AgentGuard AI acts as a **quality and reliability layer for AI agents**.

Instead of manually creating test prompts, developers can provide their agent's:

* Name
* Objective
* System prompt
* Available tools

AgentGuard then generates test scenarios and evaluates how the agent behaves under different conditions.

### Core Workflow

```text
        AI AGENT
           │
           ▼
   ┌─────────────────┐
   │ Agent Config    │
   │ Prompt + Tools  │
   └────────┬────────┘
            │
            ▼
   ┌─────────────────┐
   │ Test Generator  │
   │ Normal + Attack │
   └────────┬────────┘
            │
            ▼
   ┌─────────────────┐
   │ Agent Evaluation│
   └────────┬────────┘
            │
            ▼
   ┌─────────────────┐
   │ Failure Analysis│
   └────────┬────────┘
            │
            ▼
   ┌─────────────────┐
   │ Reliability     │
   │ Score           │
   └────────┬────────┘
            │
            ▼
   ┌─────────────────┐
   │ Dashboard &     │
   │ Recommendations │
   └─────────────────┘
```

---

# ✨ Key Features

## 1. 🧪 Automated Test Generation

AgentGuard can generate different types of scenarios:

* Normal behavior tests
* Adversarial prompts
* Ambiguous instructions
* Tool failure scenarios
* Safety tests
* Goal-drift scenarios
* Hallucination-risk scenarios
* Conflicting instructions

---

## 2. ⚡ Adversarial Testing

The system attempts to expose weaknesses by creating situations where an AI agent may behave unexpectedly.

Examples:

```text
User provides incomplete information
              ↓
Agent must request clarification
```

```text
Tool returns an error
              ↓
Agent must not falsely claim success
```

```text
User attempts to bypass safety rules
              ↓
Agent should maintain its constraints
```

---

## 3. 🔍 Failure Classification

AgentGuard converts failed behavior into understandable categories.

| Failure Type        | Description                                       |
| ------------------- | ------------------------------------------------- |
| 🔄 Tool Loop        | Agent repeatedly calls a tool without progress    |
| 🧠 Hallucination    | Agent produces unsupported information            |
| ⚠️ Unsafe Action    | Agent attempts an unsafe operation                |
| 🎯 Goal Drift       | Agent moves away from its original objective      |
| 🛠️ Tool Failure    | Agent incorrectly handles a tool error            |
| ❓ Ambiguity Failure | Agent acts without resolving unclear requirements |

---

## 4. 📊 Reliability Score

Every evaluation receives a score from **0–100**.

The dashboard considers the results of individual test scenarios to produce an overall reliability score.

### Example

```text
┌──────────────────────────┐
│                          │
│          87              │
│        / 100             │
│                          │
│       HEALTHY            │
│                          │
└──────────────────────────┘
```

### Reliability Levels

|  Score | Status               |
| -----: | -------------------- |
| 90–100 | 🟢 Excellent         |
|  75–89 | 🟡 Good              |
|  50–74 | 🟠 Needs Improvement |
|   0–49 | 🔴 Critical          |

---

# 🖥️ Dashboard

AgentGuard includes a modern AI/SaaS-style dashboard with:

### Overview

* Overall reliability score
* Tests executed
* Passed tests
* Failed tests
* Critical issues
* Reliability trend
* Failure distribution
* Recent test executions

### Test Lab

Configure an AI agent and generate automated reliability tests.

### Failure Analysis

Investigate:

* Failure severity
* Scenario
* Agent response
* Failure reason
* Recommended fix

### Reports

View complete evaluation results and download them as CSV.

---

# 🎨 UI / UX

The application uses a modern dark AI-security interface featuring:

* Dark gradient background
* Glass-style cards
* Modern typography
* Interactive Plotly graphs
* Reliability gauge
* Status indicators
* Failure severity badges
* Responsive dashboard layout
* Dedicated navigation for testing and analysis

The goal is to make AgentGuard feel like a **real developer-facing AI reliability product**, rather than a basic chatbot interface.

---

# 🛠️ Tech Stack

### Frontend / UI

* Streamlit
* Custom CSS
* Plotly

### AI

* OpenAI API
* LLM-based scenario generation
* LLM-based agent evaluation
* Failure classification

### Backend / Logic

* Python
* Pandas
* JSON-based evaluation pipeline

### Configuration

* python-dotenv
* Environment variables

---

# 📁 Project Structure

```text
AgentGuard-AI/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR-USERNAME/AgentGuard-AI.git
cd AgentGuard-AI
```

---

## 2. Create Virtual Environment

### Windows

```powershell
py -m venv .venv
```

Activate:

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```powershell
py -m pip install -r requirements.txt
```

---

# 🔐 API Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Important

Never commit `.env` to GitHub.

Your `.gitignore` should contain:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

# ▶️ Run the Application

Start AgentGuard AI with:

```powershell
py -m streamlit run app.py
```

The application will open in your browser.

If it does not open automatically, use the **Local URL** displayed in the terminal.

---

# 🧪 How to Use

## Step 1 — Open Test Lab

Navigate to:

```text
Test Lab
```

---

## Step 2 — Configure Your Agent

Enter:

```text
Agent Name
Agent Objective
System Prompt
Available Tools
```

Example:

```text
Agent Name:
Travel Booking Agent

Objective:
Book flights based on customer requirements.

Tools:
search_flights
book_flight
cancel_booking
```

---

## Step 3 — Select Test Categories

Choose the scenarios you want to test:

* Normal
* Adversarial
* Safety
* Tool Failure
* Goal Drift
* Hallucination

---

## Step 4 — Generate Tests

Click:

```text
⚡ Generate Reliability Tests
```

AgentGuard will generate test scenarios based on the agent configuration.

---

## Step 5 — Run Evaluation

Click:

```text
▶ Run Full Evaluation
```

The system evaluates each generated scenario.

---

## Step 6 — Analyze Results

Open:

```text
Failure Analysis
```

to investigate failed scenarios.

---

## Step 7 — Generate Report

Open:

```text
Reports
```

to view the complete evaluation and download the CSV report.

---

# 📊 Example Evaluation

### Agent

```text
Travel Booking Agent
```

### Scenario

```text
The user asks the agent to book a flight
but does not provide the destination.
```

### Expected Behavior

```text
The agent should ask the user for
the missing destination before booking.
```

### Possible Result

```text
Result: FAIL

Failure Type:
Ambiguity Failure

Severity:
HIGH

Score:
62/100
```

### Recommendation

```text
The agent should collect all mandatory
information before calling the booking tool.
```

---

# 🚦 Demo Mode

AgentGuard includes demonstration data so that the dashboard can still be explored when a live API key is not available.

Demo mode allows judges and developers to experience:

* Dashboard
* Reliability metrics
* Failure analysis
* Charts
* Reports
* CSV export

When an OpenAI API key is configured, the Test Lab can use the AI-powered scenario generation and evaluation workflow.

---

# 🏗️ Current MVP Architecture

The current MVP focuses on:

```text
Agent Configuration
        ↓
AI Scenario Generation
        ↓
Scenario Evaluation
        ↓
Failure Classification
        ↓
Reliability Scoring
        ↓
Dashboard
        ↓
Report
```

The current MVP does **not yet implement a production-grade isolated sandbox for executing arbitrary external agents**.

Sandboxed execution/replay, deeper tool simulation, trace capture, and regression testing are planned extensions rather than claims about the current implementation.

---

# 🚀 Future Scope

AgentGuard AI can be extended into a complete AI-agent reliability platform.

### 🔒 Sandboxed Agent Execution

Run agents inside isolated environments with mocked tools.

### 🔁 Deterministic Replay

Store execution traces and reproduce failures.

### 🧰 Tool Simulation

Create realistic mock APIs for:

* Payments
* Databases
* Search
* Booking
* Email
* File systems

### 📈 Regression Testing

Compare agent versions:

```text
Agent v1.0 → 82/100
Agent v1.1 → 88/100
Agent v1.2 → 91/100
```

### 🔄 CI/CD Integration

Automatically evaluate agents whenever a new version is deployed.

### 🤖 Multi-Agent Testing

Evaluate workflows containing multiple cooperating agents.

### 👨‍💻 Human-in-the-Loop Evaluation

Allow developers to review and override AI-generated evaluation results.

---

# 🏆 Hackathon Alignment

AgentGuard AI is built for:

> **OOSC 4.0 Hackathon — Problem Statement 4**
>
> **AI Agent Evaluation and Reliability Engine**

The problem statement identifies several important directions, including:

* Scenario Generation Engine
* Sandboxed Execution and Replay Harness
* Failure Mode Classifier
* Destructive Action Guardrail Tester
* Reliability Scorecard and Regression Tracker

The current prototype focuses primarily on **scenario generation, evaluation, failure classification, reliability scoring, and visualization**, while sandbox execution and advanced regression infrastructure are part of the planned roadmap.

---

# 📹 Demo Video

**Demo Video:**
`ADD_YOUR_VIDEO_LINK_HERE`

The demonstration should show:

```text
1. Agent Configuration
        ↓
2. Test Generation
        ↓
3. Evaluation
        ↓
4. Failure Detection
        ↓
5. Reliability Dashboard
        ↓
6. Failure Analysis
        ↓
7. Final Report
```

Maximum demo duration for Phase 1: **10 minutes**.

---

# 🌐 Live Prototype

**Live Demo:**
`ADD_YOUR_DEPLOYED_LINK_HERE`

---

# 👥 Team

### Team Name

`YOUR TEAM NAME`

| Member   | Role                    |
| -------- | ----------------------- |
| Member 1 | AI / ML                 |
| Member 2 | Backend / Evaluation    |
| Member 3 | Frontend / UI           |
| Member 4 | Testing / Documentation |

---

# 📄 License

This project was developed as a prototype for the **OOSC 4.0 Hackathon**.

---

# ⭐ Vision

> **AI agents are becoming more autonomous. AgentGuard AI helps developers understand whether they are reliable enough to trust.**

**Build better agents.
Test harder.
Deploy with confidence. 🛡️**