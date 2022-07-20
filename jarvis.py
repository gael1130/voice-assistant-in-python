import reading_quotes
from spotify_commands import *
from the_speech import *
from subprocesses_commands import *
from todolist import *
from reading_quotes import *

while True:
    query = take_command().lower()
    if "play music" in query:
        launch_spotify()
        print("ok boss I start the music")
        start_spotify_playlist(work_playlist)
    elif "pause music" in query:
        # it does not work if I do not have a separate microphone as the music is blocking my voice
        print("I pause the music")
        pause_spotify()

    #     todoist
    elif "show my list" in query:
        print("showing todo list")
        launch_todolist()
        say_the_quote("launching now")
    elif "add project" in query:
        print("adding the project")
        say_the_quote("What is the project name?")
        project_name = create_todoist_name_from_command()
        create_todoist_project(name=project_name)
        say_the_quote("project created")

    elif "new task" in query:
        task_question = "adding a task, but which name?"
        print(task_question)
        say_the_quote(task_question)
        task_name = create_todoist_name_from_command()
        say_the_quote("task created")
        create_todoist_task(content=task_name, project_id=todolist.jarvis_project_id)

    elif "quote of the day" in query:
        daily_quote = random_quote_choice(reading_quotes.my_list)
        say_the_quote(daily_quote)

    elif "rap" in query:
        say_the_quote("Never gonna happen")

    elif "stop" in query:
        print("ciao")
        say_the_quote("ciao")
        quit()
    else:
        print("nope")
