"""Solution for HackerRank challenge: Lovely Triplets
"""

def lovely_triplets(P, Q):
    """Description
    """
    nodes = P * Q + 1
    edges = []
    for i in xrange(1, nodes - nodes % 2):
        edges.append([i, i + 1])
    edges.append([nodes - nodes % 2, 1])
    if (nodes % 2):
        edges.append([1, nodes])
    return [[nodes, len(edges)]] + edges

def main():
    """Receives input from stdin, provides output to stdout.
    """
    quantity, distance = input().split(' ')
    result = lovely_triplets(quantity, distance)
    print result

if __name__ == '__main__':
    main()
