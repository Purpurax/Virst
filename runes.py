import time, pyautogui

#
#manual way of setting runes, if you stop script
#

p = pyautogui
time.sleep(3)


allRunes = {
    "Akali":        [0,  3, 2, 1, 2,   2,  4, 0, 0,   0, 0, 1],
    "Anivia":       [1,  0, 0, 2, 2,   0,  2, 4, 0,   1, 0, 2],
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
print("What champion do you want to play as?")
pick = ""
inpyt = input()
while inpyt not in allRunes:
    if inpyt == "help":
        print(list(allRunes))
    else:
        print("!No runes for this champion, please take another.")
    inpyt = input()
pick = inpyt

runes = allRunes[pick]

delaytime = 0.1
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
p.write(pick)
p.press('enter')
time.sleep(delaytime*2)
p.moveTo(2430, 460, delaytime, pyautogui.easeInOutQuad) #save
p.click()
p.moveTo(2663, 732, delaytime, pyautogui.easeInOutQuad) #yes/no
p.click()
p.moveTo(3090, 420, delaytime, pyautogui.easeInOutQuad) #escape
p.click()