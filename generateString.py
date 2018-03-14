from random import *
from datetime import datetime

charList = ['0', '1', '2', '3', '4', '5', '6',
 '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

nCharacters = input("# of Characters: ")
nRounds = input("# of Rounds: ")
rndBuffer = ""

for x in range(nRounds):
    seed(datetime.now())
    for i in range(nCharacters):
        rndBuffer += sample(charList, 1)[0]
    print rndBuffer
    rndBuffer = ""
print "\nExiting\n"
