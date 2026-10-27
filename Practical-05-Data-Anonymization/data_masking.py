def mask_email(email):
    name, domain = email.split("@", 1)
    visible = name[:2]
    return visible + "*" * max(1, len(name) - 2) + "@" + domain

def mask_phone(phone):
    digits = "".join(ch for ch in phone if ch.isdigit())
    return "*" * max(0, len(digits) - 4) + digits[-4:]

emails = ["aditya@example.com", "student@example.com"]
phones = ["9876543210", "9123456789"]

print("Masked emails:")
for e in emails:
    print(mask_email(e))

print("
Masked phones:")
for p in phones:
    print(mask_phone(p))
