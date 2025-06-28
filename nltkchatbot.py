import nltk
import re

# Download required NLTK resources
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Setup
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Knowledge base
fabric_knowledge = {
    "cotton": "Cotton is a soft, breathable natural fabric used in t-shirts, bedsheets, and daily wear.",
    "silk": "Silk is a shiny, smooth fabric made from silkworms. It is used in sarees and formal clothing.",
    "wool": "Wool is a warm and thick fabric made from sheep fleece. Ideal for winter wear.",
    "linen": "Linen is light and breathable, perfect for hot weather clothing.",
    "polyester": "Polyester is a strong synthetic fabric that resists wrinkles. Common in uniforms and sportswear.",
    "denim": "Denim is a durable cotton fabric typically used to make jeans.",
    "rayon": "Rayon is a semi-synthetic fabric that feels like silk. It’s used in dresses and blouses.",
    "nylon": "Nylon is a strong synthetic fiber used in activewear, swimwear, and ropes.",
    "fabric": "Fabric is any textile material made from fibers by weaving, knitting, or bonding.",
}

# Greeting keywords
greeting_keywords = ["hi", "hello", "hey", "good morning", "good evening"]

# Greeting response
def is_greeting(tokens):
    return any(token in greeting_keywords for token in tokens)

# Preprocessing input
def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    tokens = word_tokenize(text)
    return [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

# Find best matching fabric
def find_fabric(tokens):
    for token in tokens:
        if token in fabric_knowledge:
            return fabric_knowledge[token]
    return None

# Main chatbot loop
def fabric_chatbot():
    print("🧵 Fabric Chatbot")
    print("Ask me about any fabric like 'cotton', 'silk', or 'linen'. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! 👋 Stay fashionable!")
            break

        tokens = preprocess(user_input)

        if is_greeting(tokens):
            print("Bot: Hello! 👋 Ask me about any fabric you want to know about.")
            continue

        response = find_fabric(tokens)
        if response:
            print("Bot:", response)
        else:
            print("Bot: Sorry, I don't have information on that fabric. Try asking about cotton, silk, wool, etc.")

# Run chatbot
fabric_chatbot()
