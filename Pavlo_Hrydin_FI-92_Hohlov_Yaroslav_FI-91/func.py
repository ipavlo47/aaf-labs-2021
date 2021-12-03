is_contains = 0


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
        print("Range " + str(data) + " has been added to set_name")


    def insert(self, data, significative = 0):
        if self.data:
            if self.data == data:
                print("this line consist in")
            else:
                if data[significative] <= self.data[significative]:
                    if self.left is None:
                        self.left = Node(data)
                    else:
                        significative ^= 1
                        self.left.insert(data, significative)
                elif data[significative] > self.data[significative]:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        significative ^= 1
                        self.right.insert(data, significative)
        else:
            print("Range " + str(data) + " has been added to set_name")
            self.data = data

    def PrintTree(self, significative = 0):
        if significative != 0:
            if not (self.left) and self.right:
                print("    " * (significative - 1) + "└──", self.right.data)
                significative += 1
                self.right.PrintTree(significative)
            else:
                if self.left:
                    print("    " * (significative - 1) + "├──", self.left.data)
                    significative +=1
                    self.left.PrintTree(significative)
                significative -= 1
                if self.right:
                    print("    " * (significative - 1) + "└──", self.right.data)
                    significative += 1
                    self.right.PrintTree(significative)
        else:
            significative +=1
            print(self.data)
            self.PrintTree(significative)

    def Search(self, info_for_found, significative = 0):
        if significative == 0:
            if (self.data[significative] < info_for_found[significative]):
                if self.left:
                    significative ^= 1
                    self.left.Search(info_for_found, significative)
            else:
                if (self.data[significative] >= info_for_found[significative]) and (self.data[significative ^ 1] <= info_for_found[significative ^ 1]):
                    print(self.data)
                if self.right:
                    if self.left:
                        significative ^= 1
                        self.right.Search(info_for_found, significative)
                        self.left.Search(info_for_found, significative)
                    else:
                        significative ^= 1
                        self.right.Search(info_for_found, significative)
                elif self.left:
                    significative ^= 1
                    self.left.Search(info_for_found, significative)
        else:
            if (self.data[significative] > info_for_found[significative]):
                if self.right:
                    significative ^= 1
                    self.right.Search(info_for_found, significative)
            else:
                if (self.data[significative ^ 1] >= info_for_found[significative ^ 1]) and (self.data[significative] <= info_for_found[significative]):
                    print(self.data)
                if self.right:
                    if self.left:
                        significative ^= 1
                        self.right.Search(info_for_found, significative)
                        self.left.Search(info_for_found, significative)
                    else:
                        significative ^= 1
                        self.right.Search(info_for_found, significative)
                elif self.left:
                    significative ^= 1
                    self.left.Search(info_for_found, significative)

    def Intersects(self, info_for_found, significative = 0):
        if significative == 0:
            if (self.data[significative] > info_for_found[significative ^ 1]):
                if self.left:
                    significative ^= 1
                    self.left.Intersects(info_for_found, significative)
            else:
                if ((self.data[0] <= info_for_found[0]) and (self.data[1] >= info_for_found[0])) or ((self.data[1] >= info_for_found[1]) and (self.data[0] <= info_for_found[1])) or ((self.data[0] >= info_for_found[0]) and (self.data[1] <= info_for_found[1])) or ((self.data[0] <= info_for_found[0]) and (self.data[1] >= info_for_found[1])):
                    print(self.data)
                if self.right:
                    if self.left:
                        significative ^= 1
                        self.right.Intersects(info_for_found, significative)
                        self.left.Intersects(info_for_found, significative)
                    else:
                        significative ^= 1
                        self.right.Intersects(info_for_found, significative)
                elif self.left:
                    significative ^= 1
                    self.left.Intersects(info_for_found, significative)
        else:
            if (self.data[significative] < info_for_found[significative ^ 1]):
                if self.right:
                    significative ^= 1
                    self.right.Intersects(info_for_found, significative)
            else:
                if ((self.data[0] <= info_for_found[0]) and (self.data[1] >= info_for_found[0])) or ((self.data[1] >= info_for_found[1]) and (self.data[0] <= info_for_found[1])) or ((self.data[0] >= info_for_found[0]) and (self.data[1] <= info_for_found[1])) or ((self.data[0] <= info_for_found[0]) and (self.data[1] >= info_for_found[1])):
                    print(self.data)
                if self.right:
                    if self.left:
                        significative ^= 1
                        self.right.Intersects(info_for_found, significative)
                        self.left.Intersects(info_for_found, significative)
                    else:
                        significative ^= 1
                        self.right.Intersects(info_for_found, significative)
                elif self.left:
                    significative ^= 1
                    self.left.Intersects(info_for_found, significative)

    def Contains(self, info_for_found):
        self.Contains_by(info_for_found)
        global is_contains
        if is_contains == 1:
            print(True)
        else:
            print(False)
        is_contains = 0

    def Contains_by(self, info_for_found, significative = 0):
        global is_contains
        if significative == 0:
            if (self.data[significative] > info_for_found[significative]):
                if self.left:
                    significative ^= 1
                    self.left.Contains_by(info_for_found, significative)
            else:
                if (self.data[significative] == info_for_found[significative]) and (self.data[significative ^ 1] == info_for_found[significative ^ 1]):
                    is_contains = 1
                if self.right:
                    if self.left:
                        significative ^= 1
                        self.right.Contains_by(info_for_found, significative)
                        self.left.Contains_by(info_for_found, significative)
                    else:
                        significative ^= 1
                        self.right.Contains_by(info_for_found, significative)
                elif self.left:
                    significative ^= 1
                    self.left.Contains_by(info_for_found, significative)
        else:
            if (self.data[significative] < info_for_found[significative]):
                if self.right:
                    significative ^= 1
                    self.right.Contains_by(info_for_found, significative)
            else:
                if (self.data[significative ^ 1] == info_for_found[significative ^ 1]) and (self.data[significative] == info_for_found[significative]):
                    is_contains = 1
                if self.right:
                    if self.left:
                        significative ^= 1
                        self.right.Contains_by(info_for_found, significative)
                        self.left.Contains_by(info_for_found, significative)
                    else:
                        significative ^= 1
                        self.right.Contains_by(info_for_found, significative)
                elif self.left:
                    significative ^= 1
                    self.left.Contains_by(info_for_found, significative)
#
# tree_list = {}
# tree_list["ipt"] = []
#
#
# tree_list["ipt"] = Node([5, 10])
# tree_list["ipt"].insert([7, 15])
# tree_list["ipt"].insert([3, 7])
# tree_list["ipt"].insert([8, 10])
# tree_list["ipt"].insert([10, 20])
# tree_list["ipt"].insert([7, 15])
# tree_list["ipt"].insert([8, 16])
# tree_list["ipt"].insert([1, 4])
# tree_list["ipt"].insert([5, 8])
# tree_list["ipt"].PrintTree()
# tree_list["ipt"].Search([1, 10])
# tree_list["ipt"].Contains([8, 16])
# tree_list["ipt"].Intersects([1, 8])
# #
# #


# tree_list["ipt"].insert([6, 18])
# tree_list["ipt"].PrintTree()
#
#print(tree_list["ipt"].get_list())


# tree_list["ipt"] = Node([3, 4])
# tree_list["ipt"].insert([2, 7])
# tree_list["ipt"].insert([5, 8])
# tree_list["ipt"].insert([4, 6])
# tree_list["ipt"].insert([5, 10])
# tree_list["ipt"].PrintTree()
