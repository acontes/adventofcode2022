file1 = open('input.txt', 'r')
# A, X : rock : 1
# B, Y Paper : 2 
# C, Z : Scissor: 3
dict = {"A":1,"B":2, "C":3, "X":1, "Y":2, "Z":3 }
LOST = 0
DRAW = 3
WIN = 6

total = 0

while True:
    line = file1.readline()
    if not line:
        break
    actions = line.split()
    match actions[0]:
        case "A":
            match actions[1]:
                case "X":
                    #lost
                    total += dict["Z"] + LOST
                case "Y":
                    # draw
                    total += dict["X"] + DRAW
                case "Z":
                    # win
                    total += dict["Y"] + WIN
        case "B":
            match actions[1]:
                case "X":
                    # draw
                    total += dict["X"] + LOST
                case "Y":
                    # win
                    total += dict["Y"] + DRAW
                case "Z":
                    #lost
                    total += dict["Z"] + WIN
        case "C":
            match actions[1]:
                case "X":
                    # win
                    total += dict["Y"] + LOST
                case "Y":
                    #lost
                    total += dict["Z"] + DRAW
                case "Z":
                    # draw
                    total += dict["X"] + WIN


print(total)
