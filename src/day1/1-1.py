puzzleinput = open('inputs/1-1', 'r').readlines()
print(sum([abs(i-k) for i,k in zip(sorted([int(i.split()[0]) for i in puzzleinput]), sorted([int(i.split()[1]) for i in puzzleinput]))]))