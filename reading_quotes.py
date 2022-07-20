import pyttsx3
import pandas as pd
import openpyxl
import random

df = pd.read_excel('quotes.xlsx', header=None, index_col=None)

my_list = df[0].tolist()


def random_quote_choice(quotes_list):
    daily_quote = random.choice(quotes_list)
    return daily_quote


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# choosing the eng-US voice over the french voice
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 172)


def say_the_quote(daily_quote):
    engine.say(daily_quote)
    engine.runAndWait()
    engine.stop()


"""
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello World!")
    engine.runAndWait()
    engine.stop()
"""

