# Find the longest word in a sentence.
def longest_word_in_sentence():
    sentence="hello i am kirti i am lerning python dsa"
    words=sentence.split()
    longest_word=""
    for word in words:
        if len(word)>len(longest_word):
            longest_word=word
    print("The longest word in the sentence is:",longest_word)
longest_word_in_sentence()