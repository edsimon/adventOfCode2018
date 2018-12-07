def build_moves(dic, moves) :
    l = set()
    for value in dic.values():
        for elem in value:
            l.add(elem)
    for key in dic.keys() :
        if not key in l:
            moves.add(key)
    return moves


def loop(dic) :
    moves = build_moves(dic, set())
    taken_moves = []
    while len(moves) > 0 :
        mo = min(moves)
        taken_moves.append(mo)
        if len(dic) == 1 :
            taken_moves.extend(dic[mo])
        del dic[mo]
        moves.remove(mo)
        moves = build_moves(dic, moves)
    return "".join(taken_moves)


def sort_info() :
    my_dict = {}
    for line in f :
        data = line.split(" ")
        finished = data[1]
        begin = data[7]
        if finished in my_dict.keys() :
            my_dict[finished].append(begin)
        else :
            my_dict[finished] = [begin]
    return my_dict


with open("../inputs/day7.txt", "r") as f :
    dic = sort_info()
    print("The path taken is \'{}\'"
          .format(loop(dic)))

