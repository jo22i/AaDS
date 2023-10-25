import re

answer = 0

while True:
    try:
        val = input()
        substr = ""
        count = True
        for i in range(0, len(val)):
            if(val[i] == "-" and substr == ""):
                substr += val[i]
                count = True
            elif(val[i] >= '0' and val[i] <= '9'):
                substr += val[i]
                count = True
            else:
                count = False
            if(substr != "" and substr != "-" and not count):
                answer += int(substr)
                substr = ""

        if(substr != "-"):
            answer += int(substr)
    except EOFError:
        break
    except ValueError:
        continue

print(answer)