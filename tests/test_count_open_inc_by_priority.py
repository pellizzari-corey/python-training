from src.count_open_inc_by_priority import count_open_incidents_by_priority


run_cases = [
    (
        [
            {"number": "INC001", "priority": "P1", "state": "New"},
            {"number": "INC002", "priority": "P2", "state": "In Progress"},
            {"number": "INC003", "priority": "P1", "state": "Resolved"},
            {"number": "INC004", "priority": "P1", "state": "New"},
        ],
        {
            "P1": 2,
            "P2": 1,
        },
    ),
    (
        [
            {"number": "INC005", "priority": "P3", "state": "Closed"},
            {"number": "INC006", "priority": "P2", "state": "Resolved"},
        ],
        {},
    ),
    (
        [
            {"number": "INC007", "priority": "P1", "state": "In Progress"},
            {"number": "INC008", "priority": "P1", "state": "In Progress"},
            {"number": "INC009", "priority": "P2", "state": "New"},
        ],
        {
            "P1": 2,
            "P2": 1,
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
            {"number": "INC010", "priority": "", "state": "New"},
            {"number": "INC011", "priority": "P1", "state": ""},
            {"number": "INC012", "state": "New"},
            {"number": "INC013", "priority": "P2"},
        ],
        {},
    ),
    (
        [
            {"number": "INC014", "priority": "P1", "state": "Resolved"},
            {"number": "INC015", "priority": "P1", "state": "New"},
            {"number": "INC016", "priority": "P2", "state": "Closed"},
            {"number": "INC017", "priority": "P2", "state": "In Progress"},
            {"number": "INC018", "priority": "P3", "state": "New"},
            {"number": "INC019", "priority": "P3", "state": "Resolved"},
        ],
        {
            "P1": 1,
            "P2": 1,
            "P3": 1,
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
    result = count_open_incidents_by_priority(input1)
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