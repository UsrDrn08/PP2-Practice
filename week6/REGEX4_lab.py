import re
# Task 7: Snake case to Camel case
def snake_to_camel(text):
    # Splits by underscore and capitalizes each word
    return ''.join(word.capitalize() for word in text.split('_'))

# Task 10: Camel case to Snake case
def camel_to_snake(text):
    # Inserts underscore before caps and converts to lower
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-0])([A-Z])', r'\1_\2', str1).lower()

print(snake_to_camel("python_regex_exercise")) # PythonRegexExercise
print(camel_to_snake("PythonRegexExercise"))   # python_regex_exercise