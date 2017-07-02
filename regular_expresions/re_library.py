import re

# Using re functions
# match = re.search('pattern', 'Searching pattern in text')

# if match is not None:
#     print(match) # one match object
#     print(match.re.pattern) # gives us the pattern
#     print(match.string) # gives us the source text 
#     print(match.start()) # returns the index of the start of the match inside the source text
#     print(match.end()) # returns the index of the end of the match inside the source
# else:
#     print('There\'s no match')

# Using regex object 
# regex = re.compile('pattern')
# result = regex.search('Searching pattern in text').start()
# if result is not None:
#     print(result) # one match object
# else:
#     print('There\'s no match')

# Global matches
# regex = re.compile('pattern')
# # To get a list of all matches
# result = regex.findall('Searching pattern in text pattern')


# Iterate over all matches in the source text
# def all_matches(text, pattern):
#     print(pattern)
#     regobj = re.compile(pattern)
#     for m in regobj.finditer(text):
#         start = m.start()
#         end = m.end()
#         print(str(start) + '-' + str(end) + ':' + text[start:end])

# all_matches('xyyxxxxxyyyyxxxxyy', 'x[xy]+')

# Groups
# import re

# regex = re.compile('x([xy]+)(y)')
# match = regex.search('xyxxxyxxxyxyxy')
# print(match.groups())
# print(match.group(1))
# print(match.group(2))

# Naming the groups
# import re
# regex = re.compile('x(?P<first>[xy]+)(?P<second>y)') # By using (?P<group_name>expresion) we give a name to the group
# match = regex.search('xyxxxyxxxyxyxy')

# print(match.group('second')) # uses group name instead of index
# print(match.groupdict()) # gives us the dictionary of groups
