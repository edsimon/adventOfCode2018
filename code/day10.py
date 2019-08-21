import re
import numpy as np
import matplotlib.pyplot as plt

class movable() :
    def __init__(self, x, y, vx, vy):
        self.x  = x
        self.y  = -y
        self.vx = vx
        self.vy = -vy

    def move(self) :
        self.x += 1*self.vx
        self.y += 1*self.vy


def pretty_print(list_of_members) :
    fig, ax = plt.subplots()
    for mem in list_of_members :
        ax.fill([mem.x, mem.x, mem.x + 1, mem.x + 1], [mem.y, mem.y + 1, mem.y + 1, mem.y], c="r")
    plt.show()



def move_all(number) :
    for i in range(number) :
        for mem in list_of_members:
            mem.move()
        pretty_print(list_of_members)
        print("number of moves: ", (i+1) + steps_ahed)




arr = np.ones((20,20))
list_of_coordinates = []
list_of_members = []

with open("../inputs/day10.txt", "r") as f :
    steps_ahed = 10635
    for row in f :
        (x, y, vx, vy) = list(map(int, re.findall("-?[\d]+", row)))
        list_of_members.append(movable(x, y, vx, vy))
    for mem in list_of_members :
        mem.x += mem.vx * steps_ahed
        mem.y += mem.vy * steps_ahed
    pretty_print(list_of_members)
    move_all(10)


