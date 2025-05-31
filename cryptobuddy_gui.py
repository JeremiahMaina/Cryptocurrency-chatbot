import tkinter as tk
from tkinter import scrolledtext

# Sample crypto database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# Chatbot logic
def crypto_buddy(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!"

    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f"The coins currently trending up are: {', '.join(trending)} 🚀"

    elif "long-term" in user_query or "growth" in user_query or "should i buy" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                return f"{coin} is trending up and has a top-tier sustainability score! 🚀"
        return "Hmm, I can't find a coin that meets all long-term growth criteria right now."

    elif "most sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"The most sustainable coin is {recommend} 🌿 with a score of {crypto_db[recommend]['sustainability_score']*10}/10!"

    else:
        return (
            "I'm CryptoBuddy 🤖. Ask me things like:\n"
            "- 'Which crypto is trending up?'\n"
            "- 'What is the most sustainable coin?'\n"
            "- 'Which crypto should I buy for long-term growth?'\n"
            "⚠️ Crypto is risky—always do your own research!"
        )

# GUI interface using Tkinter
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_log.insert(tk.END, f"You: {user_input}\n", 'user')
    response = crypto_buddy(user_input)
    chat_log.insert(tk.END, f"CryptoBuddy: {response}\n\n", 'bot')
    entry.delete(0, tk.END)

# Initialize main window
root = tk.Tk()
root.title("CryptoBuddy Chatbot 💬")

# Configure layout
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Helvetica", 12))
chat_log.pack(padx=10, pady=10)
chat_log.tag_config('user', foreground='blue')
chat_log.tag_config('bot', foreground='green')

entry = tk.Entry(root, font=("Helvetica", 12), width=50)
entry.pack(padx=10, pady=(0, 10), side=tk.LEFT, expand=True, fill=tk.X)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=(0, 10), pady=(0, 10), side=tk.RIGHT)

# Start the application
root.mainloop()
