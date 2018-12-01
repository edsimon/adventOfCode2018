def firstRepeat() : # Loops circular until we found a duplicate freq
    i, freq, mySet = 0, 0, set()
    while(True) :
        for i in list:
            freq += i
            if (freq in mySet):
                return freq
            mySet.add(freq)

doc = open("../inputs/day1.txt", "r")
list = [x for x in map(int, doc.read().split())]

print( "Sum of all frequencies are {} and the first duplicate is {}."
       .format(sum(list),firstRepeat()))
doc.close()