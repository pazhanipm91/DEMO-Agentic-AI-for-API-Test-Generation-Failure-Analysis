import subprocess

class TestExecutor:
    def run(self):
        result = subprocess.run(
            ["pytest", "tests/generated_tests"],
            capture_output=True,
            text=True
        )
        return result.returncode == 0, result.stdout + result.stderr
