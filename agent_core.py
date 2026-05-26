"""PromptProof Agent CLI demo.
Run: python agent_core.py
This mirrors the browser MVP and writes a JSON evidence log.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path


@dataclass
class TokenPlan:
    users: int
    runs_per_user_per_day: int
    tokens_per_run: int
    daily_tokens: int
    monthly_tokens: int


@dataclass
class AgentRunLog:
    run_id: str
    project: str
    status: str
    created_at: str
    agents: list[str]
    quality_score: int
    token_plan: TokenPlan
    estimated_rework_reduction: str
    output_ready_for_screenshot: bool = True


def estimate_score(task: str) -> int:
    keywords = ["輸出", "格式", "語氣", "不要", "使用者", "產品", "流程", "Agent"]
    score = 48 + sum(6 for word in keywords if word in task)
    if len(task) > 80:
        score += 10
    return min(score, 96)


def run_agent(
    project: str,
    task: str,
    users: int = 10,
    runs_per_user_per_day: int = 20,
    input_tokens: int = 900,
    output_tokens: int = 1200,
) -> AgentRunLog:
    agents = [
        "Intake Agent",
        "Prompt Architect",
        "Risk Checker",
        "Token Planner",
        "Report Agent",
    ]
    tokens_per_run = input_tokens + output_tokens
    daily_tokens = users * runs_per_user_per_day * tokens_per_run
    monthly_tokens = daily_tokens * 30
    score = estimate_score(task)
    savings = max(18, min(42, math.floor((score - 45) * 0.82)))
    run_id = f"RUN-{datetime.now().strftime('%Y%m%d')}-CLI"
    return AgentRunLog(
        run_id=run_id,
        project=project,
        status="completed",
        created_at=datetime.now(timezone.utc).isoformat(),
        agents=agents,
        quality_score=score,
        token_plan=TokenPlan(
            users=users,
            runs_per_user_per_day=runs_per_user_per_day,
            tokens_per_run=tokens_per_run,
            daily_tokens=daily_tokens,
            monthly_tokens=monthly_tokens,
        ),
        estimated_rework_reduction=f"{savings}%",
    )


if __name__ == "__main__":
    demo_task = (
        "團隊在提交 AI 任務時，經常因需求描述不完整、輸出格式不清楚、"
        "Token 預算不可控，導致多輪返工。希望做一個 Agent，可以自動分析需求、"
        "重寫 Prompt、檢查缺漏、預估 Token，並輸出可截圖的執行日誌。"
    )
    log = run_agent("PromptProof Agent：提示詞品質評估與 Token 預算助手", demo_task)
    output_path = Path("evidence/demo-run-log-from-cli.json")
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(json.dumps(asdict(log), ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(asdict(log), ensure_ascii=False, indent=2))
