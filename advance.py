import nltk
from nltk.corpus import wordnet
from nltk import pos_tag, word_tokenize
import string


def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


def pos_full_name(tag):
    if tag.startswith('NN'):
        return "Noun"
    elif tag.startswith('VB'):
        return "Verb"
    elif tag.startswith('JJ'):
        return "Adjective"
    elif tag.startswith('RB'):
        return "Adverb"
    elif tag == 'DT':
        return "Determiner"
    else:
        return "Other"

def get_word_meaning(word, pos_tag=None):
    synsets = wordnet.synsets(word, pos=pos_tag)
    if synsets:
        return synsets[0].definition()
    return "No definition found."

# Introduction
print("🤖 Hello! I’m a smart Word Meaning Chatbot!")
print("💬 Type any sentence, and I’ll show the POS and meaning of each important word.")
print("🚪 Type 'bye' or 'exit' to quit.\n")

# Main loop
while True:
    text = input("👤 You: ")
    if text.lower().strip() in ['bye', 'exit']:
        print("🤖 Goodbye! Have a great day 😊")
        break

    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)

    # Filter punctuation
    filtered = [(word, tag) for word, tag in pos_tags if word not in string.punctuation]

    if not filtered:
        print("⚠️ Please enter a valid sentence.")
        continue

    print("\n📘 Here's what I found:")

    for word, tag in filtered:
        wn_tag = get_wordnet_pos(tag)
        full_tag = pos_full_name(tag)
        meaning = get_word_meaning(word, wn_tag)
        print(f"🔹 {word} ({full_tag}): {meaning}")

    print("\n📝 Try another sentence or type 'bye' to quit.\n")
