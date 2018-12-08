''' Parsing the tree to the right format needed for the task '''
def parse_tree(tree):
    n_children = tree.pop(0)
    n_meta = tree.pop(0)

    children = []
    for _ in range(n_children):
        children.append(parse_tree(tree))

    meta = []
    for _ in range(n_meta):
        meta.append(tree.pop(0))
    return (children, meta)

''' Recursive function that counts all metas'''
def sum_metas(tree):
    return sum(sum_metas(child) for child in tree[0]) + sum(tree[1])

''' Recursive function to count values '''
def node_value(node):
    children, metas = node
    if not children:
        return sum(metas)
    else:
        value = 0
        for meta in metas:
            if meta == 0 or meta > len(children):
                continue
            else:
                value += node_value(children[meta-1])
        return value

''' Standard "with open",,, my main method persé'''
with open("../inputs/day8.txt", "r") as f :
    data = list(map(int, f.read().strip().split(' ')))
    tree = parse_tree(data)
    part_a = sum_metas(tree)
    part_b = node_value(tree)
    print("Sum of the metas is {} and the values is {}."
          .format(part_a, part_b))