

def fabric_chatbot():
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

    print("🧵 Fabric Chatbot")
    print("Type the name of a fabric to know more. Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! 👋 Stay cool!")
            break
        elif user_input in fabric_knowledge:
            print("Bot:", fabric_knowledge[user_input])
        else:
            print("Bot: I don't have info on that fabric. Try asking about cotton, silk, wool, etc.")

# Run the chatbot
fabric_chatbot()
