from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from tkinter import *


conversation = ["oi","ola","bom dia", "como vai?", "eu estou bem"]

bot = ChatBot("Jorge")

trainer = ListTrainer(bot)

trainer.train(conversation)

while True:
    question = input("você: ")
    response = bot.get_response(question)
    if float(response.confidence) > 0.5 :
        print("Jorge: ", response)
    else:
        print("nao entendi...")

# GUI para o bot




