def count_letters(oneRow, two=0, three=0):
    my_set = set()
    for elem in oneRow: my_set.add(elem)
    for letter in my_set:
        elemCount = 0
        for elem in oneRow :
            if (letter is elem) :
                elemCount += 1
        if elemCount is 2 and two < 1 : two += 1
        if elemCount is 3 and three < 1 : three += 1
    return (two, three)


def check_sum() :
    for line in list_of_words :
        two, three = count_letters(line)
        total[0] += two
        total[1] += three
    return total[0] * total[1]


def find_id() :
    for line1 in list_of_words :
        for line2 in list_of_words : # takes two lines to compare
            final_str = ""
            for i in range(len(line1)) :
                if (line1[i] is line2[i]): # to check each char
                    final_str = final_str + line1[i]
            if len(line1)-1 is len(final_str):
                return final_str # returns the string where one char differ


total = [0, 0]
doc = open("../inputs/day2.txt", "r")
list_of_words = [x for x in doc.read().split()]
print("Product of twoes and threes are {} and the correct boxID is \"{}\""
      .format(check_sum(), find_id()))
doc.close()