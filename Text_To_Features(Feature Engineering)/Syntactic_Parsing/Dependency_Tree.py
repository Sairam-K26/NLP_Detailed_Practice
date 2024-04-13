import nltk

sentence = "Sairam is a good boy and he is talented in NLP Technologies"

# Tokenize the sentence into words
tokens = nltk.word_tokenize(sentence)

# Perform part-of-speech tagging
pos_tags = nltk.pos_tag(tokens)

# Use the Stanford Dependency Parser for dependency parsing
dependency_parser = nltk.parse.stanford.StanfordDependencyParser()

# Parse the sentence and get the dependency graph
result = dependency_parser.parse(tokens)

# Print the dependency graph
for parse_tree in result:
    parse_tree.pretty_print()

