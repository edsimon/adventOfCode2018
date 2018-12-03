from collections import defaultdict,namedtuple
import re

def file_reader():
    lst_file = []
    with open("../inputs/day3.txt", "r") as f:
        for line in f.readlines():
            claim = namedtuple('Claim', 'id x y width height')
            lst_file.append(claim(*map(int, re.findall('\d+', line))))
    return lst_file


def count_overlaps() :
    n = 0
    for d, x, y, w, l in input:
        for i in range(x, x + w):
            for j in range(y, y + l):
                overlap[i, j] += 1
    for loc, count in overlap.items():
        if count > 1:
            n += 1
    return n


def find_lonely_id() :
    all_claims = set()
    overlap_claims = set()
    for d, x, y, w, l in input:
        all_claims.add(d)
        for i in range(x, x + w):
            for j in range(y, y + l):
                if overlap[i, j] > 1:
                    overlap_claims.add(d)
    return all_claims - overlap_claims


input = file_reader()
overlap = defaultdict(int)
print("Found {} overlaps and {} are the only ID not overlapping"
      .format(count_overlaps(),find_lonely_id()))