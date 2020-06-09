# so we look for what values we can point to tuples are (3, 5) we want are start location to be second in tuple and destination as first


def earliest_ancestor(ancestors, starting_node):
    print(ancestors)
    print(starting_node)

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 1)  # 10
# earliest_ancestor(test_ancestors, 2) #-1)
# earliest_ancestor(test_ancestors, 3) #10)
# earliest_ancestor(test_ancestors, 4) #-1)
# earliest_ancestor(test_ancestors, 5) #4)
# earliest_ancestor(test_ancestors, 6) #10)
# earliest_ancestor(test_ancestors, 7) #4)
# earliest_ancestor(test_ancestors, 9) #4)
# earliest_ancestor(test_ancestors, 10) #-1)
# earliest_ancestor(test_ancestors, 11) #-1)
