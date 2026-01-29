from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class ReviewFinding:
    agent: str
    summary: str
    timestamp: str


class ReviewAgent:
    def __init__(self, name: str, focus: str) -> None:
        self.name = name
        self.focus = focus

    def review(self, context: dict) -> ReviewFinding:
        summary = (
            f"{self.focus} 확인: 파일={context['filename']}, "
            f"슬라이드={context['slide_count']}, "
            f"언어={context['target_language']}"
        )
        return ReviewFinding(
            agent=self.name,
            summary=summary,
            timestamp=datetime.utcnow().isoformat(timespec="seconds"),
        )


class ReviewOrchestrator:
    def __init__(self, loop_count: int = 5) -> None:
        self.loop_count = max(loop_count, 5)
        self.agents = [
            ReviewAgent("정합성", "번역 품질"),
            ReviewAgent("형식", "PPT 서식"),
            ReviewAgent("안전", "로컬 파일 처리"),
        ]

    def run(self, context: dict) -> list[dict]:
        review_log: list[dict] = []
        for cycle in range(1, self.loop_count + 1):
            for agent in self.agents:
                finding = agent.review(context)
                review_log.append(
                    {
                        "cycle": cycle,
                        "agent": finding.agent,
                        "summary": finding.summary,
                        "timestamp": finding.timestamp,
                    }
                )
        return review_log
