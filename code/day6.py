from collections import Counter
'''
Todays part a is now superslow because i loop through -500 - 1000
to be able to filter out the infinite ones by eye. 
Look through the print and look for the first element that havent changed much.
'''
def create_map(dic, width, height) :
    world_map = dict()
    a = [ (i, j) for i in range(width,height) for j in range(width, height)]
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
    return new_dic


''' Part b method to solve the size of area '''
def count_area(dic) :
    a = [(i, j) for i in range(0,350) for j in range(0, 350)]
    count = 0
    for i in a :
        limit, length = 10000, 0
        for value in dic.values() :
            length += count_distance(i, value)
        if length < limit :
            count += 1
    return count

''' Compare two diffrent dicts and takes the biggest value that is the same 
    for both dicts. That value must be the largest not infinite number'''
def find_biggest_area(dic) :
    distances = []
    dic_one = create_map(dic, 0, 350)
    dic_two = create_map(dic, -1, 351)
    for key, value in dic_one.items() :
        if value == dic_two[key] :
            distances.append(value)
    return (max(distances))

''' Counts the manhattan distance '''
def count_distance(t1, t2) :
    dist = abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])
    return dist


with open("../inputs/day6.txt", "r") as f :
    dic = dict()
    for i, line in enumerate(f) :
        x, y = line.replace("\n", "").split(",")
        dic[i] = (int(x),int(y))
    print("Largest area is {} and the location area for part b is {}"
          .format(find_biggest_area(dic), count_area(dic)))