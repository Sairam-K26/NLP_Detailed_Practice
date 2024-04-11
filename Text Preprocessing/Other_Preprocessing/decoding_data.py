# Thisis the process of transforming information from complex symbols to simple and easier to understand characters. Text data may be subject to different forms of decoding like “Latin”, “UTF8” etc. Therefore, for better analysis, it is necessary to keep the complete data in standard encoding format. UTF-8 encoding is widely accepted and is recommended to use.

original_tweet = "I luv my &lt;3 iphone &amp; you’re awsm apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com"

# printing original string
print("The original tweet is : " + str(original_tweet))

# encoding to ASCII and ignoring errors
tweet = original_tweet.encode('ascii', 'ignore')

# decoding back to string
decoded_tweet = tweet.decode()

# print result
print("The tweet after decoding : " + str(decoded_tweet))
# Output: “I luv my <3 iphone & you’re awsm apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com”
