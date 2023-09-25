import re

string = "Q-301 is at 4 th floor of quaid block."
digits = [int(digit) for digit in re.findall(r'\d', string)]
if digits:
    digit_sum = sum(digits)
    digit_average = digit_sum / len(digits)
    print(f"Sum = {digit_sum} and Average is {digit_average:.2f}")
else:
    print("No digits found in the string.")
