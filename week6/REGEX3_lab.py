import re
# Task 5: 'a' followed by anything, ending in 'b'
def match_a_to_b(text):
    pattern = r'a.*b$'
    if re.search(pattern, text):
        return "Found a match!"
    return "No match."

# Task 6: Replace space, comma, or dot with a colon
def replace_with_colon(text):
    return re.sub(r"[ ,.]", ":", text)

print(match_a_to_b("alphabet_soup_b")) # Match
print(replace_with_colon("Python Exercises, Part 1. Done"))