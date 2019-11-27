def main() :
    fnames = []
    lnames = []
    hwAVG = []
    examAVG = []
    finalGrade = []

    file = open('./gradeinput.txt', 'r')
    while (file != None) :
        line = file.readline()
        line = line.split()

        if (line == []) :
            break

        name = line[0]
        i = name.index(",")
        fname = name[i+1::]
        lname = name[:i]

        fnames.append(fname)
        lnames.append(lname)

        line.pop(0)

        hwSUM = 0
        for i in range(15) :
            hwSUM += int(line[i])
        
        hwSUM = round(hwSUM / 15, 1)
        hwAVG.append(hwSUM)

        examSUM = 0
        for i in range(15, 18) :
            examSUM += int(line[i])
        
        examSUM = round(examSUM / 3, 1)
        examAVG.append(examSUM)

        finalGrade.append(round((hwSUM * 0.55 + examSUM * 0.45), 1))

    for i in range(len(fnames)) :
        print(lnames[i] + " " + fnames[i] + " | " + str(hwAVG[i]) + " | " + str(examAVG[i]) + " | " + str(finalGrade[i]))
    file.close()

main()