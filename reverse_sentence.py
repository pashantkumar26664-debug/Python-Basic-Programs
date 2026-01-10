def reverse_sentence(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    # Reverse the list
    reversed_words = words[::-1]
    # Join them back into a string
    return " ".join(reversed_words)

print(reverse_sentence("Hello world this is Python"))