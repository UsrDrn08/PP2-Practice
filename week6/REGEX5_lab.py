import re 
# Task 8: Split a string at uppercase letters
def split_at_uppercase(text):
    return re.findall(r'[A-Z][^A-Z]*', text)

# Task 9: Insert spaces between words starting with capital letters
def insert_spaces_caps(text):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", text)

print(split_at_uppercase("SplitThisStringAtCaps"))
print(insert_spaces_caps("InsertSpacesBetweenTheseWords"))