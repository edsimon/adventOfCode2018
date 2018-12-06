from collections import Counter

'''
Todays part a is now superslow because i loop through -500 - 1000
to be able to filter out the infinite ones by eye. 
Look through the print and look for the first element that havent changed much.
'''
def create_map(dic) :
    world_map = dict()
    a = [ (i, j) for i in range(-500,1000) for j in range(-500, 1000)]
    for i in a :
        temp = 100000
        for key, value in dic.items() :
            dist = count_distance(i, value)
            if( dist is temp) :
                world_map[i] = -1
            if( dist < temp ) :
                world_map[i] = key
                temp = dist
    new_dic = Counter(world_map.values())
    print(new_dic)


def count_distance(t1, t2) :
    dist = abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])
    return dist


dic = dict()
with open("../inputs/day6.txt", "r") as f :
    for i, line in enumerate(f) :
        x, y = line.replace("\n", "").split(",")
        dic[i] = (int(x),int(y))
    create_map(dic)

