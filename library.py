import nltk
from nltk.corpus import wordnet


text = str(input("enter the text:"))
tokens = nltk.word_tokenize(text)
print("tokens:",tokens)

pos_tags = nltk.pos_tag(tokens)
print("\nPart-of-speech tags:",pos_tags)

nouns = [word for word, pos in pos_tags if pos.startswith('N')]
verbs = [word for word, pos in pos_tags if pos.startswith('V')]
determines =  [word for word, pos in pos_tags if pos.startswith('D')]

print("\nNouns:",nouns)
print("Verbs:",verbs)
print("Determines:",determines)

def get_word_meaning(word,pos_tag):
    synsets = wordnet.synsets(word, pos=pos_tag)
    if synsets and synsets[0]:
        return synsets[0].definition()
    return "No defination found"

dictionary = {
    "nouns": {word:get_word_meaning(word, wordnet.NOUN) for word in nouns},
    "verbs" : {word:get_word_meaning(word, wordnet.VERB) for word in verbs},
    "determines" : {word:get_word_meaning(word, wordnet.NOUN) for word in determines}
                             
}   


print("\nDictionary with meaning")
for category,words in dictionary.items():
    print(f"\n{category.upper()}:")
    for word,meaning in words.items():
        print(f" {word}: {meaning}")                           