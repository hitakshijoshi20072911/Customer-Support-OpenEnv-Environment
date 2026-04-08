# Customer Support OpenEnv Environment

## Overview

This project implements a **customer support simulation environment** designed for evaluating Large Language Model (LLM) agents using the **OpenEnv benchmarking framework**.

The environment models realistic customer support workflows where an AI agent must analyze user queries and determine appropriate actions to resolve issues. Each interaction is evaluated through a **programmatic grading system** that provides incremental rewards based on the correctness of the agent’s decision.

The system enables benchmarking of LLM-based agents on structured problem-solving tasks commonly encountered in production support systems.

---

# Motivation

Customer support automation is a major area of applied AI. Large organizations process millions of customer requests daily, including:

* payment failures
* refund requests
* account recovery
* order tracking
* subscription management
* technical troubleshooting

Traditional rule-based chatbots struggle with the complexity and variability of real user queries.

Recent advances in **Large Language Models and agent-based systems** allow AI agents to reason about customer issues and autonomously determine resolution strategies.

This project creates a **controlled evaluation environment** to measure how effectively AI agents can perform these tasks.

---

# Environment Architecture

The system follows the **OpenEnv environment interface**, which mirrors reinforcement learning environments used in modern AI research.

Core components include:

```
env/
 ├ models.py        → Pydantic schemas for observations and actions
 ├ tasks.py         → dataset of support tasks
 ├ grader.py        → scoring and reward logic
 └ environment.py   → OpenEnv environment implementation
```

An **inference agent** interacts with the environment and produces actions based on the current observation.

```
inference.py
```

This script runs the agent against the environment and outputs evaluation results in a structured format required by the OpenEnv evaluation pipeline.

---

# OpenEnv Interface

The environment implements the required OpenEnv methods:

### reset()

Initializes the environment and returns the first observation.

```
observation = env.reset()
```

### step(action)

Executes an agent action and returns:

```
observation, reward, done, info
```

* **observation** → next environment state
* **reward** → score from 0.0 to 1.0
* **done** → indicates task completion
* **info** → metadata about evaluation

### state()

Returns the current internal state of the environment.

---

# Observation Space

Each observation represents a customer support request.

Example:

```
{
  "query": "My payment failed but money was deducted."
}
```

The agent must interpret the request and decide the correct action.

Observation features include:

* customer query text
* conversation context
* environment state

---

# Action Space

The agent outputs structured actions representing a support resolution strategy.

Format:

```
category | priority | resolution
```

Example:

```
payment | high | initiate refund
```

Components:

| Field      | Description          |
| ---------- | -------------------- |
| category   | issue classification |
| priority   | urgency level        |
| resolution | recommended action   |

---

# Task Dataset

The environment includes a dataset of customer support tasks representing realistic service scenarios.

| Task                      | Difficulty |
| ------------------------- | ---------- |
| Refund request            | Easy       |
| Password reset            | Medium     |
| Subscription cancellation | Medium     |
| Order tracking            | Medium     |
| Duplicate payment         | Hard       |

Each task defines:

* user query
* expected category
* correct resolution
* priority level

---

# Reward Function

The grading system evaluates actions using deterministic rules.

Rewards range from **0.0 to 1.0**.

Evaluation criteria include:

* correct issue classification
* appropriate priority level
* correct resolution strategy

Example scoring:

```
Correct category → +0.4
Correct priority → +0.3
Correct solution → +0.3
```

This design provides **incremental feedback** to guide agent behavior.

---

# Baseline Agent

The project includes a baseline inference agent using the **OpenAI API client**.

The agent interacts with the environment and attempts to resolve tasks using an LLM.

Baseline configuration:

```
Model: Meta-Llama-3-8B-Instruct
API: HuggingFace Router (OpenAI-compatible)
Tasks evaluated: 10
Average reward: ~0.14
```

The inference script outputs results in the format required by the OpenEnv evaluation system.

Example:

```
[START] task=support_task env=customer-support-env model=meta-llama/Meta-Llama-3-8B-Instruct
[STEP] step=1 action=payment|high|initiate refund reward=1.00 done=false error=null
[STEP] step=2 action=account|medium|reset password reward=0.80 done=false error=null
[END] success=true steps=2 rewards=1.00,0.80
```

---

# Deployment

The environment is containerized and deployable on **Hugging Face Spaces** using Docker.

Hardware constraints:

```
2 vCPU
8GB RAM
```

Deployment files:

```
Dockerfile
openenv.yaml
requirements.txt
```

---

# Setup

Install dependencies:

```
pip install -r requirements.txt
```

Set environment variables:

```
HF_TOKEN=your_token
API_BASE_URL=https://router.huggingface.co/v1
MODEL_NAME=meta-llama/Meta-Llama-3-8B-Instruct
```

Run the environment:

```
python inference.py
```

---

# Real-World Applications

This environment can be used to evaluate AI systems designed for:

* automated customer support agents
* enterprise helpdesk automation
* AI-powered service desks
* intelligent ticket triaging systems
* support workflow optimization

Organizations such as e-commerce platforms, fintech companies, and SaaS providers could leverage similar systems to reduce support costs while improving response quality.

---

# Societal Impact

AI-driven support automation has the potential to:

* reduce response times for customer issues
* provide 24/7 support availability
* reduce operational costs for businesses
* improve accessibility of services

However, responsible deployment is critical to ensure:

* fairness in automated decision-making
* accurate handling of sensitive customer data
* escalation to human agents when necessary

Benchmark environments such as this help ensure AI systems are **tested, measurable, and reliable before deployment**.

---

# Future Improvements

Planned extensions include:

* large-scale task datasets
* evaluation metrics and benchmarking tools
* multi-agent comparison frameworks
* leaderboard-based evaluation

These additions will transform the project into a **comprehensive research benchmark for support automation agents**.

---

# License

This project was developed for the **Meta OpenEnv Hackathon**.
