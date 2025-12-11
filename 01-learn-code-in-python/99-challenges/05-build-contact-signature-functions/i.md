Build Contact Signature Functions
Complete three functions in main.py to build a simple "contact signature" string.

You work on a tiny contact card generator. Given a person's first name, last name, phone number, and email, you need to build a nicely formatted signature.

Your Task
Implement these functions:

```python
def full_name(first_name, last_name):
    # returns the person's full name as a single string


def build_contact_line(first_name, last_name, phone_number):
    # uses full_name() and returns a contact line string


def build_signature(first_name, last_name, phone_number, email):
    # uses build_contact_line() and returns the final signature string
```

Requirements
full_name(first_name, last_name)

Return the full name as: "FIRST LAST"
Example: full_name("Ada", "Lovelace") → "Ada Lovelace"
build_contact_line(first_name, last_name, phone_number)

Use full_name() inside this function.
Return a string in this format:
"Contact: FULL_NAME | Phone: PHONE_NUMBER"
Example:
```python
build_contact_line("Ada", "Lovelace", "555-0101")
# "Contact: Ada Lovelace | Phone: 555-0101"
```

build_signature(first_name, last_name, phone_number, email)

Use build_contact_line() inside this function.
Return a string in this format:
"Signature: CONTACT_LINE | Email: EMAIL"
Example:
```python
build_signature("Ada", "Lovelace", "555-0101", "ada@example.com")
# "Signature: Contact: Ada Lovelace | Phone: 555-0101 | Email: ada@example.com"
```

Notes
Do not use print() inside these functions. They must return strings.
Focus on:
Defining functions
Passing arguments
Returning values
Calling one function from another
Example

```python
from main import full_name, build_contact_line, build_signature

name = full_name("Luke", "Skywalker")
print(name)
# "Luke Skywalker"

contact = build_contact_line("Luke", "Skywalker", "555-0001")
print(contact)
# "Contact: Luke Skywalker | Phone: 555-0001"

signature = build_signature("Luke", "Skywalker", "555-0001", "luke@rebels.org")
print(signature)
# "Signature: Contact: Luke Skywalker | Phone: 555-0001 | Email: luke@rebels.org"
```