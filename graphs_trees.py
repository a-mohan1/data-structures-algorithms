import numpy as np
import sys

# Graph BFS
def BFS(start_vert="S"):
    vert = start_vert
    visited_verts = []
    queue_vert = []
    path_complete = False
    
    while not path_complete:
        if visited[vert]==0:
            visited[vert] = 1
            queue_vert.append(vert)
            visited_verts.append(vert)
        for nextvert in graph_adj[vert]:
            if visited[nextvert]==0:
                visited[nextvert] = 1
                queue_vert.append(nextvert)
                visited_verts.append(nextvert)
        if len(queue_vert)!=0:
            vert = queue_vert.pop(0)
        else:
            path_complete = True
        
    return visited_verts

# Graph DFS
def  DFS(startvert="S"):

    visited_verts = []
    stack_vert = []
    path_complete = False
    vert = startvert

    while not path_complete:
        if visited[vert] == 0:
            visited[vert] = 1
            stack_vert.append(vert)
            visited_verts.append(vert)
        # Iterate through adjacency list to find next unvisited vertex
        i = 0
        while len(graph_adj[vert]) > i and visited[graph_adj[vert][i]]:
            i += 1
        if i < len(graph_adj[vert]):
            nextvert = graph_adj[vert][i]
            visited[nextvert] = 1
            stack_vert.append(nextvert)
            visited_verts.append(nextvert)
            vert = nextvert
        elif len(stack_vert) > 0:
            vert = stack_vert.pop()
        else:
            path_complete = True

    return visited_verts

# Prim's Algorithm
def prim(G):
    visited = []
    start_vidx = 0
    visited.append(start_vidx)
    total_cost = 0
    all_visited = False
    
    while not all_visited:
        # Find min edge cost to a new vertex from among all vertices in visited
        mincost = sys.maxsize
        addvertex = -sys.maxsize
        for vidx in visited:
            for next_idx, edge_cost in enumerate(G[vidx]):
                if next_idx not in visited and edge_cost != 0 and mincost > edge_cost:
                    mincost = edge_cost
                    addvertex = next_idx
        # Add next unvisited vertex with lowest edge cost to visited
        if addvertex == -sys.maxsize:
            all_visited = True
        else:
            total_cost += mincost
            visited.append(addvertex)
            print("Min edge cost and next vertex: ", mincost, addvertex)

    return total_cost, visited

# Dijkstra's Algorithm
def dijkstra(G, S=0):
     visited = []
     visited.append(S)
     distances = [0]
     all_visited = False
     while not all_visited:
          mindist = sys.maxsize        
          for idx, vidx in enumerate(visited):
               for nextvert, edge_cost in enumerate(G[vidx]):
                    if (edge_cost!=0) and (nextvert not in visited) and (mindist > distances[idx] + edge_cost):
                         mindist = distances[idx] + edge_cost
                         addvert = nextvert

          if mindist == sys.maxsize:
               all_visited = True
          else:
               distances.append(mindist)
               visited.append(addvert)
               print("Next min path distance and vertex", mindist, addvert)
               print(distances, visited)

     return distances, visited
                   
# Binary Tree
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Inorder traversal
def InOrderTraversal(rootnode):
    tree_vals = []
    if rootnode:
        left_tree = InOrderTraversal(rootnode.left)
        if left_tree:
            tree_vals.extend(left_tree)
        tree_vals.append(rootnode.val)
        right_tree = InOrderTraversal(rootnode.right)
        if right_tree:
            tree_vals.extend(right_tree)
    return tree_vals

# Preorder traversal
def PreOrderTraversal(rootnode):
    tree_vals = []
    if rootnode:
        tree_vals.append(rootnode.val)
        left_tree = PreOrderTraversal(rootnode.left)
        if left_tree:
            tree_vals.extend(left_tree)
        right_tree = PreOrderTraversal(rootnode.right)
        if right_tree:
            tree_vals.extend(right_tree)
    return tree_vals

# Postorder traversal
def PostOrderTraversal(rootnode):
    tree_vals = []
    if rootnode:
        left_tree = PostOrderTraversal(rootnode.left)
        if left_tree:
            tree_vals.extend(left_tree)
        right_tree = PostOrderTraversal(rootnode.right)
        if right_tree:
            tree_vals.extend(right_tree)
        tree_vals.append(rootnode.val)
    return tree_vals

# Binary Search Tree
class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_data(self, data):
        new_node = BST(data)
        if self.val:
            if self.val > data:
                if not self.left:
                    self.left = new_node
                else:
                    self.left.insert_data(data)
            elif self.val < data:
                if not self.right:
                    self.right = new_node
                else:
                    self.right.insert_data(data)
        else:
            self.val = data

    def search_data(self, data):
        if not self.val:
            return -1
        if self.val == data:
            return self.val
        elif self.val > data:
            if self.left:
                return self.left.search_data(data)
            else:
                return -1
        else:
            if self.right:
                return self.right.search_data(data)
            else:
                return -1
        
    # Inorder traversal
    def InOrderTraversal(self):
        if self.left:
            self.left.InOrderTraversal()
        print(self.val)
        if self.right:
            self.right.InOrderTraversal()
        
    # Preoder Traversal
    def PreOrderTraversal(self):
        print(self.val)
        if self.left:
            self.left.PreOrderTraversal()
        if self.right:
            self.right.PreOrderTraversal()

    # Postoder Traversal
    def PostOrderTraversal(self):
        if self.left:
            self.left.PostOrderTraversal()
        if self.right:
            self.right.PostOrderTraversal()
        print(self.val)


if __name__=="__main__":
    # Graph BFS and DFS
    graph_adj = {'S': ['A', 'B', 'C'],
                'A': ['S', 'D'],
                'B': ['S', 'E'],
                'C': ['S', 'F'],
                'D': ['A', 'G'],
                'E': ['B', 'G'],
                'F': ['C', 'G'],
                'G': ['D', 'E', 'F']
                }
    
    for algo in ["BFS", "DFS"]:
        visited = {'S': 0,
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0,
            'E': 0,
            'F': 0,
            'G': 0
        }
        print(BFS()) if algo=="BFS" else print(DFS())
    
    # Prim's algorithm
    # Adjacency matrix 
    G = [[0, 9, 75, 0, 0],
        [9, 0, 95, 19, 42],
        [75, 95, 0, 51, 66],
        [0, 19, 51, 0, 31],
        [0, 42, 66, 31, 0]]
    print(prim(G))

    # Dijkstra's algorithm
    # Adjacency matrix 
    G =  [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
    print(dijkstra(G))
