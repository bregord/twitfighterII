import subprocess
import time

pathToEmu = "./StreetFighter2.sfc"

#left, up, right, down
p1DMaps= ['a', 'w', 'd', 's']
p2DMaps= ['k','o', ';', 'l']

#lshoulder, rshoulder, a, b, x, y
p1AMaps = ["q", "e", "f", "g", "c", "v"]
p2AMaps = ["i", "p", "h", "j", "n", "m"]

def resetState():
#use xdotool to reset to a saved state
   f = open("command","w") #opens file with name of "test.txt"
   f.write("key 1 key F3")
   f.close()

#takes a word, converts it to a move
def sendMove(player, moveList):

    commandString = ""

    for word in moveList:
        direction = playerMove(player, len(word) %4)
        commandString = commandString + direction

        for letter in word:
            button = ord(letter) % 6
            commandString += playerAction(player, button)

        if player == 1:
            commandString += " keyup --delay 50 " + p1DMaps[len(word) % 4]

        elif player == 2:
            commandString += " keyup --delay 50 " + p2DMaps[len(word) %4]

    sendCommand(commandString)


def sendCommand(commandString):
    f = open("command","w") #opens file with name of "test.txt"
    f.write(commandString)
    f.close()


def playerMove(player, direction):
    if(player ==1):

        return " keydown --delay 50 " + p1DMaps[direction]

    if(player ==2):
        return " keydown --delay 50 " + p2DMaps[direction]

def playerAction(player, button):

    if(player ==1):
        return " key --delay 50 " + p1AMaps[button]

    if(player ==2):
        return " key --delay 50" + p2AMaps[button]


def initGame():
    print("game started")
    strarg = "mednafen " + pathToEmu
    #subprocess.Popen(strarg, shell="True")
    subprocess.Popen(["mednafen", pathToEmu], shell="True")

    #speed up to character select
    #load the saved state
    #


