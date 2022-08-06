import pyautogui, time, sys, webbrowser, subprocess
from pywinauto import Desktop

p = pyautogui

exitOnEnd = False

def Start():
    global exitOnEnd
    game = ""

    #checking if game is set as a script argument, if not ask for the game
    if len(sys.argv) < 2:
        print("What game?")
        game = input()
        while not game.startswith("v") and not game.startswith("l"):
            if game == "help":
                print("v - valorant  or  l - league of legends")
            game = input()
    else:
        game = sys.argv[1]

    if game.startswith("v"):
        Valorant()
    elif game.startswith("ln"):
        exitOnEnd = True
        LeagueOfLegends()
    elif game.startswith("l"):
        LeagueOfLegends()
        
    print("please try again")
    subprocess.run("python main.py")


def Valorant():
    #coords of agent(newest agent fade), window-mode-2560x1440
    agent = sys.argv[2]
    pos = (0, 0)
    if len(agent) != 0:
        if agent == "Astra":
            pos = (2090, 1200)
        elif agent == "Breach":
            pos = (2190, 1200)
        elif agent == "Brimstone":
            pos = (2300, 1200)
        elif agent == "Chamber":
            pos = (2400, 1200)
        elif agent == "Cypher":
            pos = (2510, 1200)
        elif agent == "Fade":
            pos = (2610, 1200)
        elif agent == "Jett":
            pos = (2720, 1200)
        elif agent == "Kayo":
            pos = (2830, 1200)
        elif agent == "Killjoy":
            pos = (2930, 1200)
        elif agent == "Neon":
            pos = (3040, 1200)
            #second row
        elif agent == "Omen":
            pos = (2090, 1200)
        elif agent == "Phoenix":
            pos = (2190, 1300)
        elif agent == "Raze":
            pos = (2300, 1300)
        elif agent == "Reyna":
            pos = (2400, 1300)
        elif agent == "Sage":
            pos = (2510, 1300)
        elif agent == "Skye":
            pos = (2610, 1300)
        elif agent == "Sova":
            pos = (2720, 1300)
        elif agent == "Viper":
            pos = (2820, 1300)
        elif agent == "Yoru":
            pos = (2930, 1300)
        else:
            pos = (2720, 1300) #default: Sova
    else:
        print("Sova")
        pos = (2720, 1300) #default: Sova

    yrt = (0, 0, 0) #the pixel that changes in lock screen to -> (51, 173, 228)

    def InstaLock():
        p.moveTo(pos[0], pos[1], 0.05, pyautogui.easeOutQuad) #agent
        p.click()
        p.click()
        p.moveTo(2550, 1050, 0.05, pyautogui.easeOutQuad) #lock in
        p.click()
        subprocess.run("python main.py") #end

    while True:
        try: yrt = p.pixel(1360, 40)
        except: yrt = (0, 0, 0)
        if yrt == (51, 173, 228):
            InstaLock()
        yrt = (0, 0, 0)



ban, mode, role, allRoles, banningOptions, pickOptions, allRunes, pick = (None,) * 8

def LeagueOfLegends():
    global ban, mode, role, allRoles, banningOptions, pickOptions, allRunes, pick, exitOnEnd
    ban = ["Yasuo", "Blitz"] #default ban
    mode = "draft"
    role = "bot"
    allRoles = ["top", "jungle", "mid", "support", "bot"]
    banningOptions = [["Jax", "Teemo", "Vayne"],    ["Master", "Kayn", "Warwick"],    ["Yasuo", "Malzahar", "Yone"],    ["Yasuo", "Blitz", "Evelynn"],    ["Yasuo", "Blitz", "Evelynn"]] #from top-2 to bot-2
    pickOptions = [["Irelia", "Akali", "Jayce"],    ["Evelynn", "Nunu", "Vi"],    ["Akali", "Veigar", "Irelia"],    ["Soraka", "Morgana", "Pantheon"],    ["Kaisa", "Jinx", "Ashe"]] #from top-3 to bot-3
    allRunes = {
        "Aatrox":       [0,  3, 1, 0, 2,   2,  4, 2, 2,   0, 0, 1],
        "Akali":        [0,  3, 2, 1, 2,   2,  4, 0, 0,   0, 0, 1],
        "Anivia":       [1,  0, 0, 2, 2,   0,  2, 4, 0,   1, 0, 2],
        "Aurelion":     [1,  0, 1, 2, 2,   3,  4, 2, 2,   1, 0, 2],
        "Ashe":         [0,  1, 2, 2, 0,   3,  4, 2, 1,   1, 0, 1],
        "Caitlyn":      [0,  2, 2, 2, 0,   1,  4, 2, 2,   1, 0, 1],
        "Evelynn":      [1,  0, 2, 2, 1,   1,  4, 2, 2,   0, 0, 1],
        "Ezreal":       [4,  2, 1, 2, 0,   0,  2, 2, 4,   1, 0, 1],
        "Garen":        [0,  3, 1, 1, 2,   2,  4, 0, 0,   0, 0, 1],
        "Irelia":       [0,  3, 1, 0, 2,   2,  4, 2, 2,   1, 0, 2],
        "Janna":        [4,  0, 1, 2, 0,   3,  1, 4, 1,   2, 0, 1],
        "Jax":          [0,  1, 1, 0, 2,   3,  1, 4, 2,   0, 0, 1],
        "Jayce":        [2,  2, 1, 2, 2,   3,  1, 2, 4,   0, 0, 1],
        "Jinx":         [0,  1, 2, 2, 1,   0,  1, 4, 0,   1, 0, 1],
        "Kaisa":        [1,  3, 1, 2, 0,   3,  1, 2, 4,   1, 0, 1],
        "Kassadin":     [1,  0, 1, 2, 3,   2,  4, 2, 0,   0, 0, 2],
        "Lux":          [2,  1, 1, 0, 0,   1,  0, 4, 3,   0, 0, 1],
        "Miss Fortune": [2,  1, 1, 2, 0,   3,  1, 2, 4,   1, 0, 1],
        "Morgana":      [2,  1, 1, 0, 2,   3,  2, 4, 0,   2, 0, 1],
        "Nunu":         [2,  2, 2, 1, 1,   0,  1, 1, 4,   1, 0, 1],
        "Ornn":         [3,  0, 0, 1, 0,   3,  1, 2, 0,   1, 1, 1],
        "Pantheon":     [0,  0, 1, 0, 0,   0,  0, 4, 2,   0, 0, 1],
        "Riven":        [0,  3, 1, 0, 2,   1,  4, 0, 2,   0, 0, 1],
        "Samira":       [0,  3, 1, 2, 2,   0,  4, 2, 0,   1, 0, 1],
        "Senna":        [0,  2, 2, 0, 0,   3,  4, 2, 1,   0, 0, 1],
        "Sona":         [2,  0, 1, 0, 2,   2,  4, 0, 1,   0, 0, 1],
        "Soraka":       [2,  0, 1, 0, 0,   2,  4, 2, 1,   0, 0, 1],
        "Talon":        [0,  3, 1, 1, 2,   3,  1, 2, 4,   0, 0, 1],
        "Teemo":        [0,  0, 1, 0, 2,   0,  0, 4, 0,   1, 0, 1],
        "Varus":        [1,  3, 1, 2, 0,   3,  4, 2, 0,   1, 0, 1],
        "Veigar":       [1,  1, 1, 2, 1,   1,  1, 0, 4,   1, 0, 1],
        "Vi":           [1,  3, 2, 2, 1,   0,  1, 0, 4,   1, 0, 1],
        "Warwick":      [0,  0, 1, 0, 2,   1,  4, 1, 1,   1, 0, 1],
        "Xayah":        [0,  1, 1, 2, 0,   3,  1, 2, 4,   1, 0, 1]
        }
    pick = []
    
    #check if champ, role, gamemode is defined as script argument, if not ask for the variables
    if len(sys.argv) <= 2:
        print("What champion do you want to play as?")
        inpyt = input()
        while inpyt not in allRunes:
            if inpyt == "help":
                print(list(allRunes))
            else:
                print("!No runes for this champion, please take another.")
            inpyt = input()
        pick.append(inpyt)
        print("Where do you want to play this champion?")
        inpyt = input()
        while inpyt not in allRoles:
            if inpyt == "help":
                print(list(allRoles))
            else:
                print("!No role found that matches, please take another one.")
            inpyt = input()
        role = inpyt
        print("What Gamemode are you playing?")
        mode = input()
        if mode == "":
            mode = "draft"
    else:
        pick.append(sys.argv[2])
        role = sys.argv[3]
    

    def draftPick():
        global ban, mode, role, allRoles, banningOptions, pickOptions, allRunes, pick
        print("draft mode")
        #accepting
        acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
        while acceptButton == None:
            acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
        try:
            print("Accepting")
            p.moveTo(acceptButton.x, acceptButton.y, 0.5, pyautogui.easeInOutQuad)
            p.doubleClick()
            p.move(0, 200, 0.5, pyautogui.easeInOutQuad)
        except:
            print("Error clicking Accept")
        acceptButton = None
        time.sleep(1)

        #if declined accept again or declare champ
        def accept():
            acceptButton2 = p.locateCenterOnScreen('Images/LoL-Accept.png')
            declareButton = p.locateCenterOnScreen('Images/LoL-Declare-Champion.png')
            while acceptButton2 == None and declareButton == None:
                acceptButton2 = p.locateCenterOnScreen('Images/LoL-Accept.png')
                declareButton = p.locateCenterOnScreen('Images/LoL-Declare-Champion.png')
            if acceptButton2 != None:
                print("Accepting again")
                try:
                    p.moveTo(acceptButton2.x, acceptButton2.y, 0.5, pyautogui.easeInOutQuad)
                    p.doubleClick()
                    p.move(0, 200, 0.5, pyautogui.easeInOutQuad)
                except:
                    print("Error finding searchbar")
                return False
            else:
                print("Declaring champ")
                return True

        while accept() == False:
            pass
        ##declare champ
        #check for role
        declaredRole = ""
        top = p.locateCenterOnScreen('Images/LoL-Role-Top.png', confidence=0.8)
        jungle = p.locateCenterOnScreen('Images/LoL-Role-Jungle.png', confidence=0.8)
        mid = p.locateCenterOnScreen('Images/LoL-Role-Mid.png', confidence=0.8)
        support = p.locateCenterOnScreen('Images/LoL-Role-Support.png', confidence=0.8)
        bot = p.locateCenterOnScreen('Images/LoL-Role-Bot.png', confidence=0.8)
        if top != None:
            declaredRole = "top"
            print("declared top")
        elif jungle != None:
            declaredRole = "jungle"
            print("declared jungle")
        elif mid != None:
            declaredRole = "mid"
            print("declared mid")
        elif support != None:
            declaredRole = "support"
            print("declared support")
        elif bot != None:
            declaredRole = "bot"
            print("declared bot")
        else:
            declaredRole = role
            print("declared your role")

        #getting pick/ban according to role
        if declaredRole != role:
            if declaredRole == "top":
                pick = pickOptions[0]
            elif declaredRole == "jungle":
                pick = pickOptions[1]
            elif declaredRole == "mid":
                pick = pickOptions[2]
            elif declaredRole == "support":
                pick = pickOptions[3]
            elif declaredRole == "bot":
                pick = pickOptions[4]
        if declaredRole == "top":
            ban = banningOptions[0]
            pick.extend(pickOptions[0])
        elif declaredRole == "jungle":
            ban = banningOptions[1]
            pick.extend(pickOptions[1])
        elif declaredRole == "mid":
            ban = banningOptions[2]
            pick.extend(pickOptions[2])
        elif declaredRole == "support":
            ban = banningOptions[3]
            pick.extend(pickOptions[3])
        elif declaredRole == "bot":
            ban = banningOptions[4]
            pick.extend(pickOptions[4])
        if pick[0] in ban:
            ban.remove(pick[0])
        pick = list(dict.fromkeys(pick))
        role = declaredRole

        #declare champ
        declChampion = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Search.png', region=(1700, 250, 3500, 1000), confidence=0.9)
        while declChampion == None:
            declChampion = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Search.png', region=(1700, 250, 3500, 1000), confidence=0.9)
            acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
            if acceptButton != None:
                draftPick()
                return
        try:
            print("declaring " + pick[0])
            p.moveTo(declChampion.x + 165, declChampion.y, 0.2, pyautogui.easeInOutQuad)
            p.doubleClick()
            p.write(pick[0])
        except:
            print("Error finding searchbar")
        
        time.sleep(1)
        p.moveTo(2305, 502, 0.2, pyautogui.easeInOutQuad)
        p.click()

        #banning
        banPhase = p.locateCenterOnScreen('Images/LoL-Ban-Champion.png', region=(1700, 250, 3500, 1000))
        while banPhase == None:
            banPhase = p.locateCenterOnScreen('Images/LoL-Ban-Champion.png', region=(1700, 250, 3500, 1000))
            acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
            if acceptButton != None:
                draftPick()
                return
        print("banPhase")
        
        def banning(i):
            banChampion = p.locateCenterOnScreen('Images/LoL-Ban-Champion-Search.png', region=(1700, 250, 3500, 1000), confidence=0.9)
            while banChampion == None:
                banChampion = p.locateCenterOnScreen('Images/LoL-Ban-Champion-Search.png', region=(1700, 250, 3500, 1000), confidence=0.9)
                acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
                if acceptButton != None:
                    draftPick()
                    return
            try:
                print("banning " + ban[i])
                p.moveTo(banChampion.x + 165, banChampion.y, 0.5, pyautogui.easeInOutQuad)
                p.doubleClick()
                p.write(ban[i])
            except:
                print("Error finding searchbar")
            
            banTop = p.locateCenterOnScreen('Images/LoL-Ban-Champion-First.png', region=(1700, 250, 3500, 1000))
            while banTop == None:
                banTop = p.locateCenterOnScreen('Images/LoL-Ban-Champion-First.png', region=(1700, 250, 3500, 1000))
                acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
                if acceptButton != None:
                    draftPick()
                    return
            try:
                p.moveTo(banTop.x+ 25, banTop.y + 50, 0.5, pyautogui.easeInOutQuad)
                p.click()
            except:
                print("Error finding searbar")
            
            banButton = p.locateCenterOnScreen('Images/LoL-Ban-Champion-Button.png', region=(1700, 250, 3500, 1000))
            banButtonDisabled = p.locateCenterOnScreen('Images/LoL-Ban-Champion-Button-disabled.png', region=(1700, 250, 3500, 1000))
            while banButton == None and banButtonDisabled == None:
                banButton = p.locateCenterOnScreen('Images/LoL-Ban-Champion-Button.png', region=(1700, 250, 3500, 1000))
                banButtonDisabled = p.locateCenterOnScreen('Images/LoL-Ban-Champion-Button-disabled.png', region=(1700, 250, 3500, 1000))
                acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
                if acceptButton != None:
                    draftPick()
                    return
            if banButton != None:
                print("ban works")
                try:
                    p.moveTo(banButton.x, banButton.y, 0.5, pyautogui.easeInOutQuad)
                    p.click()
                    time.sleep(0.5)
                    banButtonCancel = p.locateCenterOnScreen('Images/LoL-Ban-Champion-Cancel.png', region=(1700, 250, 3500, 1000))
                    if banButtonCancel != None:
                        p.moveTo(banButtonCancel.x, banButtonCancel.y, 0.5, pyautogui.easeInOutQuad)
                        p.click()
                        time.sleep(0.5)
                        return False
                except:
                    print("Error finding searchbar")
                time.sleep(3)
                return True
            else:
                print("ban's not working")
                return False
        for i in range(len(ban)):
            if banning(i):
                break

        #picking
        pickPhase = p.locateCenterOnScreen('Images/LoL-Pick-Champion.png', region=(1700, 250, 3500, 1000), confidence=0.5)
        while pickPhase == None:
            pickPhase = p.locateCenterOnScreen('Images/LoL-Pick-Champion.png', region=(1700, 250, 3500, 1000), confidence=0.5)
            acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
            if acceptButton != None:
                draftPick()
                return
        print("pickPhase")

        pickChampion = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Search.png', region=(1700, 250, 3500, 1000), confidence=0.8)
        while pickChampion == None:
            pickChampion = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Search.png', region=(1700, 250, 3500, 1000), confidence=0.8)
            acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
            if acceptButton != None:
                draftPick()
                return
            
        pickTop = p.locateCenterOnScreen('Images/LoL-Pick-Champion-First.png', region=(1700, 250, 3500, 1000), confidence=0.8)
        while pickTop == None:
            pickTop = p.locateCenterOnScreen('Images/LoL-Pick-Champion-First.png', region=(1700, 250, 3500, 1000), confidence=0.8)
            acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
            if acceptButton != None:
                draftPick()
                return

        picked = ""

        def picking(i):
            try:
                print("picking " + pick[i])
                p.moveTo(pickChampion.x + 165, pickChampion.y, 0.5, pyautogui.easeInOutQuad)
                p.doubleClick()
                p.write(pick[i])
            except:
                print("Error finding searchbar")

            try:
                p.moveTo(pickTop.x+ 25, pickTop.y + 50, 0.5, pyautogui.easeInOutQuad)
                p.click()
            except:
                print("Error finding searchbar")
                
            pickButton = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Button.png', region=(1700, 250, 3500, 1000), confidence=0.9)
            pickButtonDisabled = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Button-disabled.png', region=(1700, 250, 3500, 1000), confidence=0.9)
            while pickButton == None and pickButtonDisabled == None:
                pickButton = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Button.png', region=(1700, 250, 3500, 1000), confidence=0.9)
                pickButtonDisabled = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Button-disabled.png', region=(1700, 250, 3500, 1000), confidence=0.9)
                acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
                if acceptButton != None:
                    draftPick()
                    return
            if pickButton != None:
                try:
                    p.moveTo(pickButton.x, pickButton.y, 0.5, pyautogui.easeInOutQuad)
                    p.click()
                except:
                    print("Error finding searchbar")
                if pick[i].lower() != "kaisa": #don't open website for my main Kai'sa 
                    webbrowser.open('https://u.gg/lol/champions/' + pick[i] + '/build') #some recommendation for a good build
                return True
            else:
                print("Cannot pick your preferred champion!")
                return False
        for i in range(len(pick)):
            if picking(i):
                picked = pick[i]
                break
            
        #runes
        time.sleep(2)
        runes = allRunes[picked]

        acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
        if acceptButton != None:
            draftPick()
            return

        delaytime = 0.15
        p.moveTo(2500, 1020, delaytime, pyautogui.easeInOutQuad)
        p.click()
        p.moveTo(2500, 740, delaytime, pyautogui.easeInOutQuad)
        p.click()
        p.moveTo(2350, 1020, delaytime, pyautogui.easeInOutQuad)
        p.click()
        time.sleep(0.5) #rune page
        p.moveTo(2160 + (40*runes[0]), 550, delaytime, pyautogui.easeInOutQuad)
        p.click()
        if runes[0] <= 1:
            p.moveTo(2160 + (50*runes[1]), 670, delaytime, pyautogui.easeInOutQuad)
            p.click()
        else:
            p.moveTo(2170 + (70*runes[1]), 670, delaytime, pyautogui.easeInOutQuad)
            p.click()
        
        acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
        if acceptButton != None:
            draftPick()
            return

        p.moveTo(2170 + (70*runes[2]), 770, delaytime, pyautogui.easeInOutQuad)
        p.click()
        p.moveTo(2170 + (70*runes[3]), 860, delaytime, pyautogui.easeInOutQuad)
        p.click()
        if runes[0] == 1:
            p.moveTo(2160 + (50*runes[4]), 940, delaytime, pyautogui.easeInOutQuad)
            p.click()
        else:
            p.moveTo(2170 + (70*runes[4]), 940, delaytime, pyautogui.easeInOutQuad)
            p.click()

        acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
        if acceptButton != None:
            draftPick()
            return
        
        p.moveTo(2490 + (50*runes[5]), 550, delaytime, pyautogui.easeInOutQuad)
        p.click()
        p.moveTo(2500 + (65*runes[6]), 640, delaytime, pyautogui.easeInOutQuad)
        p.click()
        p.moveTo(2500 + (65*runes[7]), 720, delaytime, pyautogui.easeInOutQuad)
        p.click()
        if runes[0] == 0 and runes[5] == 0 or runes[0] > 1 and runes[5] == 1:
            p.moveTo(2490 + (50*runes[8]), 800, delaytime, pyautogui.easeInOutQuad)
            p.click()
        else:
            p.moveTo(2500 + (65*runes[8]), 800, delaytime, pyautogui.easeInOutQuad)
            p.click()

        p.moveTo(2500 + (65*runes[9]), 855, delaytime, pyautogui.easeInOutQuad)
        p.click()
        p.moveTo(2500 + (65*runes[10]), 900, delaytime, pyautogui.easeInOutQuad)
        p.click()
        p.moveTo(2500 + (65*runes[11]), 945, delaytime, pyautogui.easeInOutQuad)
        p.click()
        
        acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
        if acceptButton != None:
            draftPick()
            return

        #rename and save
        p.moveTo(2080, 465, delaytime*2, pyautogui.easeInOutQuad)
        p.click()
        p.hotkey('ctrl', 'a')
        p.press('backspace')
        p.write(picked)
        p.press('enter')
        p.moveTo(2430, 460, delaytime, pyautogui.easeInOutQuad) #save
        p.click()
        time.sleep(1.5)
        #p.moveTo(2663, 732, delaytime, pyautogui.easeInOutQuad) #yes/no
        #p.click()
        p.moveTo(3090, 420, delaytime, pyautogui.easeInOutQuad) #escape
        p.click()

        #spells
        time.sleep(1)
        p.moveTo(2610, 1020, delaytime, pyautogui.easeInOutQuad) #slot 1
        p.click()
        p.moveTo(2660, 810, delaytime, pyautogui.easeInOutQuad) #flash
        p.click()
        
        p.moveTo(2650, 1020, delaytime, pyautogui.easeInOutQuad) #slot 2
        p.click()
        if role == "jungle": #smite
            p.moveTo(2600, 880, delaytime, pyautogui.easeInOutQuad) #slot 1
            p.click()
        elif role == "support" or role == "bot": #exhaust
            p.moveTo(2600, 810, delaytime, pyautogui.easeInOutQuad) #slot 1
            p.click()
        else: #tp
            p.moveTo(2660, 880, delaytime, pyautogui.easeInOutQuad) #slot 1
            p.click()
        
        #anti dodge
        RoundStartTimer = time.time() + 60
        while RoundStartTimer > time.time():
            acceptButton = p.locateCenterOnScreen('Images/LoL-Accept.png')
            if acceptButton != None:
                draftPick()
                return
    #might not work!!!
    def CustomPick():
        picked = pick[0]
        pickPhase = p.locateCenterOnScreen('Images/LoL-Pick-Champion.png', region=(1700, 250, 3500, 1000))
        while pickPhase == None:
            pickPhase = p.locateCenterOnScreen('Images/LoL-Pick-Champion.png', region=(1700, 250, 3500, 1000))
        print("pickPhase")

        #runes
        time.sleep(1)
        runes = allRunes[picked]

        delaytime = 0.1
        p.moveTo(2500, 1020, delaytime*5, pyautogui.easeInOutQuad)
        p.click()
        p.moveTo(2500, 740, delaytime*2, pyautogui.easeInOutQuad)
        p.click()
        p.moveTo(2350, 1020, delaytime*3, pyautogui.easeInOutQuad)
        p.click()
        time.sleep(0.2) #rune page
        p.moveTo(2160 + (40*runes[0]), 550, delaytime, pyautogui.easeInOutQuad)
        p.click()
        if runes[0] <= 1:
            p.moveTo(2160 + (50*runes[1]), 670, delaytime, pyautogui.easeInOutQuad)
            p.click()
        else:
            p.moveTo(2170 + (70*runes[1]), 670, delaytime, pyautogui.easeInOutQuad)
            p.click()
        
        p.moveTo(2170 + (70*runes[2]), 770, delaytime, pyautogui.easeInOutQuad)
        p.click()
        p.moveTo(2170 + (70*runes[3]), 860, delaytime, pyautogui.easeInOutQuad)
        p.click()
        if runes[0] == 1:
            p.moveTo(2160 + (50*runes[4]), 940, delaytime, pyautogui.easeInOutQuad)
            p.click()
        else:
            p.moveTo(2170 + (70*runes[4]), 940, delaytime, pyautogui.easeInOutQuad)
            p.click()

        
        p.moveTo(2490 + (50*runes[5]), 550, delaytime, pyautogui.easeInOutQuad)
        p.click()
        p.moveTo(2500 + (65*runes[6]), 640, delaytime, pyautogui.easeInOutQuad)
        p.click()
        p.moveTo(2500 + (65*runes[7]), 720, delaytime, pyautogui.easeInOutQuad)
        p.click()
        if runes[0] == 0 and runes[5] == 0 or runes[0] > 1 and runes[5] == 1:
            p.moveTo(2490 + (50*runes[8]), 800, delaytime, pyautogui.easeInOutQuad)
            p.click()
        else:
            p.moveTo(2500 + (65*runes[8]), 800, delaytime, pyautogui.easeInOutQuad)
            p.click()

        p.moveTo(2500 + (65*runes[9]), 855, delaytime, pyautogui.easeInOutQuad)
        p.click()
        p.moveTo(2500 + (65*runes[10]), 900, delaytime, pyautogui.easeInOutQuad)
        p.click()
        p.moveTo(2500 + (65*runes[11]), 945, delaytime, pyautogui.easeInOutQuad)
        p.click()

        #rename and save
        p.moveTo(2080, 465, delaytime*2, pyautogui.easeInOutQuad)
        p.click()
        p.hotkey('ctrl', 'a')
        p.press('backspace')
        p.write(picked)
        p.press('enter')
        p.moveTo(2430, 460, delaytime, pyautogui.easeInOutQuad) #save
        p.click()
        p.moveTo(2663, 732, delaytime, pyautogui.easeInOutQuad) #yes/no
        p.click()
        p.moveTo(3090, 420, delaytime, pyautogui.easeInOutQuad) #escape
        p.click()

        #spells
        time.sleep(1)
        p.moveTo(2610, 1020, delaytime, pyautogui.easeInOutQuad) #slot 1
        p.click()
        p.moveTo(2660, 810, delaytime, pyautogui.easeInOutQuad) #flash
        p.click()
        
        p.moveTo(2650, 1020, delaytime, pyautogui.easeInOutQuad) #slot 2
        p.click()
        if role == "jungle": #smite
            p.moveTo(2600, 880, delaytime, pyautogui.easeInOutQuad) #slot 1
            p.click()
        else: #tp
            p.moveTo(2660, 880, delaytime, pyautogui.easeInOutQuad) #slot 1
            p.click()
            
        
        pickChampion = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Search.png', region=(1700, 250, 3500, 1000), confidence=0.9)
        while pickChampion == None:
            pickChampion = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Search.png', region=(1700, 250, 3500, 1000), confidence=0.9)
        try:
            print("picking " + picked)
            p.moveTo(pickChampion.x + 165, pickChampion.y, 0.5, pyautogui.easeInOutQuad)
            p.doubleClick()
            p.write(picked)
        except:
            print("Error finding searchbar")
        
        
        p.moveTo(2300, 500, 0.5, pyautogui.easeInOutQuad)
        p.click()
            
        pickButton = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Button.png', region=(1700, 250, 3500, 1000))
        while pickButton == None:
            pickButton = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Button.png', region=(1700, 250, 3500, 1000))
        if pickButton != None:
            try:
                p.moveTo(pickButton.x, pickButton.y, 0.5, pyautogui.easeInOutQuad)
                p.click()
            except:
                print("Error finding searchbar")
        else:
            print("Cannot pick your preferred champion!")
    #might not work!!!
    def CustomDraftPick():
        #banning
        banPhase = p.locateCenterOnScreen('Images/LoL-Ban-Champion.png', region=(1700, 250, 3500, 1000))
        while banPhase == None:
            banPhase = p.locateCenterOnScreen('Images/LoL-Ban-Champion.png', region=(1700, 250, 3500, 1000))
        print("banPhase")
        
        def banChampion(ban):
            banChampion = p.locateCenterOnScreen('Images/LoL-Ban-Champion-Search.png', region=(1700, 250, 3500, 1000), confidence=0.9)
            while banChampion == None:
                banChampion = p.locateCenterOnScreen('Images/LoL-Ban-Champion-Search.png', region=(1700, 250, 3500, 1000), confidence=0.9)
            try:
                print("banning " + ban)
                p.moveTo(banChampion.x + 165, banChampion.y, 0.5, pyautogui.easeInOutQuad)
                p.doubleClick()
                p.write(ban)
            except:
                print("Error finding searchbar")
            
            banTop = p.locateCenterOnScreen('Images/LoL-Ban-Champion-First.png', region=(1700, 250, 3500, 1000))
            while banTop == None:
                banTop = p.locateCenterOnScreen('Images/LoL-Ban-Champion-First.png', region=(1700, 250, 3500, 1000))
            try:
                p.moveTo(banTop.x+ 25, banTop.y + 50, 0.5, pyautogui.easeInOutQuad)
                p.click()
            except:
                print("Error finding searbar")
            
            banButton = p.locateCenterOnScreen('Images/LoL-Ban-Champion-Button.png', region=(1700, 250, 3500, 1000))
            banButtonDisabled = p.locateCenterOnScreen('Images/LoL-Ban-Champion-Button-disabled.png', region=(1700, 250, 3500, 1000),)
            while banButton == None and banButtonDisabled == None:
                banButton = p.locateCenterOnScreen('Images/LoL-Ban-Champion-Button.png', region=(1700, 250, 3500, 1000))
                banButtonDisabled = p.locateCenterOnScreen('Images/LoL-Ban-Champion-Button-disabled.png', region=(1700, 250, 3500, 1000))
            if banButton != None:
                print(".found real banbutton")
                try:
                    p.moveTo(banButton.x, banButton.y, 0.5, pyautogui.easeInOutQuad)
                    p.click()
                    time.sleep(0.5)
                except:
                    print("Error finding searchbar")
                return True
            else:
                print(".didn't find any banbutton")
                return False

        successfulBans = 0
        for i in range(len(banningOptions)):
            if banChampion(banningOptions[i]):
                successfulBans += 1
            if successfulBans >= 3:
                break
        
        #picking
        pickPhase = p.locateCenterOnScreen('Images/LoL-Pick-Champion.png', region=(1700, 250, 3500, 1000))
        while pickPhase == None:
            pickPhase = p.locateCenterOnScreen('Images/LoL-Pick-Champion.png', region=(1700, 250, 3500, 1000))
        print("pickPhase")
        
        pickChampion = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Search.png', region=(1700, 250, 3500, 1000), confidence=0.9)
        while pickChampion == None:
            pickChampion = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Search.png', region=(1700, 250, 3500, 1000), confidence=0.9)
        try:
            print("picking " + pick)
            p.moveTo(pickChampion.x + 165, pickChampion.y, 0.5, pyautogui.easeInOutQuad)
            p.doubleClick()
            p.write(pick)
        except:
            print("Error finding searchbar")
        
        pickTop = p.locateCenterOnScreen('Images/LoL-Pick-Champion-First.png', region=(1700, 250, 3500, 1000))
        while pickTop == None:
            pickTop = p.locateCenterOnScreen('Images/LoL-Pick-Champion-First.png', region=(1700, 250, 3500, 1000))
        try:
            p.moveTo(pickTop.x+ 25, pickTop.y + 50, 0.5, pyautogui.easeInOutQuad)
            p.click()
        except:
            print("Error finding searchbar")
            
        pickButton = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Button.png', region=(1700, 250, 3500, 1000))
        pickButtonDisabled = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Button-disabled.png', region=(1700, 250, 3500, 1000))
        while pickButton == None and pickButtonDisabled == None:
            pickButton = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Button.png', region=(1700, 250, 3500, 1000))
            pickButtonDisabled = p.locateCenterOnScreen('Images/LoL-Pick-Champion-Button-disabled.png', region=(1700, 250, 3500, 1000))
        if pickButton != None:
            try:
                p.moveTo(pickButton.x, pickButton.y, 0.5, pyautogui.easeInOutQuad)
                p.click()
            except:
                print("Error finding searchbar")
        else:
            print("Cannot pick your preferred champion!")

    if mode == "draft":
        draftPick()
    elif mode == "custom":
        CustomPick()
    elif mode == "custom-draft":
        CustomDraftPick()
    
    if not exitOnEnd:
        subprocess.run("python main.py") #end
    



Start()