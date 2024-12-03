with open('inputs/3', 'r') as f:
    data = f.read()
state=0
total=0
number1 = 0
number2 = 0

for i in data:
    print(f"{i}\t state {state}")
    if state == 0:
        number1 = 0
        number2 = 0
    match i:
        case "m":
            state = 1
            curmul = "m"
        case "u":
            if state == 1:
                state = 2
            else:
                state = 0
        case "l":
            if state == 2:
                state = 3
            else:
                state = 0
        case "(":
            if state == 3:
                state = 4
            else:
                state = 0
        case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0": 
            if state in [4,5,6]: 
                number1 = number1*10+int(i)
                state +=1
            elif state in [8,9,10]:
                number2 = number2*10+int(i)
                state +=1
            else:
                state = 0
        case ",":
            if state in [5,6,7]:
                state = 8
            else:
                state = 0
        case ")":
            if state in [9,10,11]:
                total += number1 * number2
                print(f"found numbers {number1} and {number2} ({number1*number2})")
            state = 0
        case _:
            state = 0
print(total)