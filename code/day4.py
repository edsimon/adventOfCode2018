

def get_information(data):
    logs = []
    for log in data:
        info, msg = log.split("]")
        date, time = info.split()
        year, month, day = date.replace("[", "").split("-")
        hour, minute = (int(i) for i in time.split(":"))
        logs.append((year, month, day, hour, minute, msg))
    return sorted(logs)


def get_schedule(logs):
    l = {}
    idx = None
    for _, month, day, hour, minute, msg in logs:
        if "Guard" in msg:
            guard = msg.split()[1].replace("#", "")
            idx = (day, guard)
            l[idx] = []
        if "falls asleep" in msg:
            # begin sleeping
            l[idx].append([minute])
        if "wakes up" in msg:
            # wakes up
            l[idx][-1].append(minute)
    return l


def count_min(schedual) :
    mySet = dict()
    set_minutes = dict()
    for x, y in schedual.items() :
        if not x[1] in mySet.keys() :
            mySet[x[1]] = y
        elif not len(y) == 0 :
            mySet[x[1]].append(y[0])

    last_min = 0
    for key, value in mySet.items():
        minutes_asleep = [0]*60
        minutes = 0
        for val in value :
            minutes += val[1] - val[0]
            for i in range( val[0], val[1] ) :
                minutes_asleep[i] += 1
        set_minutes[key] = minutes
        if minutes > last_min :
            guard = key
            last_min = minutes
            most_worked_min = minutes_asleep.index(max(minutes_asleep))
    return guard, most_worked_min



file = open("../inputs/day4.txt", "r")
data = file.read().splitlines()
info = get_information(data)
schedual = get_schedule(info)
result = count_min(schedual)
print("Guard {} slept minute {} the most time.\nFinal ansver is {}"
      .format(result[0], result[1], int(result[0])*result[1]))
