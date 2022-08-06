import serial, subprocess, win32gui, time
from tkinter import *
from PIL import Image, ImageTk

ser = None
sensitivity = 3
frameTime = 0.3
level = 0
game = ""
timer = time.time() + 60
frame = 1

class LeagueOfLegends():
    pic = []
    currentpic = []
    lanes = []
    role = ""
    
    def __init__(self):
        global pic, currentpic, lanes
        print("League of Legends")
        #drawing menu on screen
        root = Tk()
        root.geometry('658x130+2230+1310')
        root.overrideredirect(1)
        root.configure(background="black")
        root.wm_attributes("-topmost", True)
        root.wm_attributes("-disabled", True)
        
        #convert gif to image
        def gifToIm(path):
            imary = []
            im = Image.open(path)
            for i in range(im.n_frames):
                im.seek(i)
                imary.append(ImageTk.PhotoImage(im.copy().resize((128, 128), Image.NEAREST)))
            return imary

        pic = {
            "empty":                gifToIm('Art/empty-64.gif'),
            "top":                  gifToIm('Images/role-Top.gif'),
            "jungle":               gifToIm('Images/role-Jungle.gif'),
            "mid":                  gifToIm('Images/role-Mid.gif'),
            "support":              gifToIm('Images/role-Support.gif'),
            "bot":                  gifToIm('Images/role-Bot.gif'),
            "Akali":                gifToIm('Art/Akali-Kda.gif'),
            "Caitlyn":              gifToIm('Art/Caitlyn.gif'),
            "Evelynn":              gifToIm('Art/Evelynn-Kda-All-out.gif'),
            "Irelia":               gifToIm('Art/Irelia.gif'),
            "Jax":                  gifToIm('Art/Jax.gif'),
            "Jinx":                 gifToIm('Art/Jinx.gif'),
            "Kaisa":                gifToIm('Art/Kaisa-Kda.gif'),
            "Samira":               gifToIm('Art/Samira.gif'),
            "Soraka":               gifToIm('Art/Soraka.gif')
        }
        lanes = {
            "empty":    ["top", "jungle", "mid", "support", "bot"],
            "top":      ["Irelia", "Jax", "empty", "empty", "empty"],
            "jungle":   ["Evelynn", "Jax", "empty", "empty", "empty"],
            "mid":      ["Akali", "Irelia", "empty", "empty", "empty"],
            "support":  ["Soraka", "empty", "empty", "empty", "empty"],
            "bot":      ["Kaisa", "Caitlyn", "Jinx", "Samira", "empty"]
        }
        currentpic = ["top", "jungle", "mid", "support", "bot"]

        #drawing the boxes of champions in order 
        Label(root, image=pic[currentpic[0]][frame], bg="black").grid(row=0, column=0, sticky=EW)
        for i in range(1, 5):
            Label(root, image=pic[currentpic[i]][0], bg="black").grid(row=0, column=i, sticky=EW) #spacing=4px
        
        self.loop(root, ser)

    def setPics(self, root):
        global currentpic
        highlightedPic = (level//sensitivity)%5
        for i in range(5):
            if i == highlightedPic:
                Label(root, image=pic[currentpic[i]][frame], bg="black").grid(row=0, column=i, sticky=EW)
            else:
                Label(root, image=pic[currentpic[i]][0], bg="black").grid(row=0, column=i, sticky=EW)

    def loop(self, root, ser):
        global level, currentpic, role, frame
        lastFrameTime = time.time()
        while True:
            root.update()
            s =  str(ser.readline())
            s = s[2:len(list(s))-5]

            if lastFrameTime + frameTime < time.time():
                lastFrameTime = time.time()
                frame += 1
                if frame >= len(pic[currentpic[(level//sensitivity)%5]]):
                    frame = 1
                self.setPics(root)
            if s.startswith("Position: "):
                if level-sensitivity >= int(s[10:]): #negative direction of arduino-potentiometer
                    lastFrameTime = time.time()
                    level = int(s[10:])
                    frame = 1
                    self.setPics(root)
                elif level+sensitivity <= int(s[10:]): #positive direction of arduino-potentiometer
                    lastFrameTime = time.time()
                    level = int(s[10:])
                    frame = 1
                    self.setPics(root)
            elif s.startswith("Button: "): #button of arduino-potentiometer
                rur = currentpic[(level//sensitivity)%5]
                if rur in lanes:
                    role = rur
                    currentpic = lanes[rur]
                else:
                    print("playing " + str(rur) + " on lane " + str(role))
                    root.destroy()
                    ser.close()
                    subprocess.run("python games.py l " + str(rur) + " " + str(role))
                self.setPics(root)
            #if user is not doing anything menu disappers after x seconds
            if timer < time.time():
                root.destroy()
                PreStart()


    
class Valorant():
    pic = []
    currentpic = []
    role = ""
    
    def __init__(self):
        global pic, currentpic
        print("Valorant")
        #drawing menu on screen
        root = Tk()
        root.geometry('658x130+2230+1310')
        root.overrideredirect(1)
        root.configure(background="black")
        root.wm_attributes("-topmost", True)
        root.wm_attributes("-disabled", True)

        #convert gif to image
        def gifToIm(path):
            imary = []
            im = Image.open(path)
            for i in range(im.n_frames):
                im.seek(i)
                imary.append(ImageTk.PhotoImage(im.copy().resize((128, 128), Image.NEAREST)))
            return imary
            
        pic = {
            "empty":                gifToIm('Art/empty-64.gif'),
            "Chamber":              gifToIm('Art/Chamber.gif'),
            "Cypher":               gifToIm('Art/Cypher.gif'),
            "Jett":                 gifToIm('Art/Jett.gif'),
            "Sage":                 gifToIm('Art/Sage.gif'),
            "Sova":                 gifToIm('Art/Sova.gif')
        }

        currentpic = ["Cypher", "Sova", "Sage", "Jett", "Chamber"]

        #drawing the boxes of champions in order 
        Label(root, image=pic[currentpic[0]][frame], bg="black").grid(row=0, column=0, sticky=EW)
        for i in range(1, 5):
            Label(root, image=pic[currentpic[i]][0], bg="black").grid(row=0, column=i, sticky=EW) #spacing=4px
        
        self.loop(root, ser)

    def setPics(self, root):
        global currentpic
        highlightedPic = (level//sensitivity)%5
        for i in range(5):
            if i == highlightedPic:
                Label(root, image=pic[currentpic[i]][frame], bg="black").grid(row=0, column=i, sticky=EW)
            else:
                Label(root, image=pic[currentpic[i]][0], bg="black").grid(row=0, column=i, sticky=EW)

    def loop(self, root, ser):
        global level, currentpic, role, frame
        lastFrameTime = time.time()
        while True:
            root.update()
            s =  str(ser.readline())
            s = s[2:len(list(s))-5]

            if lastFrameTime + frameTime < time.time():
                lastFrameTime = time.time()
                frame += 1
                if frame >= len(pic[currentpic[(level//sensitivity)%5]]):
                    frame = 1
                self.setPics(root)
            if s.startswith("Position: "):
                if level-sensitivity >= int(s[10:]): #negative direction of arduino-potentiometer
                    lastFrameTime = time.time()
                    frame = 1
                    level = int(s[10:])
                    self.setPics(root)
                elif level+sensitivity <= int(s[10:]): #positive direction of arduino-potentiometer
                    lastFrameTime = time.time()
                    frame = 1
                    level = int(s[10:])
                    self.setPics(root)
            elif s.startswith("Button: "): #button of arduino-potentiometer
                rur = currentpic[(level//sensitivity)%5]
                if rur == "empty":
                    root.destroy()
                    PreStart()
                else:
                    print("playing " + str(rur))
                    root.destroy()
                    ser.close()
                    subprocess.run("python games.py v " + str(rur))
            #if user is not doing anything menu disappers after x seconds
            if timer < time.time():
                root.destroy()
                PreStart()



#reseting script
def PreStart():
    global ser, level, game, timer, frame

    #reset variables
    level = 0
    game = ""
    frame = 1

    while ser == None:
        time.sleep(1)
        try: ser = serial.Serial('COM5', 9600, timeout=1) #the port, where the arduino communicates
        except: pass

    while True:
        s =  str(ser.readline())
        s = s[2:len(list(s))-5]
        if s.startswith("Button: "):
            print("searching Game...")
            break
    timer = time.time() + 60
    Start()


def Start():
    win = []

    #getting every window name
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != "":
            win.append(win32gui.GetWindowText(hwnd))
    win32gui.EnumWindows(winEnumHandler, None)

    for i in range(len(win)):
        if "VALO" in win[i]:
            Valorant()
        if "League of" in win[i]:
            LeagueOfLegends()

    print("no Game open, please try again")
    PreStart()

PreStart()