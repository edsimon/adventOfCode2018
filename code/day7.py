import string
number_of_workers = 5
add_to_time = 60

'''############# Class ############'''
# Create a class worker to remove code duplication
class Worker:
    not_buzy = True
    time_to_work = 0
    element = "."

    def take_work(self, time, moves):
        if self.not_buzy and len(moves) > 0:
            self.element = min(moves)
            moves.remove(self.element)
            self.not_buzy = False
            self.time_to_work = time + val[self.element] - 1 + add_to_time

    def finish_work(self, time, moves, taken_moves, elements):
        if self.time_to_work <= time and not self.not_buzy:
            take_move(dic, self.element, moves, taken_moves)
            for e in elements :
                if e in moves : moves.remove(e)
            self.not_buzy = True


############# Main Loop ###############
# This is main loop
def loop(dic) :
    taken_moves, workers, moves, time = [], [], set(), 0
    moves = build_moves(dic, moves)
    for i in range(number_of_workers):
        workers.append(Worker())
    while True:
        elements = []

        for worker in workers :
            worker.take_work(time, moves)
            elements.append(worker.element)

        for worker in workers :
            worker.finish_work(time, moves, taken_moves, elements)
            if worker.not_buzy :
                worker.element = "."

        pretty_print(time, elements, moves)

        # Basecase for when we are finished
        if ["."]*number_of_workers == elements :
            return "".join(taken_moves), time
        time += 1


############ Helper Functions #############
# Just prints the workprocess in a nice way
def pretty_print(time, elements, moves) :
    if len(moves) == 0: temp = ""
    else: temp = moves
    if time >= 100 : space = " "
    else : space = "\t "
    print(time, space, *elements, "  new:", *temp)


# Create a dict with char as key and value is what number the letter is
def get_char_value() :
    values = dict()
    for index, letter in enumerate(string.ascii_uppercase):
        values[letter] = index + 1
    return values


#Builds the dict in creation and updating the main dictionay
# that contains all possible relations
def build_moves(dic, moves) :
    l = set()
    for value in dic.values():
        for elem in value:
            l.add(elem)
    for key in dic.keys() :
        if not key in l:
            moves.add(key)
    return moves


# takes a move and then update the dict
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


# Sort the information to appear in right form
def sort_info() :
    my_dict = {}
    for line in f :
        data = line.split(" ")
        begin, finished = data[7], data[1]
        if finished in my_dict.keys() :
            my_dict[finished].append(begin)
        else :
            my_dict[finished] = [begin]
    return my_dict


# Open the file and starts the computing
with open("../inputs/day7.txt", "r") as f :
    dic = sort_info()
    val = get_char_value()
    str, time = loop(dic)
    print("The path taken is \'{}\' and the time for it to take is {}"
          .format(str, time))

