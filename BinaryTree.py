class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def in_order_dfs(node):
    if node is None:
        return
    in_order_dfs(node.left)
    print(node.data, end=' ')
    in_order_dfs(node.right)

