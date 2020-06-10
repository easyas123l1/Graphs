# so we look for what values we can point to tuples are (3, 5) we want are start location to be second in tuple and destination as first
# when we find a match
from collections import deque


def earliest_ancestor(ancestors, starting_node):
    stack = deque()
    stack.append([starting_node])
    cache = {}
    results = []
    path = []
    for ancestor in ancestors:
        if ancestor[1] in cache:
            cache[ancestor[1]].append(ancestor[0])
        else:
            cache[ancestor[1]] = [ancestor[0]]
    if starting_node not in cache:
        return -1
    while len(stack) > 0:
        print(stack)
        current_array = stack.pop()
        while len(current_array) > 0:
            current = current_array.pop()
            path.append(current)
            if current in cache:
                stack.append(cache[current])
            else:
                results.append((len(stack), current))
    best = results[0]
    print(results)
    for result in results:
        if result[0] == best[0]:
            if result[1] < best[1]:
                best = result
        if result[0] > best[0]:
            best = result
    return best[1]
    #     if ancestor[1] == current:
    #         current = ancestor[0]
    #         stack.append(ancestor)
    # new_current = stack.pop()
    # current = new_current[0]


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 1))  # 10
# print(earliest_ancestor(test_ancestors, 3))  # 10)
# print(earliest_ancestor(test_ancestors, 2))  # -1)
# print(earliest_ancestor(test_ancestors, 4))  # -1)
# print(earliest_ancestor(test_ancestors, 5))  # 4)
print(earliest_ancestor(test_ancestors, 6))  # 10)
# print(earliest_ancestor(test_ancestors, 7))  # 4)
# print(earliest_ancestor(test_ancestors, 9))  # 4)
# print(earliest_ancestor(test_ancestors, 10))  # -1)
# print(earliest_ancestor(test_ancestors, 11))  # -1)
