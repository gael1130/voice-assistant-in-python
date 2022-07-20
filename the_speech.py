import speech_recognition as sr

import todolist
from todolist import *

"""
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)


# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

"""


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language="en-US")
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except Exception as e:
        print(e)
        print("Unable to understand")
        return "None"
    return query


def create_todoist_name_from_command():
    """
    Ask me what is the name I want for the project or task I want to create
    :return:
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What is the name of the project or task?")
        audio = r.listen(source)

    try:
        query_name = r.recognize_google(audio, language="en-US")
        print("Google Speech Recognition thinks the name of the project is: " + r.recognize_google(audio))
    except Exception as e:
        print(e)
        print("Unable to understand")
        return "None"
    return query_name


def get_project_id_from_name():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What is the name of the project or task?")
        audio = r.listen(source)

        try:
            query_name = r.recognize_google(audio, language="en-US")
            print("Google Speech Recognition thinks the name of the project is: " + r.recognize_google(audio))
        except Exception as e:
            print(e)
            print("Unable to understand")
            return "None"

        if ("jarvis" or "Jarvis") in query_name:
            project_id = todolist.jarvis_project_id
        else:
            project_id = "No Comprendo"
        return project_id
