import nltk
import re

# Download required NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class ContextualChatbot:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.chat_history = []  # ⬅️ Store conversation

        # Knowledge base with context
        self.knowledge = {
            "chatbot": "A chatbot is a computer program that simulates human conversation through voice commands or text chats. They use natural language processing to understand user queries.",
            "ai": "Artificial Intelligence is the simulation of human intelligence in machines that are programmed to think and learn like humans.",
            "machine learning": "Machine learning is a method of data analysis that automates analytical model building using algorithms that iteratively learn from data.",
            "python": "Python is a high-level programming language known for its simplicity and readability, widely used in AI and data science.",
            "nltk": "NLTK is a natural language processing library for Python that provides tools for text processing and analysis.",
            "programming": "Programming is the process of creating instructions for computers to solve problems and perform tasks."
        }

        # Create sentence database from knowledge
        self.sentences = []
        for topic, info in self.knowledge.items():
            sentences = sent_tokenize(info)
            for sentence in sentences:
                self.sentences.append(sentence)

    def preprocess(self, text):
        """Clean and tokenize text"""
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        tokens = word_tokenize(text)
        return [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words]

    def similarity(self, text1, text2):
        """Calculate Jaccard similarity between two texts"""
        tokens1 = set(self.preprocess(text1))
        tokens2 = set(self.preprocess(text2))

        if not tokens1 or not tokens2:
            return 0

        intersection = tokens1.intersection(tokens2)
        union = tokens1.union(tokens2)

        return len(intersection) / len(union) if union else 0

    def get_response(self, user_input):
        """Find best matching response from knowledge base"""
        user_input = user_input.lower()

        # Check for greetings
        greetings = ["hello", "hi", "hey", "good morning"]
        if any(greeting in user_input for greeting in greetings):
            return "Hello! I'm here to help you with questions about AI, programming, and technology."

        # Check for farewells
        farewells = ["bye", "goodbye", "exit", "quit"]
        if any(farewell in user_input for farewell in farewells):
            return "Goodbye! It was nice chatting with you!"

        # Find best matching sentence
        best_score = 0
        best_response = "I'm sorry, I don't have information about that. Try asking about AI, programming, Python, or chatbots."

        for sentence in self.sentences:
            score = self.similarity(user_input, sentence)
            if score > best_score:
                best_score = score
                best_response = sentence

        # Also check topic keywords
        for topic, info in self.knowledge.items():
            if topic in user_input or self.similarity(user_input, topic) > 0.3:
                return info

        return best_response if best_score > 0.1 else "I'd be happy to help! You can ask me about chatbots, AI, machine learning, Python programming, or NLTK."

    def log_conversation(self, user_input, response):
        """Store Q&A and optionally save to a file"""
        self.chat_history.append((user_input, response))
        with open("chat_log.txt", "a") as f:
            f.write(f"You: {user_input}\nBot: {response}\n\n")

    def chat(self):
        """Main chat loop"""
        print("🤖 NLTK Contextual Chatbot")
        print("=" * 40)
        print("Hi! Ask me about AI, programming, or technology.")
        print("Type 'quit' to exit.\n")

        while True:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Bot: Goodbye! Have a great day!")
                self.log_conversation(user_input, "Goodbye! Have a great day!")  # ⬅️ Log final message
                break

            response = self.get_response(user_input)
            print(f"Bot: {response}\n")
            self.log_conversation(user_input, response)  # ⬅️ Log every turn

if __name__ == "__main__":
    bot = ContextualChatbot()
    bot.chat()
