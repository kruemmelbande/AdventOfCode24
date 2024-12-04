def countline(line):
    count = 0
    searchstring = 'XMAS'
    if len(line)<len(searchstring):
        return 0
    for i in range(len(line)-len(searchstring)+1):
        slice = line[i:i+len(searchstring)]
        if slice == searchstring or slice == "SAMX":
            count+=1
    print(line, count)
    return count
def countarr(arr):
    count = 0
    for i in arr:
        count += countline(i)
    return count
with open("inputs/4",'r') as f:
    puzzle = f.readlines()
    puzzle = [i.replace('\n','').strip() for i in puzzle]
count = 0
rotated = []
for i in range(len(puzzle[0])):
    rotated.append("".join([k[i] for k in puzzle]))
diagonal = []
for i in range(1,len(puzzle)):
    diagonal.append("".join([puzzle[i-k][k] for k in range(i+1)]))
    diagonal.append("".join([puzzle[i-k][-k-1] for k in range(i+1)]))
for i in range(1,len(puzzle)-1):
    diagonal.append("".join([puzzle[-i+k-1][-k-1] for k in range(i+1)]))
    diagonal.append("".join([puzzle[-i+k-1][k] for k in range(i+1)]))


#print(diagonal)
count += countarr(puzzle)
count += countarr(rotated)
count += countarr(diagonal)
print(count)
