def dateIO() :
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    temp = input("Enter a year(Integer): ")
    year = int(temp)

    temp = input("Enter a month(String): ")
    if (temp.lower() in months) :
        month = temp.lower()
        index = months.index(month)
    else :
        return "Invalid month"

    temp = input("Enter a day(Integer): ")
    temp = int(temp) + 1
    while (temp >= monthDays[index]) :
        if (index == 1 and year % 4 == 0 and temp >= 29) :
            if (index == 1 and temp == 29) :
                break
            else :
                temp -= 1
        temp -= monthDays[index]
        index += 1
        if index > 11 :
            index -= 12
            year += 1
    month = months[index]
    day = temp

    return month.capitalize() + " " + str(day) + ", " + str(year)