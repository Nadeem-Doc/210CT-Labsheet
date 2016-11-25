
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

def in_order2(tree):
    treeNodes = []
    cNode = tree
    inOrder = []
    loop = True
    
    while loop:
        if cNode != None:
           treeNodes.append(cNode)
           cNode = cNode.left

        elif len(treeNodes) > 0:
           p = treeNodes.pop()
           inOrder.append(p.value)
           cNode = p.right

        else:
            loop= False

    return inOrder 

def tree_sort(sequence,tree):
    for item in sequence:
        tree_insert(tree, item)
    return tree


if __name__ == '__main__':
    
  tree=tree_insert(None,10);
  addToTree =[2,7,4,1,8]
  sTree=tree_sort(addToTree,tree)
  print(in_order2(sTree))
