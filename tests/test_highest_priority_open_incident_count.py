from src.highest_priority_open_incident_count import highest_priority_open_incident_count


run_cases = [
    (
        [
            {"number": "INC001", "priority": "P1", "state": "New"},
            {"number": "INC002", "priority": "P2", "state": "In Progress"},
            {"number": "INC003", "priority": "P1", "state": "Resolved"},
            {"number": "INC004", "priority": "P1", "state": "New"},
            {"number": "INC005", "priority": "P2", "state": "New"},
        ],
        ("P1", 2),
    ),
    (
        [
            {"number": "INC006", "priority": "P3", "state": "Closed"},
            {"number": "INC007", "priority": "P2", "state": "Resolved"},
        ],
        (None, 0),
    ),
    (
        [
            {"number": "INC008", "priority": "P1", "state": "In Progress"},
            {"number": "INC009", "priority": "P1", "state": "In Progress"},
            {"number": "INC010", "priority": "P2", "state": "New"},
        ],
        ("P1", 2),
    ),
]

submit_cases = run_cases + [
    (
        [],
        (None, 0),
    ),
    (
        [
            {"number": "INC011", "priority": "", "state": "New"},
            {"number": "INC012", "priority": "P1", "state": ""},
            {"number": "INC013", "state": "New"},
            {"number": "INC014", "priority": "P2"},
        ],
        (None, 0),
    ),
    (
        [
            {"number": "INC015", "priority": "P1", "state": "Resolved"},
            {"number": "INC016", "priority": "P1", "state": "New"},
            {"number": "INC017", "priority": "P2", "state": "Closed"},
            {"number": "INC018", "priority": "P2", "state": "In Progress"},
            {"number": "INC019", "priority": "P3", "state": "New"},
            {"number": "INC020", "priority": "P3", "state": "Resolved"},
        ],
        ("P1", 1),
    ),
    (
        [
            {"number": "INC021", "priority": "P2", "state": "New"},
            {"number": "INC022", "priority": "P2", "state": "New"},
            {"number": "INC023", "priority": "P1", "state": "In Progress"},
            {"number": "INC024", "priority": "P1", "state": "In Progress"},
        ],
        ("P1", 2),
    ),
    (
        [
            {"number": "INC025", "priority": "P3", "state": "New"},
            {"number": "INC026", "priority": "P3", "state": "New"},
            {"number": "INC027", "priority": "P2", "state": "In Progress"},
            {"number": "INC028", "priority": "P2", "state": "In Progress"},
            {"number": "INC029", "priority": "P1", "state": "New"},
            {"number": "INC030", "priority": "P1", "state": "Resolved"},
        ],
        ("P2", 2),
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
    result = highest_priority_open_incident_count(input1)
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