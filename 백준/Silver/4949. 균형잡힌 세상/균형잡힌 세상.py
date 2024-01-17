import sys

while True:
    stR = sys.stdin.readline().rstrip()
    stR_list = list()
    
    if stR == ".":
        break
        
    for i in stR:
        if i == "(":
            stR_list.append(i)
        elif i == ")":
            if stR_list and stR_list[-1] == "(":
                stR_list.pop()
            else:
                stR_list.append(i)
                break
        
        if i == "[":
            stR_list.append(i)
        elif i == "]":
            if stR_list and stR_list[-1] == "[":
                stR_list.pop()
            else:
                stR_list.append(i)
                break
                

    if stR_list == []:
        print("yes")
    else:
        print("no")