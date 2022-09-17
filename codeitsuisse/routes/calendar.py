import datetime
from datetime import date


def find_day(year, num):
    curr_date = date.fromordinal(date(year, 1, 1).toordinal() + num - 1)
    month = str(curr_date)[5:7]
    if month[0] == 0:
        month = int(month[1])
    else:
        month = int(month)
    day = int(curr_date.weekday())
    return month, day


def find_date(year, month, day):
    date_of_month = datetime.datetime(year, month, 1)
    first_day_of_month = int(date_of_month.weekday())
    first_day_of_year = datetime.datetime(year, 1, 1).toordinal()
    # day = 0 - 6
    if day < first_day_of_month:
        num = 7 - first_day_of_month + day
        return (date_of_month.toordinal() + num + 1) - first_day_of_year
    else:
        num = day - first_day_of_month
        return (date_of_month.toordinal() + num + 1) - first_day_of_year


def calendar_part1(numbers):
    year = numbers[0]
    days = sorted(list(x for x in list(set(numbers[1:])) if 1 <= x <= 365))
    temp = []
    for i in range(12):
        temp.append([" "]*7)

    # 0 = monday
    day_list = ["m", "t", "w", "t", "f", "s", "s"]
    for i in days:
        month, day = find_day(year, i)
        temp[month-1][day] = day_list[day]

    res = ""
    temp2 = ["".join(i) for i in temp]
    for i in range(12):
        if temp2[i] == "mtwtf  ":
            temp2[i] = "weekday"
        elif temp2[i] == "     ss":
            temp2[i] = "weekend"
        elif temp2[i] == "mtwtfss":
            temp2[i] = "alldays"
    return ",".join(temp2) +","


def calendar_part2(month_num):
    temp = month_num.split(",")[:12]
    year = 0

    flag = False
    for i in temp:
        if i != "       ":
            for j in range(7):
                if i[j] == ' ':
                    year = 2001 + j
                    flag = True
                    break
        if flag:
            break

    if year == 0:
        return [2001]
    else:
        res = [year]

    for i in range(len(temp)):
        if temp[i] != "       ":
            if temp[i] == "weekend":
                res.append(find_date(year,i+1,5))
                res.append(find_date(year,i+1,6))
            elif temp[i] == "weekday":
                for x in range(5):
                    res.append(find_date(year, i + 1, x))
            elif temp[i] == "alldays":
                for x in range(7):
                    res.append(find_date(year, i+1, x))
            else:
                for x in range(7):
                    if temp[i][x] != ' ':
                        res.append(find_date(year, i+1, x))
    return res

