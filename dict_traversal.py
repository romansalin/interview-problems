from collections import deque, Mapping
from itertools import repeat


def print_depth_bfs(data):
    """
    Breadth-first search algorithm (non-recursive) for printing all dictionary
    keys with their depth.
    """
    if not isinstance(data, Mapping):
        raise TypeError("Input should be a dictionary.")

    items = zip(data.items(), repeat(1, len(data)))
    stack = deque(items)
    while stack:
        (key, val), depth = stack.popleft()
        print("{0} {1}".format(key, depth))
        if isinstance(val, Mapping):
            items = zip(val.items(), repeat(depth + 1, len(val)))
            stack.extend(items)


def print_depth_dfs(data):
    """
    Depth-first search algorithm (non-recursive) for printing all dictionary
    keys with their depth.
    """
    if not isinstance(data, Mapping):
        raise TypeError("Input should be a dictionary.")

    items = zip(data.items(), repeat(1, len(data)))
    stack = deque(items)
    while stack:
        (key, val), depth = stack.pop()
        print("{0} {1}".format(key, depth))
        if isinstance(val, Mapping):
            items = zip(val.items(), repeat(depth + 1, len(val)))
            stack.extend(items)


def print_depth_recursive(data, depth=1):
    """
    Depth-first search algorithm (recursive) for printing all dictionary
    keys with their depth.
    """
    if not isinstance(data, Mapping):
        raise TypeError("Input should be a dictionary.")

    for key, val in data.items():
        print("{0} {1}".format(key, depth))
        if isinstance(val, Mapping):
            print_depth_recursive(val, depth=depth+1)


def main():
    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        }
    }

    print("Breadth-first search algorithm (non-recursive):")
    print_depth_bfs(a)
    print("Depth-first search algorithm (non-recursive):")
    print_depth_dfs(a)
    print("Depth-first search algorithm (recursive):")
    print_depth_recursive(a)


if __name__ == "__main__":
    main()
