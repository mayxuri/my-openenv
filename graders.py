"""
Deterministic graders for each task.
All graders return (reward: float in [0,1], info: dict).
"""
from __future__ import annotations
from typing import Dict, Any, Tuple

PRIORITY_LEVELS = ["low", "medium", "high", "critical"]


def grade_classify(action: Dict[str, Any], answer: Dict[str, Any]) -> Tuple[float, Dict[str, Any]]:
    """
    Task 1 - Classify: reward = 1.0 for correct category, 0.0 otherwise.
    Partial credit (0.3) if submission is an adjacent, semantically related category.
    """
    submitted = (action.get("category") or "").lower().strip()
    correct = answer["category"]

    # Adjacent pairs that share some overlap
    adjacent: Dict[str, set] = {
        "billing": {"general"},
        "general": {"billing", "account"},
        "account": {"general", "technical"},
        "technical": {"account"},
    }

    if submitted == correct:
        reward = 1.0
        verdict = "correct"
    elif submitted in adjacent.get(correct, set()):
        reward = 0.3
        verdict = "adjacent"
    else:
        reward = 0.0
        verdict = "wrong"

    info = {
        "verdict": verdict,
        "submitted_category": submitted,
        "expected_category": correct,
    }
    return reward, info


def grade_route(action: Dict[str, Any], answer: Dict[str, Any]) -> Tuple[float, Dict[str, Any]]:
    """
    Task 2 - Route: weighted score across three dimensions.
      category  → 30%
      priority  → 40%  (adjacent priority gets 50% credit)
      team      → 30%
    """
    submitted_cat = (action.get("category") or "").lower().strip()
    submitted_pri = (action.get("priority") or "").lower().strip()
    submitted_team = (action.get("team") or "").lower().strip()

    correct_cat = answer["category"]
    correct_pri = answer["priority"]
    correct_team = answer["team"]

    # Category score
    cat_score = 1.0 if submitted_cat == correct_cat else 0.0

    # Priority score (partial credit for ±1 level)
    if submitted_pri == correct_pri:
        pri_score = 1.0
    elif submitted_pri in PRIORITY_LEVELS and correct_pri in PRIORITY_LEVELS:
        diff = abs(PRIORITY_LEVELS.index(submitted_pri) - PRIORITY_LEVELS.index(correct_pri))
        pri_score = 0.5 if diff == 1 else 0.0
    else:
        pri_score = 0.0

    # Team score
    team_score = 1.0 if submitted_team == correct_team else 0.0

    reward = round(cat_score * 0.30 + pri_score * 0.40 + team_score * 0.30, 4)

    info = {
        "category_score": cat_score,
        "priority_score": pri_score,
        "team_score": team_score,
        "total_reward": reward,
        "submitted": {
            "category": submitted_cat,
            "priority": submitted_pri,
            "team": submitted_team,
        },
        "expected": {
            "category": correct_cat,
            "priority": correct_pri,
            "team": correct_team,
        },
    }
    return reward, info


def grade_respond(
    action: Dict[str, Any],
    answer: Dict[str, Any],
    ticket: Dict[str, Any],
) -> Tuple[float, Dict[str, Any]]:
    """
    Task 3 - Respond: rubric-based deterministic scoring.

    Rubric (sums to 1.0):
      - Customer name present          : 0.15
      - Required words present         : 0.20   (partial)
      - Issue keywords addressed       : 0.25   (partial)
      - Resolution phrases present     : 0.25   (partial, need ≥50%)
      - Appropriate length             : 0.15
    """
    response_text = (action.get("response_text") or "").strip()
    response_lower = response_text.lower()

    if not response_text:
        return 0.0, {"error": "No response_text provided"}

    breakdown: Dict[str, float] = {}

    # 1. Customer name (0.15)
    customer_words = ticket["customer_name"].lower().split()
    name_hit = any(w in response_lower for w in customer_words)
    breakdown["name_mentioned"] = 0.15 if name_hit else 0.0

    # 2. Required words (0.20) - partial by fraction
    must_words = answer.get("must_include_words", [])
    if must_words:
        hits = sum(1 for w in must_words if w in response_lower)
        breakdown["key_words"] = round(0.20 * (hits / len(must_words)), 4)
    else:
        breakdown["key_words"] = 0.20

    # 3. Issue keywords addressed (0.25) - partial by fraction
    issue_kws = answer.get("issue_keywords", [])
    if issue_kws:
        hits = sum(1 for kw in issue_kws if kw in response_lower)
        breakdown["issue_addressed"] = round(0.25 * (hits / len(issue_kws)), 4)
    else:
        breakdown["issue_addressed"] = 0.25

    # 4. Resolution phrases (0.25) - need at least 50% of phrases
    res_phrases = answer.get("resolution_phrases", [])
    if res_phrases:
        hits = sum(1 for ph in res_phrases if ph in response_lower)
        fraction = hits / len(res_phrases)
        # Scale: 0% hits → 0.0, 50% hits → 0.125, 100% hits → 0.25
        breakdown["resolution_provided"] = round(0.25 * min(1.0, fraction / 0.5) * 0.5
                                                 + 0.25 * min(1.0, fraction) * 0.5, 4)
    else:
        breakdown["resolution_provided"] = 0.25

    # 5. Length (0.15): penalise too short or too long
    word_count = len(response_text.split())
    min_w = answer.get("min_words", 60)
    max_w = answer.get("max_words", 500)

    if min_w <= word_count <= max_w:
        length_score = 0.15
    elif word_count < min_w:
        length_score = round(0.15 * (word_count / min_w), 4)
    else:
        # Exponential decay for very long responses
        length_score = round(0.15 * max(0.0, 1.0 - (word_count - max_w) / max_w), 4)

    breakdown["length_appropriate"] = length_score

    total = round(sum(breakdown.values()), 4)
    total = min(1.0, max(0.0, total))

    return total, {
        "total_reward": total,
        "breakdown": breakdown,
        "word_count": word_count,
    }
