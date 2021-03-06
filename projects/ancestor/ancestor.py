# so we look for what values we can point to tuples are (3, 5) we want are start location to be second in tuple and destination as first
# when we find a match
from collections import deque


def earliest_ancestor(ancestors, starting_node):
    stack = []
    # starting node as first location
    stack.append([starting_node])
    # cache for all ancestors
    cache = {}
    cache2 = {}
    # results is all last parent nodes
    results = []
    # path is the destination it takes to get to the location
    path = []
    # loop thru ancestors and store them in a cache of arrays for each locations possible ways.
    for ancestor in ancestors:
        if ancestor[1] in cache:
            cache[ancestor[1]].append(ancestor[0])
        else:
            cache[ancestor[1]] = [ancestor[0]]

    for ancestor in ancestors:
        if ancestor[1] in cache2:
            cache2[ancestor[1]].append(ancestor[0])
        else:
            cache2[ancestor[1]] = [ancestor[0]]
    # if our start goes no where then return -1 edge case
    if starting_node not in cache:
        return -1
    # loop while we still have something in memory
    while len(stack) > 0:
        # pop off the last item to look for possible directions
        current_array = stack.pop()
        if len(current_array) != 0:
            # loop thru all possible directions
            current = current_array.pop()
            # verify path correct
            cleaning = True
            while cleaning:
                if len(path) > 0:
                    check = path.pop()
                    if check in cache2:
                        for x in cache2[check]:
                            if x == current:
                                path.append(check)
                                cleaning = False
                else:
                    cleaning = False
# [[3, 5], ]
            path.append(current)
            if len(current_array) != 0:
                stack.append(current_array)
            if current in cache:
                stack.append(cache[current])
            else:
                # add to results the len of path and the current node.
                results.append((len(path), current))
                path.pop()
    # print(results, 'results')
    best = results[0]
    # find the longest len and tie breaker by smallest number
    for result in results:
        if result[0] == best[0]:
            if result[1] < best[1]:
                best = result
        if result[0] > best[0]:
            best = result
    # print(cache)
    # return the node associated to the longest len
    return best[1]


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1))  # 10
print(earliest_ancestor(test_ancestors, 3))  # 10)
print(earliest_ancestor(test_ancestors, 2))  # -1)
print(earliest_ancestor(test_ancestors, 4))  # -1)
print(earliest_ancestor(test_ancestors, 5))  # 4)
print(earliest_ancestor(test_ancestors, 6))  # 10)
print(earliest_ancestor(test_ancestors, 7))  # 4)
print(earliest_ancestor(test_ancestors, 9))  # 4)
print(earliest_ancestor(test_ancestors, 10))  # -1)
print(earliest_ancestor(test_ancestors, 11))  # -1)
