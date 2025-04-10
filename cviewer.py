import os

def printc(chunk):
    i = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    while not(i == 7):
        chunklinex = chunk[i]
        print(chunklinex[0],chunklinex[1],chunklinex[2],chunklinex[3],chunklinex[4],chunklinex[5],chunklinex[6],chunklinex[7])
        i = i + 1
