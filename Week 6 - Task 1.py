
class BinTreeNode():

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None


        
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print (tree.value)
  

def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print (tree.value)
    if(tree.right!=None):
        in_order(tree.right)
"""
def in_order2(tree):
    s =[]
    Cnode = tree.value
"""
def tree_sort(sequence,tree):
    for item in sequence:
        tree_insert(tree, item)
    return tree


if __name__ == '__main__':
    
  t=tree_insert(None,10);
  T1=[2,7,4,1,8]
  t1=tree_sort(T1,t)
  in_order(t1)
