
def slice_mail(email_address):
    parts = email_address.split('@')
    strip_username = parts[0]
    strip_ending = parts[-1]
    return 'Username:' + strip_username + '\n' + 'Provider:' + strip_ending


email_from_input = input("Enter your email address : ").strip()
print(slice_mail(email_address=email_from_input))
