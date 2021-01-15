from obswebsocket import obsws, requests
import os

ws = obsws("localhost", 4444, "secret")

def connect():
    try:
        ws.connect()
        return True
    except:
        return False

def RunObs():
    os.chdir(r"C:\Program Files\obs-studio\bin\64bit")
    os.startfile("obs64.exe")

def disconnect():
    ws.disconnect()

def ChangeScenes(scene):
    ws.call(requests.SetCurrentScene(scene))