def isSolvable(l):
    goal = l[0]
    operands = l[1:]
    operators = [0 for i in range(len(operands)-1)]
    operators[0] = -1
    for i in range(3**(len(operands)-1)):
        nextOperators(operators)
        if evauluate(operands,operators) == goal:
            return True
    return False
def nextOperators(operators):
    operators[0]+=1
    for i in range(len(operators)):
        if operators[i] > 2:
            operators[i] = 0
            operators[i+1] +=1

def evauluate(operands, operators):
    total = operands[0]
    i = 0 #id like to use enumerate, however, i fucking hate myself enough as is
    for a,b in zip(operands[1:],operators):
        i+=1
        match b:
            case 0:
                total*=a
            case 1:
                total+=a
            case 2:
                total = int(str(total)+str(a))
    return total
                
with open('inputs/7','r') as f:
    lines = [list(map(int,i.replace('\n','').replace(':','').strip().split())) for i in f.readlines()]

total = 0
for num,i in enumerate(lines):
    if isSolvable(i):
        print(f"{num}: {i} is solvable")
        total +=i[0]
    else:
        print(f"{num}: {i} is not solvable")
print(total)