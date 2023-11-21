from random import choice
from os import system as cmd
from winsound import Beep
from time import sleep as wait, time
from forcegpu import forceGPU
from requests import get
def clr(): cmd("cls")
clr()
intro = "Welcome to SCORED!\nA game where LUCK decides your score!"

class HighScoreClass:
    def getHighScore(self):
        with open("hs.txt", "r") as file:
            return file.read()
        
    def isHighScore(self, score:float):
        if float(self.getHighScore()) < score:
            return True
        else:
            return False
        
    def changeHighScore(self, score:float):
        with open("hs.txt", "w") as file:
            file.write(str(score))
    def rawReadHSfile(self):
        with open("hs.txt", "r") as file:
            return file.read()
        
        
class OnlineClass:
    def __init__(self):
        self.OnlineHS = get("https://raw.githubusercontent.com/fin-github/Scored/main/Online/hs.txt").text
    def ableToConnect(self):
        if get("https://raw.githubusercontent.com/fin-github/Scored/main/Online/hs.txt").status_code == 200:
            return True
        else:
            return False
    def isHighScore(self, score:int):
        if int(self.OnlineHS) < score:
            return True
        else:
            return False
        
Online = OnlineClass()   
HighScore = HighScoreClass()
            
def playround():
    if choice(["Cow", "Moose", "Sheep"]) ==  choice(["Cow", "Moose", "Sheep"]):
        return True
    else:
        return False
def playgame():
    score = 0
    for i in range(0,1000):
        if playround() is True:
            score+=1
            win=True
        else:
            win=False
        print(f"Round {i}, Win={win}")
    return score
        
def gpucheck():
    with open("useGPU.txt", "r") as file:
        if file.read() == "True":
            clr()
            print("WARNING: Forcing GPU usage. You will see colors pop up...")
            wait(5)
            forceGPU()
            return True
        else:
            return False



print(intro)
input("\n\nPress ENTER to start!")
clr()
Beep(1000, 1000)
print("Starting")

if HighScore.rawReadHSfile() == '':
    print("DETECTED FIRST TIME USE. Now fixing HS.txt file.")
    with open("hs.txt", "w") as file:
        file.write("1")
    print("Complete.")
    wait(1)
    clr()
    
    
clr()
gpuon = gpucheck()


print("Now starting game!!!")
wait(3)
Beep(2000, 500)
Beep(1000, 500)
Beep(2000, 500)
start = time()
score = playgame()
end = time()
wait(3)



timetook = end-start
hs = HighScore.isHighScore(score=score)
currenths = HighScore.getHighScore()
if hs: HighScore.changeHighScore(score)
clr()
print(f"""
      ----Stats----
      Completed in: {str(timetook)[:5]}
      Score: {score} out of 1000
      Used GPU: {gpuon}
      ----Highscore---
      Highscore: {currenths}
      Higher than Highscore: {hs}
      {'New high score!' if hs else ''}
      ----Online----
      Connected?: {Online.ableToConnect()}
      Higher than Online Highscore: {Online.isHighScore(score)}
      Online Highscore (MAY BE OUTDATED): {Online.OnlineHS}
      """)
