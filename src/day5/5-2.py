import random
with open('inputs/5','r') as f:
    file = f.readlines()
firstpart = []
secondpart = []
amogus = 0
def parsefirst(item):
    item = list(map(int, item.split('|')))
    return item
def parsesecond(item):
    item = list(map(int, item.split(',')))
    return item
def getindexof(mylist, item):
    for num,i in enumerate(mylist):
        if i == item:
            return num
    print(f"Failed to find item {item} in {mylist}.")
    return 0
def iscompliant(first,second):
    nfirst = [parsefirst(i) for i in first]
    nsecond = parsesecond(second)
    for i in nfirst:
        if i[0] in nsecond and i[1] in nsecond:
            if getindexof(nsecond,i[0]) > getindexof(nsecond,i[1]):
                #print(f"update failed because {second} violates {i}")
                return (False, getindexof(nsecond,i[0]), getindexof(nsecond,i[1]))
    return (True,0,0)
for i in file:
    if i == '\n':
        amogus = 1
        continue
    if amogus:
        secondpart.append(i.replace('\n','').strip())
    else: 
        firstpart.append(i.replace('\n','').strip())
print(firstpart)
print(secondpart)
total = 0
for num,i in enumerate(secondpart):
    if iscompliant(firstpart,i)[0]:
        print(f"line {num} is compliant ({i})")
        pass
    else:
        print(f'line {num} is NOT compliant ({i})')
        k=0
        newline = i
        while True:
            k+=1
            awa = parsesecond(newline)
            #print(awa)
            awa = list(map(str, awa))
            (a,b,c) = iscompliant(firstpart,newline)
            if a:
                break
            newindex=b
            awa[newindex],awa[c] = awa[c], awa[newindex] #This is a terrible and awfully slow approach to doing it, however, in this case itll still finish in a couple of seconds, so realistically its fine
            newline = ",".join(awa)
            
            #print(f"try {k}",end='\r')
        total+=parsesecond(newline)[int(len(parsesecond(newline))/2)]
        print(f"\nSolution found for {i}. {newline} in {k} steps ")
print(total)