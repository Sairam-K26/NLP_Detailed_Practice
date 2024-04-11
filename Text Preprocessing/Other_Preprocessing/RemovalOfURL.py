# URLs and hyperlinks in text data like comments, reviews, and tweets should be removed.

import re

# Original tweet
tweet = "I love my iphone & you are awesome apple. Display Is Awesome, so happy! <3  http://www.apple.com"

# Remove URLs
tweet = re.sub(r'http\S+|www.\S+', '', tweet)

print(tweet)

# Output: I love my iphone & you are awesome apple. Display Is Awesome, so happy! <3 