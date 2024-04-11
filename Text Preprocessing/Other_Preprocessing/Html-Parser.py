# Escaping HTML characters: Data obtained from web usually contains a lot of html entities like &lt; &gt; &amp; which gets embedded in the original data. It is thus necessary to get rid of these entities. One approach is to directly remove them by the use of specific regular expressions. Another approach is to use appropriate packages and modules (for example htmlparser of Python), which can convert these entities to standard html tags. For example: &lt; is converted to “<” and &amp; is converted to “&”.

original_tweet = "I luv my &lt;3 iphone &amp; you’re awsm apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com"

print('\n\nEscaping HTML Characters\n\n')

from html.parser import HTMLParser
html_parser = HTMLParser()
tweet = html_parser.unescape(original_tweet)
print(tweet)

# Output: I luv my <3 iphone & you’re awsm apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com

