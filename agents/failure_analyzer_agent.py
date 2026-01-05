import re
from typing import Dict

class FailureAnalyzerAgent:
    """
    Agent that analyzes pytest failure logs and determines root cause.
    """

    FAILURE_PATTERNS = {
        "ASSERTION_ERROR": r"AssertionError",
        "TIMEOUT": r"TimeoutError",
        "SCHEMA_MISMATCH": r"KeyError|TypeError",
        "SERVER_ERROR": r"500|502|503",
        "CLIENT_ERROR": r"400|401|403|404"
    }

    def analyze(self, logs: str) -> Dict:
        analysis = {
            "failure_type": "UNKNOWN",
            "confidence": 0.4,
            "explanation": "Unable to classify failure",
            "recommended_action": "Manual investigation required"
        }

        for failure_type, pattern in self.FAILURE_PATTERNS.items():
            if re.search(pattern, logs):
                analysis.update({
                    "failure_type": failure_type,
                    "confidence": 0.85,
                    "explanation": f"Detected pattern matching {failure_type}",
                    "recommended_action": self._recommend_action(failure_type)
                })
                break

        return analysis

    def _recommend_action(self, failure_type: str) -> str:
        return {
            "ASSERTION_ERROR": "Update expected response or validate API regression",
            "TIMEOUT": "Investigate API latency or increase timeout threshold",
            "SCHEMA_MISMATCH": "Update test schema based on latest contract",
            "SERVER_ERROR": "Raise bug to backend team",
            "CLIENT_ERROR": "Validate request payload generation logic"
        }.get(failure_type, "Investigate logs manually")
