import random
items = ["#"," "]
def generate():
    chunkx =[]
    o = 0
    while not(o == 8):
        chunklinex = []
        i = 0
        while not(i == 8):
            chunklinex.append(items[random.randint(0,1)])
            i = i + 1
        chunkx.append(chunklinex)
        o = o + 1 
    return chunkx
