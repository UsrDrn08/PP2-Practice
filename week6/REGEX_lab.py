import re

# Task 1: 'a' followed by zero or more 'b's
def match_zero_or_more_b(text):
    pattern = r'ab*'
    if re.search(pattern, text):
        return "Found a match!"
    return "No match."

# Task 2: 'a' followed by two to three 'b's
def match_two_to_three_b(text):
    pattern = r'ab{2,3}'
    if re.search(pattern, text):
        return "Found a match!"
    return "No match."

print(match_zero_or_more_b("ac"))   # Match (zero b's)
print(match_two_to_three_b("abb")) # Match