import networkx as nx


def print_sorted_matching(matching: list):
    print(sorted([sorted(e) for e in matching]))


G = nx.Graph()
G.add_node('a', weight=10)
G.add_node('b', weight=8)
G.add_node('c', weight=9)
G.add_node('d', weight=6)
G.add_node('e', weight=1)
G.add_node('f', weight=3)
G.add_node('g', weight=2)
G.add_node('h', weight=5)
G.add_node('i', weight=7)
G.add_edges_from([
    ('a', 'b'), ('c', 'd'), ('a', 'c'), ('b', 'd'), ('e', 'f'),
    ('f', 'g'), ('g', 'e'), ('e', 'd'), ('d', 'h'), ('h', 'i')
])


def max_priority_matching(G: nx.Graph):
    G = G.copy()
    map_node_to_priority = {v: data["weight"] for v, data in G.nodes(data=True)}
    nodes_sorted_by_priority = sorted(G.nodes, key=map_node_to_priority.__getitem__)
    print("nodes_sorted_by_priority: ", nodes_sorted_by_priority)
    map_node_to_weight = {n: 2 ** i for i, n in enumerate(nodes_sorted_by_priority)}
    print("map_node_to_weight: ", map_node_to_weight)
    for v, data in G.nodes(data=True):
        data["weight"] = map_node_to_weight[v]
    return nx.max_weight_matching(pass_weight_to_edges(G))

def pass_weight_to_edges(G: nx.Graph):
    newG = nx.Graph()
    for n in G.nodes:
        newG.add_node(n)
    map_node = {v: data["weight"] for v, data in G.nodes(data=True)}
    for e in G.edges:
        newG.add_edge(e[0], e[1], weight=(map_node[e[0]] + map_node[e[1]]))
    print("map_edge_to_weight: ", newG.edges.data())
    return newG


print("\nMax priority matching:")
print_sorted_matching(list(max_priority_matching(G)))
