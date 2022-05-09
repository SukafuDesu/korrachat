from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_random_response
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def turnOnBot():
    my_bot = ChatBot(
        'Korra',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                "statement_comparison_function": LevenshteinDistance,
                "response_selection_method": get_random_response,
                #'default_response': 'What does that even mean?'
            }
        ]
    )
    list_trainer = ListTrainer(my_bot)
    #'chatterbot.corpus.english', 
    trainer = ChatterBotCorpusTrainer(my_bot)
    trainer.train("./db/chatbot/", "./db/defaults/")
    return [my_bot, trainer]

def botResponse(bot, input):
    return (bot.get_response(input));