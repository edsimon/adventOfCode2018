import string

def get_char_value() :
    values = dict()
    for index, letter in enumerate(string.ascii_uppercase):
        values[letter] = index + 1
    return values

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
    print("T","A","B")
    w1, w2, w3, w4, w5 = True, True, True, True, True,
    w1_time, w2_time, w3_time, w4_time, w5_time = 0, 0, 0, 0, 0
    w1_elem, w2_elem, w3_elem, w4_elem, w5_elem = "", "", "", "", ""
    taken_moves = []
    moves, time = set(), 0
    moves = build_moves(dic, moves)
    while True:
        # for debugging
        if time == 0 :
            str = ""


        if w5 :
            w5_elem = "."
        if w4 :
            w4_elem = "."
        if w3 :
            w3_elem = "."
        if w2 :
            w2_elem = "."
        if w1 :
            w1_elem = "."



        if w1 and len(moves) > 0:
            w1_elem = min(moves)
            moves.remove(w1_elem)
            w1 = False
            w1_time = time + val[w1_elem] - 1 + 60

        if w2 and len(moves) > 0:
            w2_elem = min(moves)
            moves.remove(w2_elem)
            w2 = False
            w2_time = time + val[w2_elem] - 1 + 60

        if w3 and len(moves) > 0:
            w3_elem = min(moves)
            moves.remove(w3_elem)
            w3 = False
            w3_time = time + val[w3_elem] - 1 + 60

        if w4 and len(moves) > 0:
            w4_elem = min(moves)
            moves.remove(w4_elem)
            w4 = False
            w4_time = time + val[w4_elem] - 1 + 60

        if w5 and len(moves) > 0:
            w5_elem = min(moves)
            moves.remove(w5_elem)
            w5 = False
            w5_time = time + val[w5_elem] - 1 + 60

        elements = [w1_elem,w2_elem,w3_elem,w4_elem,w5_elem]

        if w1_time <= time and not w1:
            take_move(dic, w1_elem, moves, taken_moves)
            for e in elements :
                if e in moves : moves.remove(e)
            w1 = True

        if w2_time <= time and not w2:
            take_move(dic, w2_elem, moves, taken_moves)
            for e in elements :
                if e in moves : moves.remove(e)
            w2 = True
        if w3_time <= time and not w3:
            take_move(dic, w3_elem, moves, taken_moves)
            for e in elements :
                if e in moves : moves.remove(e)
            w3 = True
        if w4_time <= time and not w4:
            take_move(dic, w4_elem, moves, taken_moves)
            for e in elements :
                if e in moves : moves.remove(e)
            w4 = True
        if w5_time <= time and not w5:
            take_move(dic, w5_elem, moves, taken_moves)
            for e in elements :
                if e in moves : moves.remove(e)
            w5 = True



        print(time, "\t", w1_elem, w2_elem, w3_elem, w4_elem, w5_elem,  "  New Moves: ", moves)
        time += 1
        if len(moves) == 0 and w1 and w2 and w3 and w4 and w5:
            break
    return "".join(taken_moves)




def take_move(dic, mo, moves, taken_moves) :
    taken_moves.append(mo)
    temp = set()
    if len(dic) == 1:
        temp = dic[mo]
    if mo in dic.keys() : del dic[mo]
    build_moves(dic, moves)
    if len(dic) == 0 :
        moves.clear()
        if len(temp) > 0 :
            moves.add(temp[0])
#    print(dic)


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
    val = get_char_value()
    temp = loop(dic)
    print("The path taken is \'{}\'"
          .format(temp))

