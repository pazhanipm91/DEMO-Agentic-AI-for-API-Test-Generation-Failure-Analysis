class TestGeneratorAgent:
    """
    Generates pytest-based API tests.
    """

    def generate_tests(self, plan: dict) -> str:
        test_code = [
            "import requests",
            "",
            "BASE_URL = 'http://localhost:8000'",
            ""
        ]

        for ep in plan["endpoints"]:
            test_name = f"test_{ep['method'].lower()}_{ep['path'].strip('/').replace('/', '_')}"
            test_code.append(f"def {test_name}():")
            test_code.append(
                f"    response = requests.{ep['method'].lower()}(BASE_URL + '{ep['path']}')"
            )
            test_code.append("    assert response.status_code < 500")
            test_code.append("")

        return "\n".join(test_code)
