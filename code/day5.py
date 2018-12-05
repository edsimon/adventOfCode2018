import string

def check_equal(a, b) :
    if (a.upper() == b.upper()) and not (a == b):
        return True
    else : return False

def filter_and_count( str ) :
    i = 0
    while i < len(str) - 1:
        if (check_equal(str[i],str[i+1])) :
            str = str[:i] + str[i + 2:]
            i = max(0, i - 1)
        else: i += 1
    return len(str)


def rm_then_count(data) :
    to_compare = list(string.ascii_lowercase)
    my_dict = dict()
    for char in to_compare:
        temp_str = data
        temp_str = temp_str.replace(char, "").replace(char.upper(), "")
        my_dict[char] = filter_and_count(temp_str)
    return min(my_dict.values())


file = open("../inputs/day5.txt", "r")
data = file.read()

print("Length of the part a is {} and minimum length of the string after removal is {}."
      .format(filter_and_count(data), rm_then_count(data)))