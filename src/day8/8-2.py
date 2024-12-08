with open('inputs/8','r') as f:
    inp = [[k for k in i.replace("\n",'').strip()] for i in f.readlines()]
    og = [i.copy() for i in inp]

letters = []
for i in og:
    for k in i:
        if k not in letters and k != ".":
            letters.append(k)

def printnicely(arr):
    for i in arr:
        print("".join(i))

def fillinterferance(og, inp, letter):
    found = []
    for x in range(len(og)):
        for y in range(len(og[0])):
            if og[x][y] == letter:
                found.append((x,y))
    for i in found:
        for k in found:
            if i == k:
                continue
            xd = i[0] - k[0]
            yd = i[1] - k[1]
            for a in range(-len(inp),len(inp)):
                point1 = ((k[0] - a*xd), (k[1] - a*yd))
                if 0<=point1[0]<len(inp) and 0<=point1[1]<len(inp[0]):
                    inp[point1[0]][point1[1]] = "#"

for letter in letters:
    fillinterferance(og,inp,letter)

printnicely(inp)
total = 0
for i in inp:
    for k in i:
        if k == "#":
            total+=1
print(total)