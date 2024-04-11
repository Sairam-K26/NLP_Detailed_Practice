# re.compile(pattern, repl, string):
# We can combine a regular expression pattern into pattern objects, which can be used for pattern matching. It also helps to search a pattern again without rewriting it.

# Importing re library
import re

pattern=re.compile('AV')
result=pattern.findall('AV Analytics Vidhya AV')
print (result)
result2=pattern.findall('AV is largest analytics community of India')
print (result2)