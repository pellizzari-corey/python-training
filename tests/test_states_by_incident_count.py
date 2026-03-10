from src.states_by_incident_count import states_by_incident_count


run_cases = [
    (
        [
            {"number": "INC001", "state": "New"},
            {"number": "INC002", "state": "In Progress"},
            {"number": "INC003", "state": "Resolved"},
            {"number": "INC004", "state": "New"},
            {"number": "INC005", "state": "Closed"},
            {"number": "INC006", "state": "New"},
        ],
        [
            ("New", 3),
            ("In Progress", 1),
            ("Resolved", 1),
            ("Closed", 1),
        ],
    ),
    (
        [
            {"number": "INC007", "state": "New"},
            {"number": "INC008", "state": "New"},
            {"number": "INC009", "state": "New"},
        ],
        [
            ("New", 3),
        ],
    ),
    (
        [
            {"number": "INC010", "state": ""},
            {"number": "INC011"},
            {"number": "INC012", "state": None},
        ],
        [],
    ),
]

submit_cases = run_cases + [
    (
        [],
        [],
    ),
    (
        [
            {"number": "INC013", "state": "Closed"},
            {"number": "INC014", "state": "Closed"},
            {"number": "INC015", "state": "Resolved"},
            {"number": "INC016", "state": "Resolved"},
            {"number": "INC017", "state": "Resolved"},
        ],
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


def run_test(input1, expected_output):
    print("---------------------------------")
    print("Input:")
    print(format_incidents(input1))
    print("")
    result = states_by_incident_count(input1)
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