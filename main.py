import obs
from time import sleep
from pywinauto import backend

desktop = backend.registry.backends['uia'].element_info_class()
order = ["ContentLeftPanel", "Meeting Tools", ""]
corresponding = {'not in meeting':'Default', 'muted':'Idling', 'unmuted':'Talking'}

def main():
    #run up obs
    if not obs.connect():
        obs.RunObs()
        obs.connect()
    prev = 'not in meeting'
    while True:
        app = DetectZoomMeeting()
        status = 'not in meeting'
        if app != -1:
            status = CheckStatus(app, 0)
        if prev != status:
            obs.ChangeScenes(corresponding[status])
        prev = status
        sleep(0.01)

def DetectZoomMeeting():
    for app in desktop.children():
        if app.name[-12:] == "Zoom Meeting":
            return app
    return -1

def CheckStatus(app, depth):
    if depth == 3:
        return "muted" if app.children()[1].name.split(',')[0] == 'Unmute' else "unmuted"
    for i in app.children():
        if i.name == order[depth]:
            return CheckStatus(i, depth+1)

if __name__=="__main__":
    main()