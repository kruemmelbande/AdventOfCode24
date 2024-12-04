with open("inputs/4",'r') as f:
    puzzle = f.readlines()
    puzzle = [i.replace('\n','').strip() for i in puzzle]
count = 0
for i in range(1,len(puzzle)-1):
    for k in range(1,len(puzzle)-1):
        if puzzle[i][k] == "A":
            if (puzzle[i-1][k-1]=="M" and puzzle[i+1][k+1]=="S") or  (puzzle[i-1][k-1]=="S" and puzzle[i+1][k+1]=="M"):
                 if (puzzle[i+1][k-1]=="M" and puzzle[i-1][k+1]=="S") or  (puzzle[i+1][k-1]=="S" and puzzle[i-1][k+1]=="M"):
                    count+=1
print(count)