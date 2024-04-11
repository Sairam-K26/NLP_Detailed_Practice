# Sometimes words are not in proper formats. For example: “I looooveee you” should be “I love you”. Simple rules and regular expressions can help solve these cases.

import itertools

def _slang_lookup(tweet):
    # Slang lookup dictionary
    SLANG_DICT = {"luv" : "love", "awsm" : "awesome"} # Add more as needed

    # Split the tweet into words
    words = tweet.split()

    # Replace slang words using the dictionary
    reformed = [SLANG_DICT[word] if word in SLANG_DICT else word for word in words]

    # Join the words back into a string
    reformed_tweet = " ".join(reformed)

    return reformed_tweet

# Original tweet
tweet = "I luv my <3 iphone & you are awsm apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com"

# Call the _slang_lookup function
tweet = _slang_lookup(tweet)

# Standardize words
tweet = ''.join(''.join(s)[:2] for _, s in itertools.groupby(tweet))

print(tweet)

# Output: I love my <3 iphone & you are awesome apple. DisplayIsAwesome, so happpy 🙂 http://www.apple.com