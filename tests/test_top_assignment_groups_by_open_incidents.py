from src.top_assignment_groups_by_open_incidents import top_assignment_groups_by_open_incidents


run_cases = [
    (
        [
            {"number": "INC001", "assignment_group": "Network", "state": "New"},
            {"number": "INC002", "assignment_group": "Service Desk", "state": "In Progress"},
            {"number": "INC003", "assignment_group": "Network", "state": "Resolved"},
            {"number": "INC004", "assignment_group": "Network", "state": "New"},
            {"number": "INC005", "assignment_group": "Security", "state": "New"}
        ],
        [
            ("Network", 2),
            ("Service Desk", 1),
            ("Security", 1)
        ]
    ),
]

submit_cases = run_cases + [
    (
        [],
        []
    ),
    (
        [
            {"number": "INC010", "assignment_group": "Network", "state": "New"},
            {"number": "INC011", "assignment_group": "Network", "state": "In Progress"},
            {"number": "INC012", "assignment_group": "Database", "state": "New"},
            {"number": "INC013", "assignment_group": "Database", "state": "Resolved"},
            {"number": "INC014", "assignment_group": "Security", "state": "New"},
            {"number": "INC015", "assignment_group": "Security", "state": "New"},
        ],
        [
            ("Network", 2),
            ("Security", 2),
            ("Database", 1)
        ]
    ),
]


def format_incidents(incidents):
    if len(incidents) == 0:
        return "  (empty list)"

    output = ""
    for incident in incidents:
        output += f"  - {incident}\n"
    return output.rstrip()


def run_test(input1, expected_output):
    print("---------------------------------")
    print("Input:")
    print(format_incidents(input1))
    print("")
    result = top_assignment_groups_by_open_incidents(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0

    for test_case in test_cases:
        correct = run_test(*test_case)
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

    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
main()