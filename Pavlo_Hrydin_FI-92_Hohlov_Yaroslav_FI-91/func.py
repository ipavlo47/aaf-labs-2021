import numpy as np

class Node:

    mass = []
    def __init__(self, data):

        self.left = None
        self.right = None
        self.mass.append(data)
        self.data = data


    def insert(self, data, deepening = 0):
        if self.data:
            if data[deepening % 2] <= self.data[deepening % 2]:
                if self.left is None:
                    data+=[deepening + 1]
                    self.left = Node(data)
                else:
                    deepening += 1
                    self.left.insert(data, deepening)
            elif data[deepening % 2] > self.data[deepening % 2]:
                if self.right is None:
                    data+=[deepening + 1]
                    self.right = Node(data)
                else:
                    deepening += 1
                    self.right.insert(data, deepening)
        else:
            self.data = data


    def PrintTree(self):
        if self.right:
            self.right.PrintTree()
        if (int(self.data[2]) != 0):
            print("     " + "              " * (int(self.data[2])-1) + "|—————— ", self.data[:2], "..."*40)
        else:
            print(self.data[:2], "..."*40)
        if self.left:
            self.left.PrintTree()

    def get_list(self):
        return np.array(self.mass).T[:2].T.tolist()



#
# tree_list = {}
# tree_list["ipt"] = []
# print(tree_list["ipt"].get_list())
#
#
# tree_list["ipt"] = Node([5, 4] + [0])
# tree_list["ipt"].insert([3, 7])
# tree_list["ipt"].insert([5, 1])
# tree_list["ipt"].insert([6, 11])
# tree_list["ipt"].insert([6, 4])
# tree_list["ipt"].insert([1, 7])
# tree_list["ipt"].insert([3, 5])
# tree_list["ipt"].PrintTree()
#
#
#
# tree_list["ipt"].insert([18, 6])
# tree_list["ipt"].PrintTree()
#
# print(tree_list["ipt"].get_list())
