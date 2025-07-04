class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def insert(self, root, value):
        if root is None:
            return Node(value)
        if value < root.val:
            root.left = self.insert(root.left, value)
        elif value > root.val:
            root.right = self.insert(root.right, value)
        return root

    def search(self, root, value):
        if root is None:
            return False
        if value < root.val:
            return self.search(root.left, value)
        elif value > root.val:
            return self.search(root.right, value)
        return True

    def delete(self, root, value):
        if root is None:
            print("No nodes to delete!")
            return None
        if value < root.val:
            root.left = self.delete(root.left, value)
        elif value > root.val:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = self.delete(root.right, successor.val)
        return root

    def find_min(self, root):
        if root is None:
            return None
        current = root
        while current.left:
            current = current.left
        return current

    def find_max(self, root):
        if root is None:
            return None
        current = root
        while current.right:
            current = current.right
        return current

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.val, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=' ')

    def height(self, root):
        if root is None:
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return 1 + max(left_height, right_height)

    def size(self, root):
        if root is None:
            return 0
        return 1 + self.size(root.left) + self.size(root.right)

# Create BST instance
bst = BinarySearchTree()
root = None

# Insert nodes
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = bst.insert(root, val)

print("Inorder Traversal (Should be sorted):")
bst.inorder(root)
print("\nPreorder Traversal:")
bst.preorder(root)
print("\nPostorder Traversal:")
bst.postorder(root)

# Search for values
print("\n\nSearch for 40:", bst.search(root, 40))  # True
print("Search for 100:", bst.search(root, 100))    # False

# Find min and max
min_node = bst.find_min(root)
max_node = bst.find_max(root)
print("\nMinimum value:", min_node.val if min_node else None)
print("Maximum value:", max_node.val if max_node else None)

# Height and Size
print("Height of tree:", bst.height(root))
print("Size of tree:", bst.size(root))

# Delete a leaf node
root = bst.delete(root, 20)
print("\nInorder after deleting 20:")
bst.inorder(root)

# Delete node with one child
root = bst.delete(root, 30)
print("\nInorder after deleting 30:")
bst.inorder(root)

# Delete node with two children
root = bst.delete(root, 50)
print("\nInorder after deleting 50:")
bst.inorder(root)
