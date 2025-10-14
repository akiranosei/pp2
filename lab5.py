#Python RegEx exercises
#Match string that has 'a' followed by zero or more 'b's.
import re
pattern = r'ab*'
test_strings = ['a', 'ab', 'abb', 'b', 'ac']
for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")

#Match string that has 'a' followed by two to three 'b'
import re
pattern = r'ab{2,3}'
test_strings = ['abb', 'abbb', 'abbbb', 'ab', 'a']
for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")

#Find sequences of lowercase letters joined with a underscore.
import re
text = "hello_world test_case anotherExample not_valid_123"
matches = re.findall(r'[a-z]+_[a-z]+', text)
print(matches)

#Find sequences of one uppercase letter followed by lowercase letters
import re
text = "Hello There from ChatGPT and OpenAI"
matches = re.findall(r'[A-Z][a-z]+', text)
print(matches)

#Match string that has 'a' followed by anything, ending in 'b'
import re
pattern = r'a.*b$'
test_strings = ['acb', 'a123b', 'ab', 'aXb', 'a_bc', 'axb']
for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Match: {s}")

#Replace all spaces, commas or dots with a colon
import re
text = "Hello, world. How are you today"
result = re.sub(r'[ ,.]', ':', text)
print(result)

#Convert snake_case string to camelCase
import re
def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.title() for word in parts[1:])
print(snake_to_camel('hello_world_goodbye_world'))

#Split string at uppercase letters
import re
text = "SplitAtUpperCaseLettersExample"
result = re.split(r'(?=[A-Z])', text)
print(result)

#Insert spaces between words starting with capital letters
import re
text = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
result = re.sub(r'([A-Z])', r' \1', text).strip()
print(result)

#Convert camelCase string to snake_case
import re
def camel_to_snake(s):
    return re.sub(r'([A-Z])', r'_\1', s).lower()
print(camel_to_snake('camelCaseTurnToSnake'))



