string = "ABC123@gmail.com"

lowercase_count = sum(1 for char in string if char.islower())
uppercase_count = sum(1 for char in string if char.isupper())
special_symbols_count = sum(1 for char in string if not char.isalnum())
digits_count = sum(1 for char in string if char.isdigit())

print(f"lowercase = {lowercase_count}, uppercase = {uppercase_count}, special symbols = {special_symbols_count}, digits = {digits_count}")
