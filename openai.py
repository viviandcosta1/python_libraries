import openai

# 🔑 Paste your API key here
openai.api_key = "YOUR_API_KEY"

def smart_chat():
    print("🤖 Smart Chatbot: Ask me anything! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Bot: Goodbye! See you soon.")
            break

        try:
            # Call ChatGPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or "gpt-4" if available
                messages=[
                    {"role": "system", "content": "You are a helpful and knowledgeable assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            bot_reply = response.choices[0].message.content.strip()
            print(f"Bot: {bot_reply}\n")

        except Exception as e:
            print("Bot: Sorry, something went wrong.")
            print(f"Error: {e}")

if __name__ == "__main__":
    smart_chat()
