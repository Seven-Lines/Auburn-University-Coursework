import os
import sys
from collections import deque

def bfs(graph, start, target):
    visited = set()
    queue = [(start, 0)]  # (node, distance)

    while queue:
        node, distance = queue.pop(0)  # Dequeue
        if node == target:
            return distance
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, distance + 1))  # Enqueue

    return -1  # If no path found

def dfs(graph, start, target):
    visited = set()
    stack = [(start, 0)]  # (node, distance)

    while stack:
        node, distance = stack.pop()  # Pop from stack
        if node == target:
            return distance
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append((neighbor, distance + 1))  # Push onto stack

    return -1  # If no path found

def main():
    #-| Read Command-Line Arguments ------------------------------------------------|
    if len(sys.argv) != 4:
        print("Usage: python3 main.py <src_node> <tgt_node> <alg>")
        return

    src = sys.argv[1].strip()
    tgt = sys.argv[2].strip()
    alg = sys.argv[3].strip().lower()

    #-| Read File ------------------------------------------------------------------|
    file_name = "testcases.txt"

    if not os.path.exists(file_name):
        print(f"Error: {file_name} not found.")
        return

    #-| Convert file to custom graph schema ----------------------------------------|
    graph = {}

    with open(file_name, 'r') as file:
        try:
            for line in file:
                node1, node2 = line.strip().split(',')
                
                # Ensure the nodes exist in the graph
                if node1 not in graph:
                    graph[node1] = []
                if node2 not in graph:
                    graph[node2] = []
                
                # Add edges if not already present
                if node2 not in graph[node1]:
                    graph[node1].append(node2)
                if node1 not in graph[node2]:
                    graph[node2].append(node1)
        except ValueError:
            print(f"Unsupported file format. Boo womp.")
            return

    #-| Validate Nodes and Execute alg ---------------------------------------|
    match alg:
        case "bfs":
            result = bfs(graph, src, tgt)
        case "dfs":
            result = dfs(graph, src, tgt)
        case _:
            print("Error: Invalid algorithm choice. Please choose BFS or DFS.")
            return

    #-| Display Result ------------------------------------------------------------|
    if result:
        print(f"A path exists between {src} and {tgt} using {alg.upper()}.")
    else:
        print(f"No path exists between {src} and {tgt} using {alg.upper()}.")

if __name__ == "__main__":
    main()
