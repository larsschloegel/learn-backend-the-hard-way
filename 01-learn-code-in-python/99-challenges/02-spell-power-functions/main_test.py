from main import *

run_cases = [
    (1, 5, 3, 10),
    (4, 10, 6, 24),
]

submit_cases = run_cases + [
    (2, 0, 5, 9),     # base: 2*2 + 0 = 4, total: 4 + 5 = 9
    (5, 5, 0, 15),    # base: 5*2 + 5 = 15, total: 15 + 0 = 15
    (7, 3, 10, 27),   # base: 7*2 + 3 = 17, total: 17 + 10 = 27
    (10, 0, 0, 20),   # base: 10*2 + 0 = 20, total: 20 + 0 = 20
]


def test(level, magic, element_power, expected_output):
    print("---------------------------------")
    print("Input:")
    print(f"  level:         {level}")
    print(f"  magic:         {magic}")
    print(f"  element_power: {element_power}")
    result = cast_spell(level, magic, element_power)
    print("")
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
