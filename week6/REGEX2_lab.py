import re
# Task 3: Lowercase letters joined with an underscore
def find_lowercase_underscore(text):
    # Matches sequences like 'hello_world'
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, text)

# Task 4: One upper case letter followed by lower case letters
def find_title_case(text):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, text)

print(find_lowercase_underscore("this_is_a_test and This_Is_Not"))
print(find_title_case("Hello World from Python"))