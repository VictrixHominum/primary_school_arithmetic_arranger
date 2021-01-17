
def arithmetic_arranger(problems, answer=False):
    arranged_problems = ""
    tab = "    "

    if len(problems) > 5:
        return "Error: Too many problems."


    for i in range(len(problems)):
        dashes = ""
        problems[i] = problems[i].split()
        try:
            problems[i][0] = int(problems[i][0])
            problems[i][2] = int(problems[i][2])
        except:
            return 'Error: Numbers must only contain digits.'

        if problems[i][1] != '+' and problems[i][1] != '-':
            return "Error: Operator must be '+' or '-'."

        elif problems[i][0] > 9999 or problems[i][2] > 9999:
            return "Error: Numbers cannot be more than four digits."

        elif problems[i][1] == "+":
            problems[i].append(problems[i][0]+problems[i][2])

        else:
            problems[i].append(problems[i][0]-problems[i][2])

        problems[i][0] = str(problems[i][0])
        problems[i][2] = str(problems[i][2])
        problems[i][3] = str(problems[i][3])

        if len(problems[i][0]) >= len(problems[i][2]) and len(problems[i][0]) >= len(str(abs(int(problems[i][3])))):
            for j in range(len(problems[i][0])+2):
                if j > 5:
                    continue
                else:
                    dashes = dashes + "-"
            problems[i].insert(3, dashes)

        elif len(problems[i][2]) >= len(problems[i][0]) and len(problems[i][2]) >= len(str(abs(int(problems[i][3])))):
            for j in range(len(problems[i][2])+2):
                if j > 5:
                    continue
                else:
                    dashes = dashes+"-"
            problems[i].insert(3, dashes)

        else:
            for j in range(len(str(abs(int(problems[i][3]))+2))):
                if j > 5:
                    continue
                else:
                    dashes = dashes + "-"
            problems[i].insert(3, dashes)

    for item in range(len(problems)):
        for element in range(len(problems[item])):
            for space in range((len(problems[item][3])-len(problems[item][element]))):
                if element != 1 and element != 2:
                    problems[item][element] = " " + problems[item][element]
                elif element == 2:
                    spaces = len(problems[item][3]) - (len(problems[item][2])+1)
                    for count in range(spaces):
                        problems[item][2] = " " + problems[item][2]
        problems[item][2] = problems[item][1] + problems[item][2]
        problems[item].pop(1)

    if answer is True:
        for count in range(4):
            for item in range(len(problems)):
                if item < len(problems)-1:
                    arranged_problems = arranged_problems + problems[item][count] + tab
                else:
                    arranged_problems = arranged_problems + problems[item][count]
            if count < 3:
                arranged_problems = arranged_problems + "\n"

    else:
        for count in range(3):
            for item in range(len(problems)):
                if item < len(problems) - 1:
                    arranged_problems = arranged_problems + problems[item][count] + tab
                else:
                    arranged_problems = arranged_problems + problems[item][count]
            if count < 2:
                arranged_problems = arranged_problems + "\n"

    return arranged_problems
