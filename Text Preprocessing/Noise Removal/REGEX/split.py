# re.split(pattern, string, [maxsplit=0]):
# This methods helps to split string by the occurrences of given pattern.

# Importing re library
import re

# Splitting the text by occurrences of 'y'
result = re.split(r'y', 'Analytics')
print(result)

#split() has another argument “maxsplit“. It has default value of zero. In this case it does the maximum splits that can be done, but if we give value to maxsplit, it will split the string

result1=re.split(r'i','Analytics Vidhya')
print (result1)

# Splitting the text by occurrences of 'i' with maxsplit set to 1
result2 = re.split(r'i', 'Analytics Vidhya', maxsplit=1)
print(result2)

