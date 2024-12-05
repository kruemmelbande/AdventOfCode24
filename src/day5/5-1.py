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
                print(f"update failed because {second} violates {i}")
                return False
    return True
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
for i in secondpart:
    if iscompliant(firstpart,i):
        awa = parsesecond(i)[int(len(parsesecond(i))/2)]
        total += awa
        print(f"true {i} {awa}")
    else:
        print("false" + i)
print(total)