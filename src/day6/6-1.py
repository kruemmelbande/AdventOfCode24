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
                    if map[nx][ny] in [".","X"]:
                        map[nx][ny] = k
                        map[x][y] = "X"
                        break
                    else:
                        map[x][y] = d[2]
                    break
            else:
                continue
            break
        print("\[H")
        for i in map:
            for k in i:
                print(k,end="")
            print()
        print()
        return (True, 0)
    except:
        count = 0
        for x,i in enumerate(map):
            for y,k in enumerate(i):
                if k in directions or k == "X":
                    count += 1
        return (False,count)
while True:
    result = simulationstep(map)
    if not result[0]:
        print(result[1])
        break