from src.get_host_severity_counts import get_host_severity_counts

run_cases = [
    (
        [
            "host=web-1 severity=ERROR message=disk_full",
            "severity=INFO host=web-1 message=boot_complete",
            "host=db-1 severity=ERROR code=500",
        ],
        {
            "web-1": {"ERROR": 1, "INFO": 1},
            "db-1": {"ERROR": 1},
        },
    ),
    (
        [
            "severity=WARNING host=api-2",
            "host=api-2 severity=WARNING",
            "host=api-2 severity=ERROR",
        ],
        {
            "api-2": {"WARNING": 2, "ERROR": 1},
        },
    ),
]

submit_cases = run_cases + [
    (
        [
            "host=web-1 severity=ERROR",
            "host=web-1 message=missing_severity",
            "severity=INFO message=missing_host",
            "host=db-2 severity=INFO",
        ],
        {
            "web-1": {"ERROR": 1},
            "db-2": {"INFO": 1},
        },
    ),
    (
        [],
        {},
    ),
    (
        [
            "region=us host=web-3 severity=INFO user=alice",
            "host=web-3 severity=INFO",
            "severity=ERROR host=web-3 code=500",
            "host=db-9 severity=WARNING",
            "severity=WARNING host=db-9",
        ],
        {
            "web-3": {"INFO": 2, "ERROR": 1},
            "db-9": {"WARNING": 2},
        },
    ),
]


def format_lines(log_lines):
    if len(log_lines) == 0:
        return "  (empty)"

    output = ""
    for line in log_lines:
        output += f"  - {line}\n"
    return output.rstrip()


def test(log_lines, expected_output):
    print("---------------------------------")
    print("Input:")
    print(format_lines(log_lines))
    print("")
    result = get_host_severity_counts(log_lines)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
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
