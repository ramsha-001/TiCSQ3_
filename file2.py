def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        word = word.lower()
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

sentence = input("Enter a sentence: ")
print("Word frequency:", word_frequency(sentence))
