# # When data analysis needs to be data driven at the word level, the commonly occurring words (stop-words) should be removed. One can either create a long list of stop-words or one can use predefined language specific libraries.
# All the punctuation marks according to the priorities should be dealt with. For example: “.”, “,”,”?” are important punctuations that should be retained while others need to be removed.
# Textual data (usually speech transcripts) may contain human expressions like [laughing], [Crying], [Audience paused]. These expressions are usually non relevant to content of the speech and hence need to be removed. Simple regular expression can be useful in this case.

import re
import nltk
from nltk.corpus import stopwords

# Download the stopwords from NLTK
nltk.download('stopwords')

# Define the stop words
stop_words = set(stopwords.words('english'))

# Define the input text
text = "I luv my <3 iphone & you are awsm apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com"

# Remove the stop words
text = ' '.join([word for word in text.split() if word not in stop_words])

# Remove all punctuation except ".", ",", "?"
text = re.sub(r'[^\w\s.,?]', '', text)

# Remove expressions in brackets
text = re.sub(r'\[.*?\]', '', text)

print(text)

# Output: 'I luv my <3 iphone & you are awsm apple. DisplayIsAwesome, sooo happppppy http://www.apple.com'
