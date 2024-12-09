with open('inputs/9', 'r') as f:
    l = f.readline().replace('\n','').strip()
state = 1
result = []
for num,i in enumerate(l):
    if state:
        state = 0
        for k in range(int(i)):
            result.append(int(num/2))
    else:
        state = 1
        for k in range(int(i)):
            result.append(".")
for i in range(1,len(result)+1):
    print(f"{i} / {len(result)}",end='\r')
    if result[-i] != ".":
        for k in range(len(result)-i):
            if result[k] == ".":
                x,y = result[k],result[-i]
                result[k],result[-i] = y,x
                continue
total = 0 
for num,i in enumerate(result):
    if i != ".":
        total += num*i
print(result)
print(total)