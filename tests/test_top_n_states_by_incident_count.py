from src.top_n_states_by_incident_count import top_n_states_by_incident_count


run_cases = [
    (
        [
            {"number": "INC001", "state": "New"},
            {"number": "INC002", "state": "In Progress"},
            {"number": "INC003", "state": "Resolved"},
            {"number": "INC004", "state": "New"},
            {"number": "INC005", "state": "Closed"},
            {"number": "INC006", "state": "New"},
            {"number": "INC007", "state": "Resolved"},
        ],
        2,
        [
            ("New", 3),
            ("Resolved", 2),
        ],
    ),
    (
        [
            {"number": "INC010", "state": "New"},
            {"number": "INC011", "state": "New"},
            {"number": "INC012", "state": "Resolved"},
        ],
        1,
        [
            ("New", 2),
        ],
    ),
]

submit_cases = run_cases + [
    (
        [],
        3,
        [],
    ),
    (
        [
            {"number": "INC013", "state": ""},
            {"number": "INC014"},
            {"number": "INC015", "state": None},
        ],
        2,
        [],
    ),
    (
        [
            {"number": "INC016", "state": "Closed"},
            {"number": "INC017", "state": "Closed"},
            {"number": "INC018", "state": "Resolved"},
            {"number": "INC019", "state": "Resolved"},
            {"number": "INC020", "state": "Resolved"},
        ],
        3,
        [
            ("Resolved", 3),
            ("Closed", 2),
        ],
    ),
]


def format_incidents(incidents):
    if len(incidents) == 0:
        return "  (empty list)"

    output = ""
    for incident in incidents:
        output += f"  - {incident}\n"
    return output.rstrip()


def run_test(input1, n, expected_output):
    print("---------------------------------")
    print("Input:")
    print(format_incidents(input1))
    print(f"\nTop N: {n}")

    result = top_n_states_by_incident_count(input1, n)

    print(f"\nExpected: {expected_output}")
    print(f"Actual:   {result}")

    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0

    for test_case in submit_cases:
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


main()