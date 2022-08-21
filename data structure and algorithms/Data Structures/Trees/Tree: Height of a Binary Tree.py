def height(node):
  if node is None:
    return -1
  return max(height(node.left),height(node.right))+1
