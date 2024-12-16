with open("inputs/10", "r") as f:
    map = [list(map(int, i.replace("/n","").strip())) for i in f.readlines()]

def countDeduplicate(list):
    a = {}
    for i in list:
        a[str(i)] = 0
    return len(a)
def getScore(map, xi, yi):
    if map[xi][yi] != 0:
        
        return 0
    possiblePositions = [ [] for i in range(10)]
    possiblePositions[0] = [(xi,yi)]
    for i in range(10):
        if possiblePositions[i] == []:
            return 0
        for (x,y) in possiblePositions[i]:
            #print(x,y)
            try:
                if map[x][y+1] == i+1:
                    possiblePositions[i+1].append((x,y+1))
            except Exception:
                pass
            try:
                if map[x][y-1] == i+1 and y>0:
                    possiblePositions[i+1].append((x,y-1))
            except Exception:
                pass
            try:
                if map[x+1][y] == i+1:
                    possiblePositions[i+1].append((x+1,y))
            except Exception:
                pass
            try:
                if map[x-1][y] == i+1 and x>0:
                    possiblePositions[i+1].append((x-1,y))
            except Exception:
                pass
    return len(possiblePositions[9])
total = 0
for i in range(len(map)):
    for k in range(len(map[i])):
        print(f"{i},{k} {getScore(map, i,k)}", end="\n")
        total += getScore(map, i,k)
print(total)