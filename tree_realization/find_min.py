from basic_search_tree import Node, insert

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val

if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    min_value = find_min(root)
    print(f"У дереві знайдено найменше значення: {min_value}")
