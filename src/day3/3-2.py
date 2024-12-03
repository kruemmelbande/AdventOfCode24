with open('inputs/3', 'r') as f:
    data = f.read()
state = 0 
estate = 0 #do()'nt()
total = 0
enabled  = True
number1 = 0
number2 = 0

for i in data:
    print(f"{i}\t state {state}, estate {estate}, enabled {enabled}")
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
                total += number1 * number2 * enabled
                print(f"found numbers {number1} and {number2} ({number1*number2}) enabled: {enabled}")
            state = 0
        case _:
            state = 0
    match i:
        case "d":
            estate = 1
        case "o":
            if estate == 1:
                estate = 2
            else:
                estate = 0
        case "n":
            if estate == 2:
                estate = 5
            else:
                estate = 0
        case "'":
            if estate == 5:
                estate = 6
            else:
                estate = 0
        case "t":
            if estate == 6:
                estate = 7
            else:
                estate = 0
        case "(":
            if estate == 2:
                estate = 3
            elif estate == 7:
                estate = 8
            else:
                estate = 0
        case ")":
            if estate == 3:
                enabled = True
                print("Enabled")
            if estate == 8:
                print("Disabled")
                enabled = False
            estate = 0
        case _:
            estate = 0
print(total)