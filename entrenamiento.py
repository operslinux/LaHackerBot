from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('La Hacker')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.spanish")

# Get a response to an input statement
#chatbot.get_response("Hello, how are you today?")

while True:
    usuario = input(">>> ")
    respuesta = chatbot.get_response(usuario)
    print("BOT: " +str(respuesta))