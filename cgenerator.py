import random
items = ["#"," ","&","@"]
def generate():
    lnyh = len(items) - 1
    chunkx =[]
    o = 0
    while not(o == 8):
        chunklinex = []
        i = 0
        while not(i == 8):
            chunklinex.append(items[random.randint(0,lnyh)])
            i = i + 1
        chunkx.append(chunklinex)
        o = o + 1 
    return chunkx