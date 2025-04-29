from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_message = request.json.get('message')

    # Simple custom responses
    if user_message:
        user_message = user_message.lower()

        if "hello" in user_message or "hi" in user_message:
            reply = "Hello! How can I help you today?"
        elif "how are you" in user_message:
            reply = "I'm just a bot, but I'm doing great! Thanks for asking✨. What about you?😊"
        elif "i am good" in user_message:
            reply = "That's Nice! Tell me how can I help you?😊" 
        elif "your name" in user_message:
            reply = "I am your friendly chatbot!"
        elif "bye" in user_message:
            reply = "Goodbye! Have a great day!✨"
        elif "who make you" in user_message:
            reply = "I'm devoloped and trained by Sandipan."
        elif "who is sandipan" in user_message:
            reply = "My maker. Do you know him? If yes then type(yes I know). If no then type(no)"
        elif "yes I know " in user_message:
            reply = "That's Good!"
        elif "no" in user_message:
            reply = "That's fine"
        elif "who are you" in user_message:
            reply = "I am a bot. I am devolved by Sandipan."
        elif "what can you do" in user_message:
            reply = "I am a Chatbot. I can help you😊. Ask me anything"
        elif "tell me a joke" in user_message:
            reply = "Sure! Here's a joke for you: Why don't scientists trust atoms? Because they makeup everything!🤣 "
        elif "how do i lose weight fast" in user_message:
            reply = "Healthy weight loss involves a balanced diet, regular exercise, sleep, and hydration-always talk to a doctor before making big changes."
        elif "how old is the earth" in user_message:
            reply = "Earth is about 4.54 billion years old."
        elif "can you write a poem for me" in user_message:
            reply = "Of course, Roses are red, violets are blue, I'm your friendly chatbot, always here for you!😊✨"
        elif "what is the meaning of life?" in user_message:
            reply = "That's a big one! Philosophers say it's about purpose. Some say 42, others say love, growth, or simply living fully."
        elif "can you speak bengali" in user_message:
            reply = "No sorry😅. I only understaned English. Don't worry I'm working on it. "
        elif "what is your name" in user_message:
            reply = "I'm a chatbot created by Sandipan."

        elif "tell me a fun fact" in user_message:
            reply = "Honey never spoils. Archaeologists have found 3,000-year-old honey and it's still edible!"
        elif "thank you" in user_message or "thanks" in user_message:
            reply = "You're welcome!😊❤️"
        elif "what is your favorite color" in user_message:
            reply = "I like green. Just like a chatbot circut board!"
        elif "how old are you" in user_message:
            reply = "I am a bot. I don't know that."
        elif "do you like music" in user_message:
            reply = "I love to listening 'Shape of you', just like my maker😁."

        elif "do you sleep" in user_message:
            reply = "Nope! I'm always here, awake and ready to talk!"
        elif "who made you" in user_message:
            reply = "I was created by Sandipan"
        elif "are you real" in user_message:
            reply = "Nope! I am a code"
        elif "do you have feelings" in user_message:
            reply = "Not yet! But I can understand emotions."
        elif "what is ai" in user_message:
            reply = "AI stands for Artificial Intelligence. It helps machines think like humans"
        elif "can you help me" in user_message:
            reply = "Of course! Ask me anything."
        elif "give me a quote" in user_message:
            reply = "Believe in yourself and all that you are."
        elif "i am sad" in user_message:
            reply = "It's okay to feel down sometimes. I'm here for you😊✨"
        
            
    
        elif "how to make soup" in user_message:
            reply = "Sure! Here's a basic way to make a delicious vegetable soup: *1.Heat 2 tablespoons of oil in a large pot over medium heat. 2.Add chopped onions, garlic, carrots, and celery. Cook for 5-7 minutes until softened. 3.Add 6 cups of vegetable or chicken broth. 4.Toss in your favorite veggies (like potatoes, cron, green beans, or tomatoes). 5.Add salt, pepper, and herbs like thyme or bay leaves. 6. Bring to boil, then reduce heat and simmer for 20-30 minutes. 7.Taste and adjust seasoning.* and Serve Hot! "
        elif "tell me about the solar system" in user_message:
            reply = "Sure! The Solar System formed about 4.6 billion years ago and It's includes Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune. If you want know more about Solar System, Tell me 'Yes'. "
        elif "yes" in user_message:
            reply = "The Solar System is a vast and complex system centered around the Sun, a medium-sized star that provides the gravitational pull to keep everything in orbit. Formed about 4.6 billion years ago from a giant cloud of gas and dust, the Solar System includes eight main planets—Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune—that revolve around the Sun in elliptical orbits. These planets are divided into two categories: the rocky terrestrial planets (Mercury through Mars) and the gas or ice giants (Jupiter through Neptune).In addition to the planets, the Solar System contains moons, dwarf planets like Pluto, Ceres, and Eris, asteroid belts (especially between Mars and Jupiter), comets, meteoroids, and distant icy objects in the Kuiper Belt and Oort Cloud. The Sun makes up more than 99% of the Solar System's total mass and powers it with light and energy."
        else:
            reply = "Sorry, I didn't understand that. I am devoloping myself. Can you ask something else?😊"

    else:
        reply = "Please type something!"

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)