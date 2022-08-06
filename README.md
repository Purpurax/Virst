# Vrist
This is a 2 in 1 python script for insta-locking agents in Valorant or having an automated option for the pick/banning-phase in League of Legends.

# How does it work?
Before: list all open windows and check if Valorant or League of Legends is open. If one is, then start the according function in the script.

Valorant: The goal is to click on given coordinates instantly after entering agent-pick-phase. So you need to recognize, if you are in the agent-pick-phase and then determined, where the agent is located.

I recognize the pick-phase, by checking the color of one pixel (in the top-left corner of the screen). The coords of every Agent are predefined manually and have to be changed after unlocking an agent or a new agent comes to the game. note: this can of course be automated too, if you put in a little more effort than me. Simple right?


League of Legends: This is a little harder, than in Valorant, because this script adapts to the response of the game. The goal here is to 1. click on accept, 2. select the champion you want, 3. ban a champ you hate the most, 4. lock your champ (if not available, pick another predefined champion), 5. choose summoner spells and runes. In here I used the picture finding tool of the package "pyautogui". This tool searches the whole screen for one picture and after finding it, it returns the coords of the center.

1. part is the most important and simplest because it just seeks the "accept-button"-picture until it finds it and then clicks on it. If someone dodges afterwards, you want to restart the script, that is the reason, why I'm always searching for a new "accept-button".
2. Unlike in Valorant, you can search for a champion's name. The "search-button"-picture gets clicked, and then it picks the first champ in the menu.
3. I create a small subfunction for the banning. The subfunction is like the second step and this time your desired ban might be disabled, your team wants to play that champ or this champ already got banned. If that is the case, it will try the function with another predefined champ again.
4. repeats step three similar.
And for the 5. Step, I use a coordinate grid. I just have to create an array of numbers, what will convert to coords later. Here is an example of an array of numbers: [1, 3, 1, 2, 0, 3, 1, 2, 4, 1, 0, 1]
 
Optional: Now I took an Arduino and made a small rotating cylinder and I made some of my favorite champs/agents as pixel art. If I click on the cylinder, a small menu pops up, with a variety of agents I can select. The pictures before are examples of these menus - in Valorant just some Agents in a row - in League of Legends sorted in roles.

# Why did I create "Vrist"?
Do you know the feeling, that you are waiting ages in a pick-screen and you want to do something else meanwhile, like eating or going to the bathroom? Vrist is the solution. I'm someone who wants to be as efficient as possible in anything and knows how to use Arduino and Python. So it wasn't hard creating this simple script. In addition to that, I already made a script similar to this (school-automation).
# How useful is it actually?
In Valorant it is saving about 1-3 minutes and gives me almost always the desired agent I want to play. For the second part to work, your internet connection has to be fast and consistent for a 100% success rate. The time saving in League of Legends ranges from 4-15 minutes, what is huge. The picking- and banning-phase in League of Legends is, in my opinion, way too long. I won't always get the champion I want, but my script is smart enough to adapt and pick something else.
# Can anyone create "Vrist" themselves?
Yes, programming seems to be very hard, but this is one of the perfect starting projects you can do with no real programming experience. In school you might learn some theoretical stuff, but here you make something useful and learn the same stuff on the go. I personally added more stuff, like the Arduino controls, than needed, because I'm not new to programming and wanted to train some electronics.
# Download
ATTENTION!!!: This is just the source-code and is adapted to MY pc. For personal use, you have to modify my version or create your own.

# http://purpurax.de/projects/vrist.html
