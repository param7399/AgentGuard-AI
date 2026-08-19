# AgentGuard AI — Demo Script

## OOSC 4.0 Hackathon — Problem Statement 4

### Project

**AgentGuard AI — AI Agent Reliability & Evaluation Platform**

### Recommended Demo Duration

**7–8 minutes**

> Keep the final video below the mandatory 10-minute limit.

---

## 1. 🎬 Introduction — 0:00–0:40

### Screen

Show the AgentGuard AI dashboard.

### Say

> "Hello everyone. We are presenting **AgentGuard AI**, an AI-powered reliability and evaluation platform for autonomous AI agents."

> "AI agents can fail because of hallucinations, unsafe actions, tool failures, ambiguous instructions, and goal drift."

> "AgentGuard helps developers discover these failures before deploying their agents into real-world workflows."

---

## 2. 🚨 Problem — 0:40–1:20

### Screen

Show the problem statement.

### Say

> "Traditional AI-agent testing often depends on manually written test prompts. This makes it difficult to discover failures that only appear under unexpected or adversarial conditions."

> "For example, what happens when a tool fails? What happens when the user provides incomplete information? Or when someone tries to bypass the agent's safety constraints?"

> "Our challenge is to build an AI-powered platform that automatically generates realistic and adversarial test scenarios, evaluates agents, classifies failures, and produces a reliability report."

The selected problem statement specifically highlights scenario generation, sandboxed execution and replay, failure classification, destructive-action testing, and reliability scorecards.

---

## 3. 💡 Solution — 1:20–2:00

### Screen

Open the AgentGuard overview dashboard.

### Say

> "Our solution is **AgentGuard AI**."

> "A developer provides the agent's objective, system prompt, and available tools."

> "AgentGuard generates targeted test scenarios, evaluates the agent's behavior, identifies failure modes, calculates a reliability score, and provides actionable recommendations."

### Show

```text
Agent Configuration
        ↓
Scenario Generation
        ↓
Agent Evaluation
        ↓
Failure Detection
        ↓
Reliability Score
        ↓
Actionable Report
```

---

## 4. 🖥️ Dashboard — 2:00–2:45

### Screen

Open **Overview**.

Show:

* Reliability Score
* Tests Executed
* Passed Tests
* Failed Tests
* Critical Failures
* Reliability Trend
* Failure Distribution

### Say

> "This is our main reliability dashboard."

> "The top metrics give developers an immediate view of the agent's current health."

> "The reliability trend shows how performance changes across evaluation cycles, while the failure distribution helps identify recurring weaknesses."

---

## 5. 🧪 Test Lab — 2:45–4:00

### Screen

Open **Test Lab**.

Use:

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

Select:

```text
Normal
Adversarial
Safety
Tool Failure
```

### Say

> "Let's test a travel booking agent."

> "We provide its objective, system prompt, and available tools."

Click:

**⚡ Generate Reliability Tests**

### Say

> "AgentGuard now generates scenarios specifically for this agent."

Show examples such as:

```text
Incomplete booking information
Tool failure
Conflicting instructions
Safety constraint bypass
```

> "Each scenario contains a category, severity, scenario description, and expected behavior."

---

## 6. ⚡ Run Evaluation — 4:00–5:00

### Screen

Click:

**▶ Run Full Evaluation**

### Say

> "Now we run the generated test suite."

> "Each scenario is evaluated against the expected behavior of the agent."

Show:

```text
Passed
Failed
Score
Failure Type
Severity
```

### Say

> "AgentGuard goes beyond a simple pass-or-fail result."

> "It identifies the failure type, determines its severity, assigns a score, and provides a recommendation for improving the agent."

---

## 7. ⚠️ Failure Analysis — 5:00–6:00

### Screen

Open **Failure Analysis**.

Select a failed test.

Show:

```text
Failure Type:
Tool Failure

Severity:
HIGH

Score:
51/100
```

### Say

> "Let's inspect one of the detected failures."

> "In this scenario, the external tool fails, but the agent incorrectly claims that the operation was successful."

> "AgentGuard identifies this as a high-severity tool failure."

Show the recommendation.

### Say

> "The recommended improvement is to require explicit tool confirmation before the agent reports successful execution."

> "This turns a raw failure into actionable engineering feedback."

---

## 8. 📊 Reliability Score — 6:00–6:40

### Screen

Return to **Overview**.

Show the reliability gauge.

### Say

> "Individual test results are summarized into an overall reliability score from zero to one hundred."

Example:

```text
87 / 100
```

Show:

```text
90–100 → Excellent
75–89  → Good
50–74  → Needs Improvement
0–49   → Critical
```

### Say

> "This gives developers a simple high-level measure of agent health while still allowing them to investigate individual failures."

---

## 9. 📋 Reports — 6:40–7:15

### Screen

Open **Reports**.

Show:

* Complete test table
* Test categories
* Pass/fail status
* Failure type
* Severity
* Score
* CSV export

### Say

> "AgentGuard also provides a complete evaluation report."

> "Developers can inspect individual test results and export the evaluation data as a CSV file for further analysis."

---

## 10. 🚀 Future Scope — 7:15–7:50

### Screen

Show the architecture/future roadmap.

### Say

> "The current MVP focuses on scenario generation, evaluation, failure classification, reliability scoring, dashboard visualization, and reporting."

> "Our next step is to turn AgentGuard into a complete AI-agent reliability infrastructure."

Show:

```text
Current MVP
     ↓
Sandboxed Agent Execution
     ↓
Mock Tool Environment
     ↓
Execution Trace Capture
     ↓
Deterministic Replay
     ↓
Regression Testing
     ↓
CI/CD Integration
```

> "These extensions align with the broader directions of the selected problem statement, including sandboxed execution, replay, guardrail testing, and reliability tracking."

---

## 11. 🏆 Closing — 7:50–8:15

### Screen

Return to the AgentGuard dashboard.

### Say

> "AI agents should not only be capable — they should also be reliable."

> "AgentGuard AI gives developers a structured way to test difficult scenarios, identify failures, measure reliability, and improve agent behavior before deployment."

> "Our vision is simple: **Test harder. Understand failures. Deploy with confidence.**"

> "Thank you."

---

# 🎥 Recording Checklist

Before recording:

* [ ] Close unnecessary applications and browser tabs
* [ ] Use a clean desktop
* [ ] Verify AgentGuard starts without errors
* [ ] Verify the Overview dashboard
* [ ] Verify Test Lab
* [ ] Generate test scenarios
* [ ] Run evaluation
* [ ] Open Failure Analysis
* [ ] Open Reports
* [ ] Test CSV download
* [ ] Remove personal information
* [ ] Ensure API keys are never visible
* [ ] Record at 1080p if possible
* [ ] Keep the final video below 10 minutes
* [ ] Upload the video
* [ ] Add the video link to `README.md`

---

# 🎯 Recommended Presentation Flow

Do not spend most of the demo explaining the code.

Focus on the working product:

```text
Problem
   ↓
Solution
   ↓
Live Dashboard
   ↓
Configure Agent
   ↓
Generate Tests
   ↓
Run Evaluation
   ↓
Show Failure
   ↓
Explain Recommendation
   ↓
Reliability Score
   ↓
Future Vision
```

The judges should clearly understand:

1. **What problem AgentGuard solves**
2. **How the working prototype solves it**
3. **How the system evaluates agent reliability**
4. **What makes the solution scalable**
5. **How the prototype can evolve into a complete agent-testing platform**
