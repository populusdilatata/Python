import random

def generate_random_graph(filename, num_vertices=200, max_edges_per_vertex=10, max_weight=100):
    with open(filename, 'w') as f:
        for vertex in range(1, num_vertices + 1):
            num_edges = random.randint(1, max_edges_per_vertex)
            edges = []
            for _ in range(num_edges):
                neighbor = random.randint(1, num_vertices)
                while neighbor == vertex:
                    neighbor = random.randint(1, num_vertices)  # Ensure no self-loops
                weight = random.randint(1, max_weight)
                edges.append(f"{neighbor},{weight}")
            f.write(f"{vertex} {' '.join(edges)}\n")

# Generate the random graph and save it to 'dijkstraDataB.txt'
generate_random_graph('dijkstraData.txt')