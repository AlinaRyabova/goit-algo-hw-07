from basic_search_tree import Node, insert

def sum_tree(node):
    if node is None:
        return 0
    return node.val + sum_tree(node.left) + sum_tree(node.right)

if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    total_sum = sum_tree(root)
    print(f"У дереві знайдено суму всіх значень: {total_sum}")
