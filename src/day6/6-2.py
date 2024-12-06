with open('inputs/6','r') as f:
    map =[[a for a in i.replace('\n','').strip()] for i in f.readlines()]
def simulationstep(map):
    try:
        directions={
            "^": (-1,0,">"),
            ">": (0,1, "v"),
            "v": (1,0, "<"),
            "<": (0,-1,"^")
        }
        for x,i in enumerate(map):
            for y,k in enumerate(i):
                if k in directions:
                    d = directions[k]
                    nx = x+d[0]
                    ny = y+d[1]
                    if nx <0 or ny < 0:
                        0/0
                    if map[nx][ny] in [".","X"]:
                        map[nx][ny] = k
                        map[x][y] = "."
                        break
                    else:
                        map[x][y] = d[2]
                    break
            else:
                continue
            break
        if 0:
            print('\n')
            for i in map:
                for k in i:
                    print(k,end="")
                print()
            
        return True
    except Exception:
        count = 0
        return False

def compare(map1,map2):
    for i,k in zip(map1,map2):
        for a,b in zip(i,k):
            if a!=b:
                #print(a,b)
                return False
    return True


count = 0
for i,_ in enumerate(map):
    for k,_ in enumerate(map[0]):
        if map[i][k] != ".":
            continue
        newmap = [i.copy() for i in map.copy()]
        newmap[i][k] = "#"
        goal = [i.copy() for i in newmap.copy()]
        lim = 0
        while True:
            lim +=1
            res = simulationstep(newmap)
            if not res:
                print(f"[{i}][{k}] doesnt loop")
                break
            #if newmap == goal:
            if lim > len(map) * len(map[0]) or compare(newmap,goal):
                count += 1
                print(f"[{i}][{k}] loops")
                break
print(count)