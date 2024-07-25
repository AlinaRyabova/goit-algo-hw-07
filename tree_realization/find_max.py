from basic_search_tree import Node, insert

def find_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.val

if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    max_value = find_max(root)
    print(f"У дереві знайдено найбільше значення: {max_value}")
