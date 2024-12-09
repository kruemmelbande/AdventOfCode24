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
print(result, len(result))
def is_same(arr, c):
    t = c #this used to be different, however, its like this. Why am i assigning a variable to another variable? I dont know. Why do i yap about it for 3 years instead of just deleting this line and changing the input to c? Cuz meow. I wanna go to sleep, its been a long day, my brain is not braining, but the grind never stops umu
    for i in arr:
        if i !=t:
            return False
    return True
def organize_array(arr):
    a=None
    for i in range(len(arr)):
        if not arr[len(arr)-i - 1] in (".",a) :
            stop = len(arr)-i -1
            a = arr[-i -1]
            start = stop
            while (start>0 and arr[start]==a):
                start = start-1
            start += 1
            print(f"{a} goes from {start} to {stop}")
            for k in range(len(arr)-(stop-start)):
                if is_same(arr[k:k+stop-start+1], ".") and k<start:
                    for j in range(stop-start+1):
                        arr[start+j] = "."
                        arr[k+j] = a
                        
                    break
            #print(arr)
            for i in range(len(arr)):
                if arr[i] == "#":
                    arr[i] == "."
organize_array(result)
total = 0 
for num,i in enumerate(result):
    if i != ".":
        total += num*i
print(result, len(result))
print(total)