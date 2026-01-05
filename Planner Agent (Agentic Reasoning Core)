from typing import Dict, List

class PlannerAgent:
    """
    Agent responsible for deciding WHAT to test and HOW.
    """

    def plan(self, api_spec: Dict) -> Dict:
        plan = {
            "strategy": "risk_based",
            "endpoints": []
        }

        paths = api_spec.get("paths", {})

        for path, methods in paths.items():
            for method, details in methods.items():
                plan["endpoints"].append({
                    "path": path,
                    "method": method.upper(),
                    "tests": [
                        "happy_path",
                        "invalid_input",
                        "boundary_condition"
                    ],
                    "expected_status": details.get("responses", {}).keys()
                })

        return plan
