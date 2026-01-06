# Create weights data
var_cst = 0.5

d = [24, 173,
      100, 150, 10, 60,
      76, 10, 41,
      52, 21, 152,
      37,
      94]

t = [14, 35,
     41, 78, 60, 28,
     35, 6, 21,
     25, 12, 12,
     8,
     50]

assert len(d) == len(t), 'len of t and d must be equal'

# Function to compute weights w(e) for factor of 5 years
def calculate_weights(d, t, var_cst = 0.5, factor = 1):
    return [var_cst * dist - factor * toll for dist, toll in zip(d,t) ]

w5y = calculate_weights(d,t)

hard_coded_weights = [-2.0, 51.5, 9.0, -3.0, -55.0, 2.0, 3.0, -1.0, -0.5, 1.0, -1.5, 64.0, 10.5, -3.0]

assert w5y == hard_coded_weights, 'there is error in compute_weights function'


# Create list of the edges of the network
edges = [('NM', 'N'), ('NM', 'W'),
         ('N', 'E'), ('N', 'EM'), ('N', 'S'), ('N', 'W'),
         ('E', 'EM'), ('E', 'S'), ('E', 'SM'),
         ('S', 'SM'), ('S', 'W'), ('S', 'WM'),
         ('SM', 'W'),
         ('W', 'WM')  
         ]

assert len(edges) == len(w5y), 'must be same amount of edges and edge weights'

# Generate adjacency list for network
def generate_network(edges=edges, weights=w5y):
    network = {}
    for (u, v), w in zip(edges, weights):
        if u not in network:
            network[u] = []
        if v not in network:
            network[v] = []
        network[u].append((v,w))
        network[v].append((u, w))       
    return network    


hard_coded_network = {
    'NM': [('N', -2.0), ('W', 51.5)],
    'N': [('NM', -2.0), ('E', 9.0), ('EM', -3.0), ('S', -55.0), ('W', 2.0)],
    'E': [('N', 9.0), ('EM', 3.0), ('S', -1.0), ('SM', -0.5)],
    'S': [('N', -55.0), ('E', -1.0), ('SM', 1.0), ('W', -1.5), ('WM', 64.0),],
    'SM': [('E', -0.5), ('S', 1.0), ('W', 10.5),],
    'W': [('NM', 51.5), ('N', 2.0), ('S', -1.5), ('SM', 10.5), ('WM', -3.0)],
    'EM': [('N', -3.0), ('E', 3.0), ],
    'WM': [('S', 64.0), ('W', -3.0)]
}

assert hard_coded_network == generate_network(), 'there is error in generate_network function'

def remove_edge(network, u, v):
    if u in network:
        network[u] = [e for e in network[u] if e[0] != v]
    if v in network:
        network[v] = [e for e in network[v] if e[0] != u]

    return network


edge_removed_hard_coded_network =  {
    'NM': [('N', -2.0), ('W', 51.5)],
    'N': [('NM', -2.0), ('E', 9.0), ('EM', -3.0), ('W', 2.0)],
    'E': [('N', 9.0), ('EM', 3.0), ('S', -1.0), ('SM', -0.5)],
    'S': [ ('E', -1.0), ('SM', 1.0), ('W', -1.5), ('WM', 64.0),],
    'SM': [('E', -0.5), ('S', 1.0), ('W', 10.5),],
    'W': [('NM', 51.5), ('N', 2.0), ('S', -1.5), ('SM', 10.5), ('WM', -3.0)],
    'EM': [('N', -3.0), ('E', 3.0), ],
    'WM': [('S', 64.0), ('W', -3.0)]
}

assert edge_removed_hard_coded_network == remove_edge(hard_coded_network, 'N', 'S'), 'there is error in remove_edge function'