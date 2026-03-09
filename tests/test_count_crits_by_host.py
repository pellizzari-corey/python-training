from src.count_crits_by_host import *

run_cases = [
    (
        [
            "host=web-1 severity=CRITICAL vuln=CVE-2024-0001",
            "host=db-1 severity=HIGH vuln=CVE-2024-0002",
            "vuln=CVE-2024-0003 severity=CRITICAL host=web-1",
            "severity=CRITICAL host=api-2 vuln=CVE-2024-0004",
        ],
        {"web-1": 2, "api-2": 1},
    ),
    (
        [
            "host=mail-1 severity=LOW vuln=CVE-1",
            "host=mail-1 severity=MEDIUM vuln=CVE-2",
            "host=mail-2 severity=CRITICAL vuln=CVE-3",
        ],
        {"mail-2": 1},
    ),
    (
        [
            "severity=CRITICAL host=jump-1 vuln=CVE-10",
            "host=jump-1 vuln=CVE-11 severity=CRITICAL",
            "host=jump-2 severity=CRITICAL vuln=CVE-12",
        ],
        {"jump-1": 2, "jump-2": 1},
    ),
]

submit_cases = run_cases + [
    (
        [
            "host=web-1 vuln=CVE-1",
            "severity=CRITICAL vuln=CVE-2",
            "host=db-1 severity=HIGH vuln=CVE-3",
            "note=missing_fields",
        ],
        {},
    ),
    (
        [
            "severity=CRITICAL host=auth-1 vuln=CVE-100",
            "severity=LOW host=auth-1 vuln=CVE-101",
            "host=auth-2 severity=CRITICAL vuln=CVE-102",
            "host=auth-1 severity=CRITICAL vuln=CVE-103",
            "vuln=CVE-104 host=auth-2 severity=CRITICAL",
            "host=auth-3 severity=MEDIUM vuln=CVE-105",
        ],
        {"auth-1": 2, "auth-2": 2},
    ),
]


def format_lines(lines):
    output = ""
    for line in lines:
        output += f"  - {line}\n"
    return output


def test(scan_lines, expected_output):
    print("---------------------------------")
    print("Input:")
    print(format_lines(scan_lines), end="")
    print("")
    result = count_critical_by_host(scan_lines)
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
