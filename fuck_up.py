'''
import re
def zero_more (e):
    a = r'ab*'
    return bool(re.search(a,e))


u = input()
results = zero_more(u)
print(results)
'''
'''
-------------------------------
'''
'''
import re
def two_three (e):
    a = r'ab{2,3}'
    return bool(re.search(a,e))


u = input()
results = two_three(u)
print(results)
'''
'''
--------------------------------
'''
'''
import re

def find_underscore_sequences(text):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, text)

u = input()
give = find_underscore_sequences(u)
print(give)
'''
'''
-----------------------------
'''
'''
import re

def find_upperscore_sequences(text):
    pattern = r'[A-Z]+_[A-Z]+'
    return re.findall(pattern, text)

u = input()
give = find_upperscore_sequences(u)
print(give)
'''
'''
---------------------
'''
'''
import re
def match_pattern_anywhere(text):

    pattern = r'a.*b$'
    return bool(re.search(pattern, text))
i = input()
text = match_pattern_anywhere(i)
print(text)
'''
'''
import re
def replace_column(er):
    pattern = r'[ ,.]'
    result = re.sub(pattern,':',er)
    return result

i = input()
text = replace_column(i)
print(text)
'''
'''
----------------------
'''
'''
import re
def snake_to_camel(snake_str):

    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
i = input()
text = snake_to_camel(i)
print(text)
'''
'''
import re
def split_at_uppercase(text):

    parts = re.split(r'(?=[A-Z])', text)


    return [part for part in parts if part]

a = input()
result1 = split_at_uppercase(a)
print(result1)
'''
'''
------------------
'''
'''
import re

def insert_spaces(text):

    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return result

a = input()
result = insert_spaces(a)
print(result)
'''
'''
---------------------
'''

import re

def camel_to_snake(camel_str):

    snake_case = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str)
    return snake_case.lower()


a = input()
result = camel_to_snake(a)
print(result)

