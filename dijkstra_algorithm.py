class Dijkstra:
    def find_shortest_paths(self, graph, start):
        dist = {point: float('inf') for point in graph}
        dist[start] = 0
        visited = set()

        while len(visited) < len(graph):
            current_point = min((point, distance) for point, distance in dist.items() if point not in visited)[0]
            visited.add(current_point)

            for neighbor, weight in graph[current_point].items():
                distance = dist[current_point] + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
        
        print(f'Shortest distances from {start}: {dist}')
