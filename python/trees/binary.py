import numpy as npy 
import pandas as pd

'''
INTRO TO BINARY TREES 
TODO: implement in c / cpp

always a root node 
every left node gets smaller whereas every right node gets bigger than their parent


makes sure the bianry tree is sorted
left is smaller
right is bigger

BINARY SEARCH TREE 
TODO: implement a binary search tree (BST algorithm)


4 ways to traverse a binary tree:

1- depth first aproach of DFS
    a. inorder traversal
    b. preorder traversal
    c. postorder traversal
2- level order traversal or breadth first search of BFS
3- boundary traversal
4- diagonal traversal
'''

# node itself
class node:
    #init the head node
    def __init__(self, data):

        self.data = None
        self.left = None  # default
        self.right = None # default none
        #basically linked list
        if isinstance(data,str): # if the data is a string
            for c in data:
                self.insert(c)
        else:
            self.data = data # must have data

    def insert(self,data):
        if(self.data is None): # if node itself is null
            self.data = data 
            
        else:
            #NOTE: the binary tree has no duplicates because neither condition will be true
            if data < self.data: #inser to the left
                if self.left is None: # if theres nothing then put it
                    self.left = node(data) #new node using the data
                    #NOTE: tutorial implements as if and else statements
                else:
                    #if theres something there then recursively insert it there
                    self.left.insert(data) #gonna keep recursing until the condition becomes false

            elif data > self.data:
                # same as left but to right
                if self.right is None:
                    self.right = node(data)
                
                self.right.insert(data) #recursiveee
    
    def remove(self, value):
        if self is None:
            return
        if self.data == value:
            print('deleting node:', curr.data)
        self.left.remove(value)
        self.right.remove(value)
        del self

def delete(curr:node):
    if curr is None:
        return


    print('deleting node:', curr.data)
    delete(curr.left)
    delete(curr.right)
    del curr

# printing all nodes InOrder

'''
#   DEPTH FIRST SEARCH
# aka vertical search 
# searches until end of branch and doesnt move until very end


lets say a tree like this

        b (root)
       / \
(left)a   c  (right)
       \
        e

INORDER:
left, root, right

starts at root, prints left, then prints the current, then prints the right
in ex - prints a b c e
quickly sorts in ascending order 


PREORDER:
root, left, right 


POSTORDER:
root, right, left

b , c , a

'''
#prints from a node
def in_order_print(curr:node):
    if curr is None:
        return

    in_order_print(curr.left)
    print(curr.data, end = ' ')
    in_order_print(curr.right)

def pre_order_print(curr:node):
    if curr is None:
        return
    else:
        print(curr.data, end = ' ')
        pre_order_print(curr.left)
        pre_order_print(curr.right)    

def post_order_print(curr:node):
    if curr is None:
        return
    else:
        print(curr.data, end = ' ')
        pre_order_print(curr.right) 
        pre_order_print(curr.left)


'''
 BREADTH FIRST APPROACH
 aka level first approach
 goes horizontally


basically a queue
each time add children of a node, pop the head from the queue

    
'''



# makes sure that the python file is NOT imported
if __name__ == '__main__':

    #can do each individual
    #but implemented pseudo constructor overloading
    root = node('gcbaedfihjk')
    root.insert('z')

    in_order_print(root) # a b c d e f g h i j k 
    print('\n')

    pre_order_print(root) # g c b a e d f i h j k
    print('\n')

    post_order_print(root) # g i h j k z c b a e d f
    print('\n')

    root.remove('h')
    #delete(root)



