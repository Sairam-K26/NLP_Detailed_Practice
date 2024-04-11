# re.findall (pattern, string):
# It helps to get a list of all matching patterns. It has no constraints of searching from start or end. If we will use method findall to search ‘AV’ in given string it will return both occurrence of AV. While searching a string, I would recommend you to use re.findall() always, it can work like re.search() and re.match() both.

# Importing libraries
import re

# Finding all occurrences of AV in given string
result = re.findall(r'AV', 'AV Analytics Vidhya AV')
print (result)