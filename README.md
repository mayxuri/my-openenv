# Customer Support OpenEnv

A **real-world OpenEnv environment** for training and evaluating AI agents on customer support ticket management — one of the most ubiquitous knowledge-work tasks at scale.

Agents must handle three tasks of increasing difficulty: classifying tickets, routing them to the correct team with appropriate priority, and drafting complete professional responses.

---

## Environment Description

Customer support teams handle thousands of tickets daily. Efficient triage, routing, and response require understanding context, urgency, and tone simultaneously. This environment simulates that workflow with realistic synthetic tickets across four categories: **billing**, **technical**, **account**, and **general**.

### Why this domain?
- Immediately applicable: every software company runs a support queue
- Rich, graded signal: partial credit rewards incremental improvement
- Genuine difficulty curve: classification → routing → open-ended generation
- Fully deterministic graders: reproducible scores with no LLM-as-judge

---

## Tasks

| Task | Difficulty | Max Steps | Description |
|------|-----------|-----------|-------------|
| `classify` | Easy | 3 | Classify ticket into billing / technical / account / general |
| `route` | Medium | 5 | Determine category + priority + team assignment |
| `respond` | Hard | 5 | Draft a complete, professional customer response |

### Task 1 — `classify` (Easy)
**Goal:** Identify the correct category for an incoming ticket.  
**Reward:** `1.0` exact match · `0.3` adjacent category · `0.0` wrong  
**Expected baseline score:** ~0.85

### Task 2 — `route` (Medium)
**Goal:** Set category (30%), priority (40%), and team (30%) simultaneously.  
Priority: `low | medium | high | critical` — adjacent priority gets 50% credit.  
Team: `billing_team | technical_team | account_team | customer_success`  
**Reward:** Weighted sum of three components (0.0–1.0)  
**Expected baseline score:** ~0.65

### Task 3 — `respond` (Hard)
**Goal:** Draft a professional, empathetic customer support response.  
**Rubric (deterministic keyword + length check):**

| Criterion | Weight |
|-----------|--------|
| Customer name mentioned | 0.15 |
| Required words present | 0.20 |
| Issue keywords addressed | 0.25 |
| Resolution phrases present | 0.25 |
| Appropriate length (60–500 words) | 0.15 |

**Expected baseline score:** ~0.55

---

## Observation Space

```json
{
  "ticket": {
    "ticket_id": "T001",
    "subject": "Can't login to my account",
    "body": "...",
    "customer_name": "Alice Johnson",
    "account_type": "pro",
    "created_at": "2024-01-15T10:30:00Z",
    "previous_tickets": []
  },
  "task_name": "classify",
  "task_description": "...",
  "available_action_types": ["submit", "ask_clarification"],
  "step_count": 0,
  "max_steps": 3,
  "feedback": null,
  "cumulative_reward": 0.0
}
```

## Action Space

```json
{
  "action_type": "submit",
  "category": "account",
  "priority": "high",
  "team": "account_team",
  "response_text": "Dear Alice, ...",
  "reasoning": "Login issue → account category"
}
```

| Field | Values | Required for |
|-------|--------|-------------|
| `action_type` | `submit` \| `ask_clarification` | always |
| `category` | `billing` \| `technical` \| `account` \| `general` | classify, route |
| `priority` | `low` \| `medium` \| `high` \| `critical` | route |
| `team` | `billing_team` \| `technical_team` \| `account_team` \| `customer_success` | route |
| `response_text` | string (60–500 words) | respond |
| `reasoning` | string | optional |

---

## Reward Function

```
reward = grader_score − (max(0, steps_taken − 1) × 0.03)
reward = clamp(reward, 0.0, 1.0)
```

- **Partial progress:** graders give fractional scores across multiple dimensions
- **Efficiency incentive:** a 3% penalty per extra step encourages single-shot solutions
- **No sparse rewards:** every submission produces a meaningful signal in [0, 1]

---

## Setup & Usage

### Run with Docker

```bash
docker build -t customer-support-env .
docker run -p 7860:7860 customer-support-env
```

### Run locally (dev)

```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 7860 --reload
```

### API Quick Start

```bash
# Reset an episode
curl -X POST http://localhost:7860/reset \
  -H "Content-Type: application/json" \
  -d '{"task_name": "classify", "seed": 42}'

# Take a step (use session_id from reset response)
curl -X POST http://localhost:7860/step/<session_id> \
  -H "Content-Type: application/json" \
  -d '{"action_type": "submit", "category": "technical"}'

# Inspect state
curl http://localhost:7860/state/<session_id>
```

### Run the Baseline Inference Script

```bash
export API_BASE_URL="https://api.openai.com/v1"
export MODEL_NAME="gpt-4o-mini"
export HF_TOKEN="sk-..."
export ENV_BASE_URL="http://localhost:7860"

python inference.py
```

The script will start the environment (or connect to a running instance), run all three tasks, and print structured `[START]` / `[STEP]` / `[END]` logs followed by a score summary.

---

## Baseline Scores (gpt-4o-mini, seed=42)

| Task | Score | Steps | Success |
|------|-------|-------|---------|
| classify | 1.00 | 1 | true |
| route | 0.67 | 1 | true |
| respond | 0.58 | 1 | true |
| **Average** | **0.75** | | |

---

## Project Structure

```
openenv-customer-support/
├── app.py            FastAPI server (OpenEnv HTTP API)
├── environment.py    Core environment logic (reset/step/state)
├── models.py         Pydantic models (Observation, Action, Reward, …)
├── data.py           Synthetic ticket dataset with ground-truth answers
├── graders.py        Deterministic graders for all three tasks
├── inference.py      Baseline agent using OpenAI client
├── openenv.yaml      OpenEnv metadata specification
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## OpenEnv Spec Compliance

- Typed `Observation`, `Action`, `Reward` Pydantic models ✓
- `reset()` → clean initial observation ✓
- `step(action)` → observation, reward ∈ [0,1], done, info ✓
- `state()` → current episode state ✓
- `openenv.yaml` with full metadata ✓
- Deterministic graders (same input → same score) ✓
- 3+ tasks with easy → medium → hard difficulty ✓
- Working Dockerfile ✓
