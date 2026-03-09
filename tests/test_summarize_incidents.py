from src.summarize_incidents import summarize_incidents


run_cases = [
    (
        [
            {"number": "INC001", "assignment_group": "Network", "state": "New"},
            {"number": "INC002", "assignment_group": "Network", "state": "Resolved"},
            {"number": "INC003", "assignment_group": "Service Desk", "state": "In Progress"},
            {"number": "INC004", "assignment_group": "Network", "state": "New"},
        ],
        {
            "Network": {"New": 2, "Resolved": 1},
            "Service Desk": {"In Progress": 1},
        },
    ),
    (
        [
            {"number": "INC005", "assignment_group": "Database", "state": "New"},
            {"number": "INC006", "assignment_group": "Database", "state": "New"},
            {"number": "INC007", "assignment_group": "Database", "state": "In Progress"},
        ],
        {
            "Database": {"New": 2, "In Progress": 1},
        },
    ),
    (
        [
            {"number": "INC008", "assignment_group": "Security", "state": "Resolved"},
        ],
        {
            "Security": {"Resolved": 1},
        },
    ),
]

submit_cases = run_cases + [
    (
        [],
        {},
    ),
    (
        [
            {"number": "INC009", "assignment_group": "", "state": "New"},
            {"number": "INC010", "assignment_group": "Network", "state": ""},
            {"number": "INC011", "state": "Resolved"},
            {"number": "INC012", "assignment_group": "Service Desk"},
        ],
        {},
    ),
    (
        [
            {"number": "INC013", "assignment_group": "Service Desk", "state": "New"},
            {"number": "INC014", "assignment_group": "Service Desk", "state": "New"},
            {"number": "INC015", "assignment_group": "Service Desk", "state": "Resolved"},
            {"number": "INC016", "assignment_group": "Network", "state": "In Progress"},
            {"number": "INC017", "assignment_group": "Network", "state": "In Progress"},
            {"number": "INC018", "assignment_group": "Network", "state": "Resolved"},
        ],
        {
            "Service Desk": {"New": 2, "Resolved": 1},
            "Network": {"In Progress": 2, "Resolved": 1},
        },
    ),
    (
        [
            {"number": "INC019", "assignment_group": "Platform", "state": "New"},
            {"number": "INC020", "assignment_group": "Platform", "state": "New"},
            {"number": "INC021", "assignment_group": "Platform", "state": "New"},
            {"number": "INC022", "assignment_group": "Security", "state": "Resolved"},
            {"number": "INC023", "assignment_group": "Security", "state": "Resolved"},
            {"number": "INC024", "assignment_group": "Security", "state": "In Progress"},
            {"number": "INC025", "assignment_group": "", "state": "Resolved"},
            {"number": "INC026", "assignment_group": "Platform", "state": ""},
        ],
        {
            "Platform": {"New": 3},
            "Security": {"Resolved": 2, "In Progress": 1},
        },
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
    result = summarize_incidents(input1)
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

    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()