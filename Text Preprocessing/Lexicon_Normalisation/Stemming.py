# Another type of textual noise is about the multiple representations exhibited by single word.
# For example, the word “play” may be used in the context of “playing”, “played”, “plays”.
#The most common lexicon normalization practices are :

#Stemming:  Stemming is a rudimentary rule-based process of stripping the suffixes (“ing”, “ly”, “es”, “s” etc) from a word.
#Stemming is the process of reducing inflected (or sometimes derived) words to their word stem, base or root form—generally a written word form. Example if we consider the word “Jumps” then the stem word would be “Jump”. Stemming is important in natural language processing (NLP) and information retrieval (IR) for indexing and searching for relevant information.

#There are many stemming algorithms, but the most common algorithm is the Porter Stemmer. The Porter stemming algorithm (or ‘Porter stemmer’) is a process for removing the commoner morphological and inflexional endings from words in English. Its main use is as part of a term normalisation process that is usually done when setting up Information Retrieval systems.

'''
Stemming
'''

#importing required libraries
import nltk
from nltk.stem.porter import PorterStemmer 
stem = PorterStemmer()

word = "multiplying" 


print('\n\nStemming\n\n')
print(stem.stem(word))



#The output of the above code will be:
#multipli


