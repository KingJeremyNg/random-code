def main() :
    data = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
    }
    
    file = open('./2009CensusData.txt', 'r')
    line = file.readline().split()
    while (file) :
        line = file.readline().split()

        if (line == []) :
            break

        value = line[-1]
        data[value[:1]] += 1
    
    total = 0
    for key in data :
        total += data[key]

    print("{0:^10}{1:^10}{2:^10}".format("Digit", "Count", "%"))
    for key in data :
        print("{digit:^10}{count:^10}{percent:^10}".format(digit = key, count = data[key], percent = round((data[key]/total) * 100, 1)))

main()