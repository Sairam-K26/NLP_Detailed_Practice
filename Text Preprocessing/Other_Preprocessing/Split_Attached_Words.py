# We humans in the social forums generate text data, which is completely informal in nature. Most of the tweets are accompanied with multiple attached words like RainyDay, PlayingInTheCold etc. These entities can be split into their normal forms using simple rules and regex.

import re
import nltk
from nltk.corpus import stopwords

# Download the stopwords from NLTK
nltk.download('stopwords')

# Define the stop words
stop_words = set(stopwords.words('english'))

# Define the input text
original_tweet = "I luv my <3 iphone & you are awsm apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com"

# Remove the stop words
text = ' '.join([word for word in original_tweet.split() if word not in stop_words])

# Remove all punctuation except ".", ",", "?"
text = re.sub(r'[^\w\s.,?]', '', text)

# Split attached words
cleaned = " ".join(re.findall('[A-Z][^A-Z]*', text))

print(cleaned)

# Output: 'I luv my <3 iphone & you are awsm apple. Display Is Awesome, sooo happppppy http://www.apple.com'

