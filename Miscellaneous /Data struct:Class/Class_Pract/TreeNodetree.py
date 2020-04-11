
# TreeNodetree.py

from TreeNode import TreeNode

def main():

    root = TreeNode(12, TreeNode(54, None, TreeNode(14)),
    TreeNode(78, TreeNode(12), TreeNode(12)))


    print("Root is {}, left number {}, right number {}"
          .format(root.item, root.left.item, root.right.item))

    print("Child's Left, Right Node {}, Child's Right, left Node {}, \nChild's right, right {}  "
          .format(root.left.right.item, root.right.left.item, root.right.right.item ))



"""
12, 54, 78, None, 14, 12, 12

"""
    
main()
