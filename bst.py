from functools import total_ordering

@total_ordering
class TestClass:
    """ Represents an arbitrary thing, for testing the BST. """

    def __init__(self, field1, field2=None):
        """ Initialise an object. """
        self._field1 = field1
        self._field2 = field2

    def __str__(self):
        """ Return a short string representation of this object. """
        outstr = self._field1
        return outstr

    def full_str(self):
        """ Return a full string representation of this object. """
        outstr = self._field1 + ": "
        outstr = outstr + str(self._field2)
        return outstr

    def __eq__(self, other):
        """ Return True if this object has exactly same field1 as other. """
        if (other._field1 == self._field1):
            return True
        return False

    def __ne__(self, other):
        """ Return False if this object has exactly same field1 as other. """
        return not (self._field1 == other._field1)

    def __lt__(self, other):
        """ Return True if this object is ordered before other.

        A thing is less than another if it's field1 is alphabetically before.
        """
        if other._field1 > self._field1:
            return True
        return False



class BSTNode:
    """ An internal node for a Binary Search Tree.  """
    
    def __init__(self, item):
        """ Initialise a BSTNode on creation, with value==item. """
        self._element = item
        self._leftchild = None
        self._rightchild = None
        self._parent = None

    def __str__(self):
        """ Return a string representation of the tree rooted at this node.

        The string will be created by an in-order traversal.
        """
        # method body goes here

        if self:
            if self._leftchild or self._rightchild:
                string = ''
                if self._leftchild:
                    string += self._leftchild.__str__() + ''

                string += str(self._element) +' '

                if self._rightchild:
                    string += self._rightchild.__str__() + ''
                return string
            else:
                return str(self._element) + ' '
        else:
            return None


    def _stats(self):
        """ Return the basic stats on the tree. """
        return ('size = ' + str(self.size())
               + '; height = ' + str(self.height()))
    
  
    def search(self, searchitem):
        """ Return object matching searchitem, or None.

        Args:
            searchitem: an object of any class stored in the BST

        """
        #return object - movie
        #call search node
        # method body goes here

        self.search_node(searchitem)


    def search_node(self, searchitem):
        """ Return the BSTNode (with subtree) containing searchitem, or None. 

        Args:
            searchitem: an object of any class stored in the BST
        """

        # return node
        # most work
        # method body goes here

        if self == None:
            return None

        elif searchitem < self._element:
            if self._leftchild is None:
                return None
            return self._leftchild.search_node(searchitem)

        elif searchitem > self._element:
            if self._rightchild is None:
                return None
            return self._rightchild.search_node(searchitem)

        elif searchitem is self._element:
            return self

        else:
            return None

    def add(self, obj):
        """ Add item to the tree, maintaining BST properties.

        Returns the item added, or None if a matching object was already there.
        """
        # method body goes here

        #go left
        if obj < self._element:
            if self._leftchild is None:
                new_node = BSTNode(obj)
                new_node._parent = self
                self._leftchild = new_node
                return obj
            else:
                return self._leftchild.add(obj)

        #go right
        elif obj > self._element:
            if self._rightchild is None:
                new_node = BSTNode(obj)
                new_node._parent = self
                self._rightchild = new_node
                return obj
            else:
                return self._rightchild.add(obj)

        #if equal
        else:
            #obj == self._element
            return None


    def findmaxnode(self):
        """ Return the BSTNode with maximal element at or below here. """
        # method body goes here

        if self._rightchild is not None:
            return self._rightchild.findmaxnode()
        else:
            return self

    def height(self):
        """ Return the height of this node.

        Note that with the recursive definition of the tree the height of the
        node is the same as the depth of the tree rooted at this node.
        """
        # method body goes here

        if self == None:
            return -1
        left = BSTNode.height(self._leftchild)
        right = BSTNode.height(self._rightchild)
        return 1 + max(left, right)

    def size(self):
        """ Return the size of this subtree.

        The size is the number of nodes (or elements) in the tree, 
        including this node.
        """
        # method body goes here

        if self is None:
            return 0
        elif self._leftchild and self._rightchild is not None:
            return 1 + self._leftchild.size() + self._rightchild.size()
        elif self._leftchild is not None:
            return 1 + self._leftchild.size()
        elif self._rightchild is not None:
            return 1 + self._rightchild.size()
        else:
            return 1


    def leaf(self):
        """ Return True if this node has no children. """
        # method body goes here
        # no children

        if self._leftchild and self._rightchild is None:
            return True
        else:
            return False


    def semileaf(self):
        """ Return True if this node has exactly one child. """
        if self._leftchild is None and self._rightchild is not None:
            return True
        elif self._rightchild is None and self._leftchild is not None:
            return True
        elif self._rightchild and self._leftchild is not None:
            return False


    def full(self):
        """ Return true if this node has two children. """
        # method body goes here

        if self._leftchild and self._rightchild is not None:
            return True
        else:
            return False

    def internal(self):
        """ Return True if this node has at least one child. """
        # method body goes here

        if self._leftchild or self._rightchild:
            return True
        elif self._leftchild and self._rightchild:
            return True
        else:
            return False


    def remove(self, searchitem):
        """ Remove and return the object matching searchitem, if there.

        Args:
            searchitem - an object of any class stored in the BST

        Remove the matching object from the tree rooted at this node.
        Maintains the BST properties.
        """
        # call remove node, find the node first
        # method body goes here
        node = self.search_node(searchitem)
        if node is not None:
            node.remove_node()
            #print(node._element)
            
    def remove_node(self):
        """ Remove this BSTNode from its tree, and return its element.
        Maintains the BST properties.
        """
        #work
        #if this is a full node
            #find the biggest item in the left tree
            #  - there must be a left tree, since this is a full node
            #  - the node for that item can have no right children
            #move that item up into this item
            #remove that old node, which is now a semileaf
            #return the original element
        #else if this has no children
            #find who the parent was
            #set the parent's appropriate child to None
            #wipe this node
            #return this node's element
        #else if this has no right child (but must have a left child)
            #shift leftchild up into its place, and clean up
            #return the original element
        #else this has no left child (but must have a right child)
            #shift rightchild up into its place, and clean up
            #return the original element

        # method body goes here

        if self._leftchild and self._rightchild is not None:
            biggest = self._leftchild.findmaxnode()
            biggest._leftchild = self._leftchild
            biggest._rightchild = self._rightchild
            biggest._parent = self._parent
            self._parent = None
            self._rightchild = None
            self._leftchild = None
            return self._element
        elif self._leftchild and self._rightchild is None:
            if self._parent._leftchild is self:
                self._parent._leftchild = None
                self._parent = None
            elif self._parent._rightchild is self:
                self._parent._rightchild = None
                self._parent = None
            return self._element
        elif self._leftchild is not None and self._rightchild is None:
            self._parent._rightchild = self._leftchild
            self._leftchild._parent = self._parent
            self._parent = None
            self._leftchild = None
            return self._element
        elif self._rightchild is not None and self._leftchild is None:
            self._parent._leftchild = self._rightchild
            self._rightchild._parent = self._parent
            self._parent = None
            self._rightchild = None
            return self._element

    def _print_structure(self):
        """ (Private) Print a structured representation of tree at this node. """
        if self._isthisapropertree() == False:
            print("ERROR: this is not a proper Binary Search Tree. ++++++++++")
        outstr = str(self._element) + ' (hgt=' + str(self.height()) + ')['
        if self._leftchild is not None:
            outstr = outstr + "left: " + str(self._leftchild._element)
        else:
            outstr = outstr + 'left: *'
        if self._rightchild is not None:
            outstr = outstr + "; right: " + str(self._rightchild._element) + ']'
        else:
            outstr = outstr + '; right: *]'
        if self._parent is not None:
            outstr = outstr + ' -- parent: ' + str(self._parent._element)
        else:
            outstr = outstr + ' -- parent: *'
        print(outstr)
        if self._leftchild is not None:
            self._leftchild._print_structure()
        if self._rightchild is not None:
            self._rightchild._print_structure()

    def _properBST(self):
        """ Return True if this is the root of a proper BST; False otherwise. 

        First checks that this is a proper tree (i.e. parent and child
        references all link up properly.

        Then checks that it obeys the BST property.
        """
        if not self._isthisapropertree():
            return False
        return self._BSTproperties()[0]

    def _BSTproperties(self):
        """ Return a tuple describing state of this node as root of a BST.

        Returns:
            (boolean, minvalue, maxvalue):
                boolean is True if it is a BST, and false otherwise
                minvalue is the lowest value in this subtree
                maxvalue is the highest value in this subtree
        """
        minvalue = self._element
        maxvalue = self._element
        if self._leftchild is not None:
            leftstate = self._leftchild._BSTproperties()
            if not leftstate[0] or leftstate[2] > self._element:
                return (False,None,None)
            minvalue = leftstate[1]

        if self._rightchild is not None:
            rightstate = self._rightchild._BSTproperties()
            if not rightstate[0] or rightstate[1] < self._element:
                return (False,None,None)
            maxvalue = rightstate[2]

        return (True, minvalue,maxvalue)

    def _isthisapropertree(self):
        """ Return True if this node is a properly implemented tree. """
        ok = True
        if self._leftchild is not None:
            if self._leftchild._parent != self:
                ok = False
            if self._leftchild._isthisapropertree() == False:
                ok = False
        if self._rightchild is not None:
            if self._rightchild._parent != self:
                ok = False
            if self._rightchild._isthisapropertree() == False:
                ok = False          
        if self._parent is not None:
            if (self._parent._leftchild != self
                and self._parent._rightchild != self):
                ok = False
        return ok

    def _testadd():
        node = BSTNode(TestClass("Memento", "11/10/2000"))
        node._print_structure()
        print('> adding Melvin and Howard')
        node.add(TestClass("Melvin and Howard", "19/09/1980"))
        node._print_structure()
        print('> adding a second version of Melvin and Howard')
        node.add(TestClass("Melvin and Howard", "21/03/2007"))
        node._print_structure()
        print('> adding Mellow Mud')
        node.add(TestClass("Mellow Mud", "21/09/2016"))
        node._print_structure()
        print('> adding Melody')
        node.add(TestClass("Melody", "21/03/2007"))
        node._print_structure()
        return node

    def _test():
        node = BSTNode(TestClass("B", "b"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "A")
        node.add(TestClass("A", "a"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "A")
        node.remove(TestClass("A"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(TestClass("C", "c"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "C")
        node.remove(TestClass("C"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "F")
        node.add(TestClass("F", "f"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "B")
        node.remove(TestClass("B"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(TestClass("C", "c"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "D")
        node.add(TestClass("D", "d"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "C")
        node.add(TestClass("C", "c"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "E")
        node.add(TestClass("E", "e"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "B")
        node.remove(TestClass("B"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "D")
        node.remove(TestClass("D"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "C")
        node.remove(TestClass("C"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "E")
        node.remove(TestClass("E"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "L")
        node.add(TestClass("L", "l"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "H")
        node.add(TestClass("H", "h"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "I")
        node.add(TestClass("I", "i"))
        print('Ordered:', node)
        node._print_structure()
        print('adding', "G")
        node.add(TestClass("G", "g"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "L")
        node.remove(TestClass("L"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "H")
        node.remove(TestClass("H"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "I")
        node.remove(TestClass("I"))
        print('Ordered:', node)
        node._print_structure()
        print('removing', "G")
        node.remove(TestClass("G"))
        print('Ordered:', node)
        node._print_structure()
        print(node)

# bst = BSTNode._testadd()
#
#bst.findmaxnode()
# maxnode = bst.findmaxnode()
#print(maxnode)
#BSTNode._test()

#BSTNode._print_structure()

#print('++++++++++')
#BSTNode._test()


# def main():
#     bst = BSTNode(5)
    # bst.add(2)
    # bst.add(1)
    # bst.add(3)
    # bst.add(4)
    # bst.add(7)
    # bst.add(6)
    # bst.add(9)
    # bst.add(8)
    # bst.add(10)

    # bst._testadd()
    # bst._print_structure()
    # maxnode = bst.findmaxnode()
    # print(maxnode)
    # bst.height()
    # print(bst.height())
    # print(bst.height())
    # bst.remove(5)
    # print(bst)
    # print(bst.size())
    # bst._print_structure()
    # print(bst.search_node(11))
    # print(bst.remove(3))



# if __name__ == '__main__':
#     main()

            
