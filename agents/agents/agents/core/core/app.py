#MAIN ARCHESTRATOR (AGENTIC FLOW)
from agents.planner_agent import PlannerAgent
from agents.test_generator_agent import TestGeneratorAgent
from agents.failure_analyzer_agent import FailureAnalyzerAgent
from core.api_parser import load_openapi
from core.test_executor import TestExecutor

api_spec = load_openapi("samples/openapi.yaml")

plan = PlannerAgent().plan(api_spec)
tests = TestGeneratorAgent().generate_tests(plan)

with open("tests/generated_tests/test_api.py", "w") as f:
    f.write(tests)

success, logs = TestExecutor().run()

if not success:
    analysis = FailureAnalyzerAgent().analyze(logs)
    print("Test Failure Detected")
    print("Root Cause:", analysis)
else:
    print("All tests passed successfully")
