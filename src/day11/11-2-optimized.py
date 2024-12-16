import sys
sys.set_int_max_str_digits(0) # We *probably* dont need this, but if itll run for ages, i dont want it to fail cuz the numbers get too large
#I just wanna be very clear, that this is not optimized for speed, but for ram usage. Its slower, but like, it doesnt make my laptop run out of memory instantly
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

def makeitbutlikegood(inputs, depth):
    if depth == 0:
        return 1
    newinputs = processNumber(inputs)
    total = 0
    if len(newinputs) == 1:
        return makeitbutlikegood(newinputs[0], depth-1)
    else:
        total += makeitbutlikegood(newinputs[0], depth-1)
        total += makeitbutlikegood(newinputs[1], depth-1)
        return total
    
def simulationStep(inputs):
    out = []
    for i in map(processNumber,inputs):
        for k in i:
            out.append(k)
    return out
total = 0
for i in inputs:
    total +=  makeitbutlikegood(i, 75)
print(total)