import time

import psutil
import subprocess as sp
import time
from spotify_commands import *
import fixed

spotify_exe = fixed.spotify_exe
todolist_app = fixed.todolist_app


def launch_spotify():
    if "Spotify.exe" in (p.name() for p in psutil.process_iter()):
        print("Spotify is already running")
    else:
        sp.Popen(spotify_exe)
        time.sleep(6)
        start_spotify_playlist(work_playlist)


def launch_todolist():
    if "todoist.exe" in (p.name() for p in psutil.process_iter()):
        print("Todoist is already running")
    else:
        # sp.call(spotify_exe)
        sp.Popen(todolist_app)
        print("todolist launched")
        time.sleep(2)
