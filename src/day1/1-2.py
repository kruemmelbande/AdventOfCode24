def count(arr, number):
    return sum([i == number for i in arr])
        
with open("inputs/1-1") as f:
    puzzleinput = f.readlines()
leftside = [int(i.split()[0]) for i in puzzleinput]
rightside = [int(i.split()[1]) for i in puzzleinput]
print(sum([i*count(rightside,i) for i in leftside]))