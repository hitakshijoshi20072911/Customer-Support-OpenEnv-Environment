# Customer Support OpenEnv Environment

## Overview

Customer support automation is one of the most impactful applications of modern AI systems. Organizations across industries such as e-commerce, fintech, SaaS, and telecommunications handle thousands of user queries daily related to payments, account access, subscriptions, and order tracking.

This project implements a **Customer Support Simulation Environment built using the OpenEnv framework**, designed to evaluate how effectively AI agents can handle customer queries. The environment simulates real-world customer support tasks and evaluates the performance of automated agents using structured actions and reward-based feedback.

Instead of simply building an AI chatbot, this project focuses on **building the environment where AI agents operate**, allowing systematic benchmarking of different agent strategies.

The system enables evaluation of:

* Rule-based baseline agents
* Large Language Model (LLM) powered agents
* Future reinforcement learning agents

This makes the repository a **benchmarking framework for intelligent customer support systems**.

---

# Environment Design

The environment follows the **OpenEnv interaction pattern**, where an agent interacts with the environment using the following cycle:

Agent → Observation → Action → Environment → Reward → Next Observation

### Environment Workflow

1. A customer support query is presented as an observation.
2. The agent analyzes the query.
3. The agent selects a structured action.
4. The environment evaluates the action.
5. A reward score is assigned based on correctness.

This loop continues until the task is completed.

---

# Observation Space

Each observation contains the **customer support query** describing the user's problem.

Example:

```
"My payment failed but money was deducted."
```

The agent must interpret this query and determine the correct action.

---

# Action Space

Agents must output a structured action in the format:

```
category | priority | solution
```

Example:

```
payment | high | initiate refund
```

### Action Components

| Component | Description            |
| --------- | ---------------------- |
| Category  | Type of support issue  |
| Priority  | Urgency of the request |
| Solution  | Suggested resolution   |

---

# Task Dataset

The environment includes a dataset of **10 simulated customer support tasks**, representing common real-world issues.

| Task Type          | Example                        |
| ------------------ | ------------------------------ |
| Payment Issues     | Refund or failed transactions  |
| Account Management | Password reset or login issues |
| Billing            | Subscription changes           |
| Order Tracking     | Delivery related queries       |
| Technical Support  | System or platform errors      |

These tasks simulate realistic support interactions seen in modern digital platforms.

---

# Reward System

The environment evaluates the correctness of the agent's response using a reward-based scoring mechanism.

Typical evaluation factors include:

* Correct issue classification
* Correct priority level
* Correct resolution

Example reward distribution:

| Evaluation Component | Reward |
| -------------------- | ------ |
| Correct category     | +0.4   |
| Correct priority     | +0.3   |
| Correct solution     | +0.3   |

Total possible reward per task: **1.0**

This reward system allows **quantitative benchmarking of AI support agents**.

---

# Baseline Agent

To establish a performance reference, the project includes a **rule-based baseline agent**.

The baseline agent uses simple keyword heuristics to classify queries and generate structured actions.

Example logic:

```
If query contains "refund" → payment issue
If query contains "password" → account issue
If query contains "subscription" → billing issue
```

This baseline allows comparison between:

* Simple rule-based systems
* LLM-powered agents
* Future reinforcement learning agents

---

# Benchmarking System

The repository includes a **benchmark evaluation pipeline** to measure agent performance across all tasks.

The benchmark runner:

1. Loads all tasks
2. Runs the agent on each task
3. Collects rewards
4. Computes performance metrics

Example output:

```
Agent Performance Report
---------------------------
Tasks evaluated: 10
Average reward: 0.32
Category accuracy: 0.50
Priority accuracy: 0.40
```

These metrics allow comparison between different agent architectures.

---

# Project Structure

```
Customer-Support-OpenEnv-Environment
│
├── agents
│   ├── baseline_agent.py
│   └── llm_agent.py
│
├── env
│   ├── environment.py
│   ├── tasks.py
│   ├── models.py
│   └── grader.py
│
├── evaluation
│   ├── benchmark.py
│   └── metrics.py
│
├── inference.py
├── test_env.py
├── requirements.txt
├── openenv.yaml
└── Dockerfile
```

### Folder Explanation

**env/**
Contains the OpenEnv environment implementation, task definitions, and reward grading logic.

**agents/**
Contains agent implementations including baseline rule-based agents and LLM-powered agents.

**evaluation/**
Provides benchmarking utilities to measure agent performance.

---

# Real-World Applications

This system can be applied to several real-world scenarios:

### AI Customer Support Assistants

Evaluate automated support agents before deploying them in production.

### Model Benchmarking

Compare different LLMs or AI agents on structured support tasks.

### Reinforcement Learning Research

Use the environment as a training ground for RL agents learning customer support workflows.

### Smart Helpdesk Systems

Improve automated helpdesk routing and resolution strategies.

---

# Impact

AI-driven customer support systems can significantly improve operational efficiency.

Potential benefits include:

* Reduced response times
* Lower support operational costs
* Scalable support infrastructure
* Improved customer satisfaction

Benchmark environments like this help ensure **AI systems are reliable before deployment**.

---

# Current Features

✔ OpenEnv-compatible customer support environment
✔ Structured action space for AI agents
✔ Reward-based evaluation system
✔ Rule-based baseline agent
✔ Benchmark evaluation pipeline

---

# Planned Improvements (Future Work)

The following improvements are planned to expand the project:

### Multi-Agent Benchmarking

Compare performance of multiple agents including different LLM models.

### Intelligent Action Parsing

Convert natural language responses from LLMs into structured actions automatically.

### Task Difficulty System

Introduce difficulty levels (easy / medium / hard) for better benchmarking.

### Agent Leaderboard

Create a performance leaderboard comparing different agent architectures.

### Reinforcement Learning Integration

Train RL agents directly within the environment.

---

# Getting Started

### Install dependencies

```
pip install -r requirements.txt
```

### Run the benchmark

```
python -m evaluation.benchmark
```

This will evaluate the baseline agent across all customer support tasks.

---

# Repository

GitHub Repository:

https://github.com/hitakshijoshi20072911/Customer-Support-OpenEnv-Environment

---

# License

This project is intended for research and educational purposes.
