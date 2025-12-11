def full_name(first_name, last_name):
    return first_name + " " + last_name


def build_contact_line(first_name, last_name, phone_number):
    name = full_name(first_name, last_name)
    return "Contact: " + name + " | Phone: " + phone_number


def build_signature(first_name, last_name, phone_number, email):
    contact_line = build_contact_line(first_name, last_name, phone_number)
    return "Signature: " + contact_line + " | Email: " + email

## my solution
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"


def build_contact_line(first_name, last_name, phone_number):
    contact = f"Contact: {full_name(first_name, last_name)}"
    phone = f"Phone: {phone_number}"
    return f"{contact} | {phone}"


def build_signature(first_name, last_name, phone_number, email):
    contact_and_phone = build_contact_line(first_name, last_name, phone_number)
    return f"Signature: {contact_and_phone} | Email: {email}"

