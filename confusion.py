import nltk 
from nltk.corpus import wordnet

text = str(input("start the conversation:"))


def get_word_meaning(word,pos_tag):
    synsets = wordnet.synsets(word, pos=pos_tag)
    if synsets and synsets[0]:
        return synsets[0].definition()
    return "no definition found"

print("hello! i am a chatbot")  
print("Type a sentence and I'll give meanings of nouns, verbs, and determines.") 
print("type 'bye' or 'exit' to end.\n") 

while True:  
    text = input("you: ")
    if text.lower() in ['bye', 'exit']:
        print("goodbye!have a great day  ")
        break

    tokens = nltk.word_tokenize(text) 
    pos_tag = nltk.pos_tag(tokens) 

    nouns = [word for word, pos in pos_tag if pos.startswith('N')]
    verbs = [word for word, pos in pos_tag if pos.startswith('V')]
    determines = [word for word, pos in pos_tag if pos.startswith('D')]  

    print("\n. what i found is:")

    for category, word_list, wn_pos in [
        ("Nouns", nouns, wordnet.NOUN),
        ("Verbs", verbs, wordnet.VERB),
        ("Determines", determines, wordnet.NOUN)
    
]:
        if word_list:
            print(f"\n{category}:")
            for word in word_list:
                meaning = get_word_meaning(word, wn_pos)
                print(f"   {word}: {meaning}")
