# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define unknown = Character("???")
define You = Character("...")
define Tamriel = Character("Tamriel")
default sleep = 10
define player = Character("[player_name]")

init python:
        
    testInput = "???:Mmmph#You:You roll over, trying to enjoy the sun’s warmth for a little longer.#You:The grass is cool, and gives the heat a comforting feeling.#You:…#You:Huh?#You:Grass? Sun?#???: Wha-?#"
    inputList = testInput.split("#")[:-1]
    #print(inputList)
    sleep = 10
    
    def readLine(textFileName):
        filepath = renpy.loader.transfn(textFileName)
        #filepath = textFileName
        with open(filepath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(readLines(line.strip()))
            
    def readLines(oneLine):
        oneLine = oneLine.split(":")
        if len(oneLine) != 2:
            changeStats(oneLine[2])
        user = oneLine[0]
        if user == "???":
            renpy.say(unknown, oneLine[1])
        if user == "You":
            renpy.say(You, oneLine[1])
        #renpy.say(e, oneLine[1])
        #return oneLine[0:2]
        return

    def changeStats(changes):
        changes = changes.split()
        if changes[0] == "sleep":
            if  changes[1] == "+":
                global sleep 
                sleep = sleep + int(changes[2])
        return True
        
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    python:
        for i in range(len(inputList)):
            readLines(inputList[i])
    
    $ player_name = renpy.input("What is your name?", length=32)
    $ player_name = player_name.strip()
    if not player_name:
        $ player_name = "1o8ryan"
    player "hello"
    # This ends the game.

    return
