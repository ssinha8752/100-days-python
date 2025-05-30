def min_val(self,current_node):
    while current_node.left is not None:
        current_node=current_node.left
    return current_node.value