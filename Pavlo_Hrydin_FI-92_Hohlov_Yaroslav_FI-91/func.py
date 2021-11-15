#штука для красивого вівода дерева
import pprint
pp = pprint.PrettyPrinter(indent = 15)

#создания списка деревьев
tree_list = {}

#создание дерева с пустым значением для самого дерева, которое будет каждый раз обновляться, при добавление новых значений
def create_tree(tree_list, name):
    tree_list[name] = [[]]
    return 0

#список всех точек обновляется, в 0 место вставляется дерево с описанием, кто чей листочек
def insert_data_to_tree(tree_list,  name, x, y):
    dots_list = tree_list.get(name)
    dots_list.append([x,y])
    dots_list[0] = print_tree(dots_list[1:])
    # print(dots_list)
    tree_list.update({name:dots_list})
    return 0

#как выглядет само дерево со списка деревьев
def contains_tree(tree_list, name):
    print(tree_list.get(name))
    return 0

#создание дерева со списка точек
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

# create_tree(tree_list, "ipt")
# insert_data_to_tree(tree_list, "ipt", 3, 7)
# insert_data_to_tree(tree_list, "ipt", 8, 6)
# insert_data_to_tree(tree_list, "ipt", 5, 4)
# insert_data_to_tree(tree_list, "ipt", 3, 6)
# insert_data_to_tree(tree_list, "ipt", 5, 8)
# insert_data_to_tree(tree_list, "ipt", 3, 8)
# insert_data_to_tree(tree_list, "ipt", 5, 7)
# contains_tree(tree_list, "ipt")
# pp.pprint(tree_list.get("ipt")[0])
# print(print_tree(tree_list.get("ipt")[1:]))
