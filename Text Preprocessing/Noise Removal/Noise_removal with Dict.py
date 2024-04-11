# Sample code to remove noisy words from a text

# Noise removal is a text preprocessing step concerned with removing unnecessary noise from the text. Noise is any part of the text that is not relevant to the context of the data and the end-output of the task we are working on. For example, the following words are considered noise in the context of sentiment analysis: a, an, the, this, is, and so on. Similarly, in the context of spam detection, the following words could be considered noise: subject, from, to, cc, etc. Noise removal is essential for text preprocessing because it helps to eliminate words that are irrelevant to the analysis and focus on the important words instead.
noise_list = ["is", "a", "this", "..."] 
def _remove_noise(input_text):
    words = input_text.split() 
    noise_free_words = [word for word in words if word not in noise_list] 
    noise_free_text = " ".join(noise_free_words) 
    return noise_free_text

print(_remove_noise("this is a sample text"))


