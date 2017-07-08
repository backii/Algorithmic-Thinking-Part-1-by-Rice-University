"""
digraqphs representations

"""


EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}

GRAPH7 = {0: set([1, 2, 3, 4]),
          1: set([0, 2, 3, 4]),
          2: set([0, 1, 3, 4]),
          3: set([0, 1, 2, 4]),
          4: set([0, 1, 2, 3]),
          5: set([2, 3, 4]),
          6: set([0, 1, 4]),
          7: set([0, 1, 2, 3]),
          8: set([0, 1, 4, 7]),
          9: set([2, 4]),
          10: set([1, 2, 4]),
          11: set([1, 3, 4, 7]),
          12: set([0, 2, 3]),
          13: set([0, 2, 4, 10]),
          14: set([0, 2, 3, 4, 13])}


def compute_in_degree(digraph):
    """
    compute in degree distribution per each node
    return dictonary with in degree distribution

    """
    zero_value = [0 for x in digraph.keys()]
    in_degree_dict = dict(zip(digraph.keys(), zero_value))

    for nodes in digraph.values():

        for node in nodes:
            in_degree_dict[node] = in_degree_dict.get(node, 0) + 1

    return in_degree_dict

print compute_in_degree(GRAPH7)


def in_degree_distribution(digraph):
    """
    Compute in degree distribution

    return dict with in degree distribution
    """

    distro = compute_in_degree(digraph)
    distribution = {}

    for node_value in distro.values():

        distribution[node_value] = len(list(item for item, value in distro.items()
                                            if value == node_value))

    print distribution
    return distribution

in_degree_distribution(GRAPH7)