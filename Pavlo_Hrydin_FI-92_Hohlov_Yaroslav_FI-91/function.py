import pprint

pp = pprint.PrettyPrinter(indent = 15)
tree_list = {}

def  create_tree(tree_list, name):
    tree_list[name] = []
    return 0

def insert_data_to_tree(tree_list,  name, x, y):
    dots_list = tree_list.get(name)
    dots_list.append([x,y])
    tree_list.update({name:dots_list})
    return 0 

def contains_tree(tree_list, name):
    print(tree_list.get(name))
    return 0

def print_tree(mas, depth = 0):
    length = len(mas)
    if length <= 0:
        return None
    axis = depth % 2
    sorted_dots_list = sorted(mas, key = lambda point: point[axis])
    return {
        "point" : sorted_dots_list[int(length/2)],
        "left" : print_tree(sorted_dots_list[:int(length/2)], depth + 1),
        "right" : print_tree(sorted_dots_list[int(length/2 + 1):], depth + 1)
        
    }

create_tree(tree_list, "ipt")
insert_data_to_tree(tree_list, "ipt", 3, 7)
insert_data_to_tree(tree_list, "ipt", 8, 6)
insert_data_to_tree(tree_list, "ipt", 5, 4)
insert_data_to_tree(tree_list, "ipt", 3, 6)
insert_data_to_tree(tree_list, "ipt", 5, 8)
insert_data_to_tree(tree_list, "ipt", 3, 8)
insert_data_to_tree(tree_list, "ipt", 5, 7)
print(tree_list)
contains_tree(tree_list, "ipt")
pp.pprint(print_tree(tree_list.get("ipt")))