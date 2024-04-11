# re.search(pattern, string):
# It is similar to match() but it doesn’t restrict us to find matches at the beginning of the string only. Unlike previous method, here searching for pattern ‘Analytics’ will return a match.
 
# Importing libraries
import re

# matching AV in the given sentence
result = re.search(r'Analytics', 'AV Analytics Vidhya AV')
print (result.group(0))

