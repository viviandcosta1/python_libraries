import wikipedia
import re
import difflib

class WikiChatbot:
    def __init__(self):
        wikipedia.set_lang("en")
        self.exit_words = ['exit', 'bye', 'quit']
        print("\n🤖 Wikipedia Chatbot")
        print("Ask me about anything — politics, history, sports, people, or tech.")
        print("Type 'exit' to quit.\n")

    def clean_text(self, text):
        return re.sub(r'[^\w\s]', '', text.lower())

    def search_topic(self, query):
        # Try direct search
        results = wikipedia.search(query)
        if results:
            return results[0]

        # Try suggested topic
        suggestion = wikipedia.suggest(query)
        if suggestion:
            return suggestion

        # Try close match from existing titles
        titles = wikipedia.search(query)
        if titles:
            return difflib.get_close_matches(query, titles, n=1, cutoff=0.2)[0]

        return None

    def get_summary(self, topic):
        try:
            return wikipedia.summary(topic, sentences=2)
        except wikipedia.exceptions.DisambiguationError as e:
            return f"❗️ Your question is too broad. Try one of: {', '.join(e.options[:3])}"
        except wikipedia.exceptions.PageError:
            return "❌ I couldn't find a Wikipedia page for that."
        except Exception as e:
            return f"⚠️ Something went wrong: {e}"

    def chat(self):
        while True:
            user_input = input("You: ").strip()
            if self.clean_text(user_input) in self.exit_words:
                print("Bot: Goodbye! 👋")
                break
            if not user_input:
                continue

            topic = self.search_topic(user_input)
            if topic:
                response = self.get_summary(topic)
            else:
                response = "❌ I couldn’t find anything relevant in Wikipedia."

            print(f"Bot: {response}\n")

if __name__ == "__main__":
    bot = WikiChatbot()
    bot.chat()
