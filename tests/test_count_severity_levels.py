from src.count_severity_levels import *

run_cases = [
    (
        [
            "ERROR: Disk full",
            "INFO: User logged in",
            "ERROR: Connection lost",
        ],
        {"ERROR": 2, "INFO": 1},
    ),
    (
        [
            "WARNING: High memory usage",
            "WARNING: CPU spike",
            "WARNING: Network slowdown",
        ],
        {"WARNING": 3},
    ),
    (
        [
            "INFO: Start",
            "DEBUG: Loading config",
            "INFO: Ready",
            "DEBUG: Cache warm",
            "ERROR: Missing file",
        ],
        {"INFO": 2, "DEBUG": 2, "ERROR": 1},
    ),
]

submit_cases = run_cases + [
    (
        [],
        {},
    ),
    (
        [
            "CRITICAL: Database offline",
        ],
        {"CRITICAL": 1},
    ),
    (
        [
            "INFO: Boot",
            "INFO: Login",
            "WARNING: Slow response",
            "ERROR: Timeout",
            "INFO: Retry",
            "WARNING: High load",
            "ERROR: Timeout again",
            "INFO: Finished",
        ],
        {"INFO": 4, "WARNING": 2, "ERROR": 2},
    ),
]


def format_logs(logs):
    if len(logs) == 0:
        return "  (empty)"

    lines = []
    for log in logs:
        lines.append(f"  - {log}")
    return "\n".join(lines)



def test(logs, expected_output):
    print("---------------------------------")
    print("Input:")
    print(format_logs(logs))
    print("")
    result = count_severity_levels(logs)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False



def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")



test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
