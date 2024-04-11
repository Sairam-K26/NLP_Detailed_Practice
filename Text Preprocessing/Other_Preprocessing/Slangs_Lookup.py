# Again, social media comprises of a majority of slang words. These words should be transformed into standard words to make free text. The words like luv will be converted to love, Helo to Hello. The similar approach of apostrophe look up can be used to convert slangs to standard words. A number of sources are available on the web, which provides lists of all possible slangs, this would be your holy grail and you could use them as lookup dictionaries for conversion purposes.

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

print(tweet)

# Output: I love my <3 iphone & you are awesome apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com
