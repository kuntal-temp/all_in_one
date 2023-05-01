'''
  pip install binarytree 
'''
from binarytree import Node, build, tree, bst, heap

root = Node(3)
root.left = Node(6)
root.right = Node(8)
print('Binary tree :', root)
print('List of nodes :', list(root))
print('Inorder of nodes :', root.inorder)
print('Size of tree :', root.size)
print('Height of tree :', root.height)
print('Properties of tree : \n', root.properties)

nodes =[3, 6, 8, 2, 11, None, 13]
binary_tree = build(nodes)
print('Binary tree from list :\n', binary_tree)

root = tree()
print("Binary tree of any height :")
print(root)

root3 = tree(height = 2, is_perfect = True)
print("Perfect binary tree of given height :")
print(root3)

root = bst()
print('BST of any height : \n', root)

root3 = bst(height = 2, is_perfect = True)
print('Perfect BST of given height : \n', root3)

root = heap()
print('Max-heap of any height : \n', root)

root3 = heap(height = 2, is_max = False, is_perfect = True)
print('Perfect min-heap of given height : \n', root3)



'''
There are different types of Tree like:
  Binary Tree,
  Binary Search Tree,
  AVL Tree,
  B-Tree
'''



##################################
        # Binary Tree #
##################################


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
 

# Create root
root = Node(1)
''' 
following is the tree after above statement
    1
  /   \
  None  None
  '''
  
root.left = Node(2)
root.right = Node(3)
''' 
2 and 3 become left and right children of 1
        1
      /   \
    2      3
  /    \    /  \
None None None None
'''
  
root.left.left = Node(4)
'''
4 becomes left child of 2
            1
        /       \
      2          3
    /   \       /  \
    4    None  None  None
  /  \
None None
'''


'''
1) The maximum number of nodes at level l of a binary tree is 2^l. 
2) The Maximum number of nodes in a binary tree of height h is 2^h-1. 
'''



##################################
        # Tree Traversal #
##################################

'''
Tree Traversal:
  -> Inorder traversal
      inorder(root->left)
      display(root->data)
      inorder(root->right)

  -> Preorder traversal
      display(root->data)
      preorder(root->left)
      preorder(root->right)
        
  -> Postorder traversal
      postorder(root->left)
      postorder(root->right)
      display(root->data)
'''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def print_Inorder(root):
    if root:
        # First recur on left child
        print_Inorder(root.left)
        # then print the data of node
        print(root.val)
        # now recur on right child
        print_Inorder(root.right)

def print_Preorder(root):
    if root:
        # then print the data of node
        print(root.val)
        # First recur on left child
        print_Preorder(root.left)
        # now recur on right child
        print_Preorder(root.right)

def print_Postorder(root):
    if root:
        # First recur on left child
        print_Postorder(root.left)
        # now recur on right child
        print_Postorder(root.right)
        # then print the data of node
        print(root.val)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print_Inorder(root)



##################################
      # Binary Search Tree #
##################################

'''
# Binary Search Tree

In Binary Search Tree is a Binary Tree with the following additional properties:

>The left subtree of a node contains only nodes with keys less than the node's key.
>The right subtree of a node contains only nodes with keys greater than the node's key.
>The left and right subtree each must also be a binary search tree.

>It is called a binary tree because each tree node has a maximum of two children.
>It is called a search tree because it can be used to search for the presence of a 
number in O(log(n)) time.


Search	  O(log n)	O(log n)	O(n)
Insertion	O(log n)	O(log n)	O(n)
Deletion	O(log n)	O(log n)	O(n)

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_node_to_tree(root, new_value):
    if root is None:
        root = Node(new_value)
    elif root.data < new_value:
        root.right = insert_node_to_tree(root.right, new_value)
    elif root.data > new_value:
        root.left = insert_node_to_tree(root.left, new_value)
    elif root.data == new_value:
        pass
    else:
      print("No condition matched there")
    return root

def search_tree(root, find):
    if root is None:
        return root
    elif root.data == find:
        return root 
    elif root.data > find:
        root = search_tree(root.left, find)
        return root
    elif root.data < find:
        root = search_tree(root.right, find)
        return root
    else:
        return None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


''' insert on BST '''
r = Node(50)
r = insert_node_to_tree(r, 30)
r = insert_node_to_tree(r, 20)
r = insert_node_to_tree(r, 40)
r = insert_node_to_tree(r, 70)
r = insert_node_to_tree(r, 60)
r = insert_node_to_tree(r, 80)

''' print tree'''
inorder(r)

''' search on BST tree '''
find = 50
root = search_tree(r, find)
if root:
    if find == root.data:
        print("found")
else:
    print("not found")




##################################
        # AVL Tree #
##################################

'''
https://www.javatpoint.com/avl-tree

AVL tree is a self-balancing binary search tree in which each node maintains 
extra information called a balance factor whose value is either -1, 0 or +1.

Balance Factor (k) = height (left(k)) - height (right(k))

Insertion	Deletion	Search
O(log n)	O(log n)	O(log n)
'''



##################################
        # B-Tree #
##################################

'''
Why do you need a B-tree data strcuture?

> The need for B-tree arose with the rise in the need for lesser time in 
accessing the physical storage media like a hard disk. The secondary storage 
devices are slower with a larger capacity. There was a need for such types of 
data structures that minimize the disk accesses.

Other data structures such as a binary search tree, avl tree, red-black tree, etc can 
store only one key in one node. If you have to store a large number of keys, then the 
height of such trees becomes very large and the access time increases.

However, B-tree can store many keys in a single node and can have multiple child nodes. 
This decreases the height significantly allowing faster disk accesses.
'''

