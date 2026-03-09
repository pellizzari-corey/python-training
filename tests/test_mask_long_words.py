from src.mask_long_words import *

run_cases = [
    (
        ["apple banana fig", "small words only"],
        ["apple * fig", "small words only"],
    ),
    (
        ["python coding is fun", "write clean simple code"],
        ["* * is fun", "write clean * code"],
    ),
    (
        ["short test", "hello world"],
        ["short test", "hello world"],
    ),
]

submit_cases = run_cases + [
    (
        ["", "tiny words"],
        ["", "tiny words"],
    ),
    (
        ["network security scanner", "logs stay clear"],
        ["* * *", "logs stay clear"],
    ),
    (
        ["alpha beta gamma delta epsilon zeta"],
        ["alpha beta gamma delta * zeta"],
    ),
]


def format_sentences(sentences):
    if sentences is None:
        return "  None"

    if type(sentences) != list:
        return f"  {sentences}"

    if len(sentences) == 0:
        return "  (empty list)"

    lines = []
    for sentence in sentences:
        lines.append(f'  - "{sentence}"')
    return "\n".join(lines)


def test(input1, expected_output):
    print("---------------------------------")
    print("Input:")
    print(format_sentences(input1))
    print("")
    result = mask_long_words(input1)
    print("Expected:")
    print(format_sentences(expected_output))
    print("Actual:")
    print(format_sentences(result))
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
