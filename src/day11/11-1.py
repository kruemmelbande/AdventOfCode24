with open("inputs/11","r") as f:
    inputs = list(map(int, f.readline().split()))

def processNumber(num):
    if num == 0:
        return [1]
    if len(str(num))%2==0:
        return [
            int(str(num)[:int(len(str(num))/2)]),
            int(str(num)[int(len(str(num))/2):])
            ]
    return [num*2024]

def simulationStep(inputs):
    out = []
    for i in map(processNumber,inputs):
        for k in i:
            out.append(k)
    return out
for i in range(25):
    inputs = simulationStep(inputs)
    print(i)
    print(len(inputs))