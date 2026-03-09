from src.summarize_words import *

run_cases = [
    (["red apple", "big banana tree"], (5, "banana")),
    (["hello world", "python"], (3, "python")),
    (["one two", "", "three"], (3, "three")),
]

submit_cases = run_cases + [
    (["", "", ""], (0, "")),
    (["ant bee", "cat dog"], (4, "ant")),
    (["tiny", "medium size", "extraordinary word"], (5, "extraordinary")),
]


def format_lines(lines):
    if len(lines) == 0:
        return "  (empty list)"

    output = ""
    for line in lines:
        output += f'  - "{line}"\n'
    return output.rstrip()



def test(input1, expected_output):
    print("---------------------------------")
    print("Input:")
    print(format_lines(input1))
    print("")
    result = summarize_words(input1)
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
