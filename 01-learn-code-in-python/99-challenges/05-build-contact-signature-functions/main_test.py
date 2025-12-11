from main import *

run_cases = [
    ("Ada", "Lovelace", "555-0101", "ada@example.com",
     "Signature: Contact: Ada Lovelace | Phone: 555-0101 | Email: ada@example.com"),
    ("Luke", "Skywalker", "555-0001", "luke@rebels.org",
     "Signature: Contact: Luke Skywalker | Phone: 555-0001 | Email: luke@rebels.org"),
    ("Sam", "Wise", "123-4567", "sam@shire.net",
     "Signature: Contact: Sam Wise | Phone: 123-4567 | Email: sam@shire.net"),
]

submit_cases = run_cases + [
    ("Harry", "Potter", "111-2222", "harry@hogwarts.edu",
     "Signature: Contact: Harry Potter | Phone: 111-2222 | Email: harry@hogwarts.edu"),
    ("Leia", "Organa", "999-9999", "leia@alderaan.gov",
     "Signature: Contact: Leia Organa | Phone: 999-9999 | Email: leia@alderaan.gov"),
    ("Tony", "Stark", "800-IRONMAN", "tony@starkindustries.com",
     "Signature: Contact: Tony Stark | Phone: 800-IRONMAN | Email: tony@starkindustries.com"),
]


def test(first_name, last_name, phone_number, email, expected_output):
    print("---------------------------------")
    print("Input:")
    print(f"  first_name:   {first_name}")
    print(f"  last_name:    {last_name}")
    print(f"  phone_number: {phone_number}")
    print(f"  email:        {email}")
    result = build_signature(first_name, last_name, phone_number, email)
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
