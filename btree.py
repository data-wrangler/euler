# btree.py -- implementation of unbalanced binary trees
# 
# so I want this to do fast phi functions. I will have an array of 1,0 values that correspond
# to the existence of primes in the factorization of a number. I would like to be able to 
# traverse a tree through these values and return the factor.
#
# in theory, it should work for recomposition of composite numbers as well, given exponents
# instead of 

class treeNode(object):
    parent=None
    value=None
    children={}
    def __init__(self,node_parent,node_value):
        self.parent=node_parent
        self.setVal(node_value)
    def getVal(self):
        return self.value
    def setVal(self,node_value):
        self.value=node_value
    def setChild(self,child_key,child_value=None):
        try:
            self.children[child_key].setVal(child_value)
        except KeyError:
            self.children[child_key]=treeNode(self,child_value)
        return children[child_key]
    def getChild(self,child_key):
        try:
            return self.children[child_key]
        except KeyError:
            return None
    def draw(self):
        for child_key,child in self.children.iteritems():
            print "({0!s})->{1!s}:{2!s}".format(self.value,child_key,child.draw())

class btree(object):
    def __init__(self,root_value=None):
        self.root=treeNode(None,root_value)
    def traverse_get(self,key_list,current_node=None,traversed_nodes=[]):
        current_node=current_node or self.root
        try:
            current_node=current_node.getChild(key_list[0])
            traversed_nodes.append(key_list.pop(0))
            return self.traverse_get(key_list,current_node,traversed_nodes)
        except:
            return current_node.getVal(), traversed_nodes
    def traverse_set(self,value_to_set,key_list,current_node=None,traversed_nodes=[]):
        current_node=current_node or self.root
        try:
            last_node=current_node
            current_node=current_node.getChild(key_list[0])
            traversed_nodes.append(key_list.pop(0))
            return self.traverse_set(value_to_set,key_list,current_node,traversed_nodes)
        except IndexError:
            current_node.setVal(value_to_set)
        except AttributeError:
            current_node=last_node
            for key in key_list:
                current_node=current_node.setChild(key)
            current_node.setVal(value_to_set)
    def draw(self):
        self.root.draw()
