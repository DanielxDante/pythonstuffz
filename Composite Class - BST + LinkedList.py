class BSTNode():
    def __init__(self, new_data):
        self._data = new_data   #Integer
        self._left = None       #BSTNode
        self._right = None      #BSTNode

    def get_data(self):
        return self._data

    def set_data(self, new_data):
        self._data = new_data

    def get_left(self):
        return self._left

    def set_left(self, new_left):
        self._left = new_left

    def get_right(self):
        return self._right

    def set_right(self, new_right):
        self._right = new_right

    def print(self):
        print(str(self._data))

    #method to facilitate print in HybridStructure
    def inorder_print(self):
        if self._left != None:
            self._left.inorder_print()
        self.print()
        if self._right != None:
            self._right.inorder_print()

class LLNode(BSTNode):
    def __init__(self, new_data):
        super().__init__(new_data)
        self._next = None       #LLNode

    def get_next(self):
        return self._next

    def set_next(self, new_next):
        self._next = new_next


class HybridStructure():
    def __init__(self):
        self._first = None

    def get_first(self):
        return self._first

    def set_first(self, new_first):
        self._first = new_first

    def inLL(self, search_value):
        current_LL_node = self._first
        while current_LL_node != None:
            if current_LL_node.get_data() % 100 // 10  == search_value % 100 // 10:
                return True
            else:
                current_LL_node = current_LL_node.get_next()
        return False

    def contains(self, search_value):
        if self.get_first() == None:
            return False
        else:
            current_LL_node = self._first
            while current_LL_node != None:
                if current_LL_node.get_data() % 100 // 10  == search_value % 100 // 10:
                    current_BST_node = current_LL_node
                    while True:
                        if search_value < current_BST_node.get_data():
                            if current_BST_node.get_left() == None:
                                return False
                            else:
                                current_BST_node = current_BST_node.get_left()
                        elif search_value > current_BST_node.get_data():
                            if current_BST_node.get_right() == None:
                                return False
                            else:
                                current_BST_node = current_BST_node.get_right()
                        else:
                            return True
                else:
                    current_LL_node = current_LL_node.get_next()
            return False

    def insert(self, new_value):
        # if structure empty
        if self.get_first() == None:
            self.set_first(LLNode(new_value)) 
        else:
            inserted = False
            previous_LL_node = None
            current_LL_node = self._first
            while current_LL_node != None:
                if current_LL_node.get_data() % 100 // 10  == new_value % 100 // 10:
                    # insert it in this LLNode (i.e., BST)
                    current_BST_node = current_LL_node
                    while not inserted:
                        if new_value < current_BST_node.get_data():
                            if current_BST_node.get_left() == None:
                                current_BST_node.set_left(BSTNode(new_value))
                                inserted = True
                            else:
                                current_BST_node = current_BST_node.get_left()
                        else:
                            if current_BST_node.get_right() == None:
                                current_BST_node.set_right(BSTNode(new_value))
                                inserted = True
                            else:
                                current_BST_node = current_BST_node.get_right()
                    break # since inserted into current_LL_node BST
                else:
                    previous_LL_node = current_LL_node
                    current_LL_node = current_LL_node.get_next()
            if inserted == False:
                # insert new LLNode - i.e., no existing LLNode with same 10s digit
                if previous_LL_node != None:
                    # more than 1 LLNode case
                    previous_LL_node.set_next(LLNode(new_value))
                else:
                    # only 1 LLNode case
                    current_LL_node.set_next(LLNode(new_value))

    def print(self):
        current_LL_node = self._first
        while current_LL_node != None:
            current_LL_node.inorder_print()
            print("")
            current_LL_node = current_LL_node.get_next()




# Testing HybridStructure
h = HybridStructure()
h.insert(15)
h.insert(99)
h.insert(97)
h.insert(17)
h.insert(12)
h.insert(13)
h.insert(96)
h.insert(91)

h.print()
