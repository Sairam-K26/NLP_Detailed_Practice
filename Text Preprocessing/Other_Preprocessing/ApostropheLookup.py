# To avoid any word sense disambiguation in text, it is recommended to maintain proper structure in it and to abide by the rules of context free grammar. When apostrophes are used, chances of disambiguation increases.
# For example “it’s is a contraction for it is or it has”.

# All the apostrophes should be converted into standard lexicons. One can use a lookup table of all possible keys to get rid of disambiguates.

import html

# Apostrophe lookup dictionary
APPOSTOPHES = {"'s" : " is", "'re" : " are"} # Add more as needed

# Original tweet
original_tweet = "I luv my &lt;3 iphone &amp; you’re awsm apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com"

# Decode HTML entities
decoded_html = html.unescape(original_tweet)

# Split the tweet into words
words = decoded_html.split()

# Replace apostrophes using the dictionary
reformed = [APPOSTOPHES[word] if word in APPOSTOPHES else word for word in words]

# Join the words back into a string
reformed_tweet = " ".join(reformed)

# Encode to ASCII and ignore errors
ascii_encoded = reformed_tweet.encode('ascii', 'ignore')

# Decode back to string
final_tweet = ascii_encoded.decode()

# Print the final tweet
print("The final tweet is : " + str(final_tweet))