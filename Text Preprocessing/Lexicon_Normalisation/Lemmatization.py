# Another type of textual noise is about the multiple representations exhibited by single word.
# For example, the word “play” may be used in the context of “playing”, “played”, “plays”.
#The most common lexicon normalization practices are :

#Lemmatization: Lemmatization, on the other hand, is an organized & step by step procedure of obtaining the root form of the word, it makes use of vocabulary (dictionary importance of words) and morphological analysis (word structure and grammar relations).

#Lemmatization is similar to stemming but it brings context to the words. So it links words with similar meaning to one word. Lemmatization is preferred over stemming because lemmatization does morphological analysis of the words.

#Lemmatization returns the base or dictionary form of a word, which is known as the lemma.

#Lemmatization is more accurate than stemming as it uses a dictionary-based approach i.e. a vocabulary and morphological analysis to the root word.

#Lemmatization is a more powerful operation than stemming. It involves first determining the part of speech of a word and applying different normalization rules for each part of speech.

#Lemmatization is a process of extracting a base word by considering the vocabulary. For example, “better” will be lemmatized to “good”.

#Lemmatization is very useful in question-answering systems and language generation applications.

#There are many lemmatization algorithms, but the most common algorithm is the WordNet Lemmatizer. WordNet is a lexical database of the English language, which was created by Princeton, and is part of the NLTK corpus.

'''
Lemmatization
'''

#importing required libraries
import nltk
from nltk.stem.wordnet import WordNetLemmatizer 
lem = WordNetLemmatizer()
word = "multiplying" 
print('\n\nLemmatization\n\n')
print(lem.lemmatize(word, "v"))


#The output of the above code will be:
#multiply
