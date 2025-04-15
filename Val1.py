import re
import dns.resolver
import socket

def is_valid_email_format(email):
    # Regex to check email format
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def get_domain_from_email(email):
    # Extract domain from email
    return email.split('@')[1]

def has_valid_mx_records(domain):
    # Check if domain has valid MX records
    try:
        # Query the MX records for the domain
        dns.resolver.resolve(domain, 'MX')
        return True
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return False

def main():
    print("Email Validator with MX Check")
    print("Type 'exit' to quit.\n")

    while True:
        email = input("Enter an email address: ").strip()
        if email.lower() == 'exit':
            print("Goodbye!")
            break

        if not is_valid_email_format(email):
            print("Invalid email format. Please try again.\n")
            continue

        # Extract the domain and check for MX records
        domain = get_domain_from_email(email)
        if has_valid_mx_records(domain):
            print(f"Valid email domain: {domain} has MX records. Email may be deliverable!\n")
        else:
            print(f"Invalid email domain: {domain} has no MX records. Email may not be deliverable.\n")

if __name__ == "__main__":
    main()
