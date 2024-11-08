import collections
import argparse

def parse_dot_file(file_path):
    """Parse the .dot file to create a graph in adjacency list format."""
    graph = collections.defaultdict(list)
    with open(file_path, "r") as file:
        for line in file:
            if "->" in line:
                # Remove unnecessary characters and split by '->' to extract nodes
                target, source = line.strip().replace(";", "").split("->")
                source = source.strip().strip('"')
                target = target.strip().strip('"')
                graph[source].append(target)
    return graph


def bfs_shortest_path(graph, start_node):
    """Perform BFS to find the shortest path from start_node to all reachable nodes."""
    distances = collections.defaultdict(lambda: -1)  # Default distance is -1
    queue = collections.deque([(start_node, 0)])  # Queue of (node, distance)
    distances[start_node] = 0  # Distance to itself is 0

    while queue:
        node, distance = queue.popleft()
        for neighbor in graph[node]:
            if distances[neighbor] == -1:  # Only visit unvisited nodes
                distances[neighbor] = distance + 1
                queue.append((neighbor, distance + 1))

    return distances


def main(start_node: str):
    # Example usage:
    file_path = "import_graph.dot"  # Replace with your actual .dot file path
    graph = parse_dot_file(file_path)

    shortest_paths = bfs_shortest_path(graph, start_node)

    # Output the results
    for node, distance in shortest_paths.items():
        print(f"{node}: {distance}")

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--start_node', type=str, required=True)
    args = args.parse_args()
    main(args.start_node)