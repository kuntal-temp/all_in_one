"""
    https://towardsdatascience.com/10-graph-algorithms-visually-explained-e57faa1336f3
"""

# Graph Algo
graph = {}
def create_graph(graph, u, v):
    if u not in graph.keys():
        graph[u] = list(v)
    else:
        graph[u].append(v)

create_graph(graph,'a','c')
create_graph(graph,'b','c')
create_graph(graph,'b','e')
create_graph(graph,'c','d')
create_graph(graph,'c','e')
create_graph(graph,'c','a')
create_graph(graph,'c','b')
create_graph(graph,'e','b')
create_graph(graph,'d','c')
create_graph(graph,'e','c')
print("graph = ", graph)


def bfs(graph, root):
    visited = set()
    queue = []
    visited.add(root)
    queue.append(root)
    
    while queue:
        vertex = queue.pop(0)
        print("vertex : ", vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=",")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

bfs(graph, '5')
dfs(visited, graph, '5')

"""
BFS can be used to find the shortest path, with unit weight edges, 
from a node (origional source) to another. Whereas, DFS can be used to 
exhaust all the choices because of its nature of going in depth, like 
discovering the longest path between two nodes in an acyclic graph.
"""



#####################################
       # Dijkstra's Algorithm #
#####################################

'''
Dijkstra's algorithm allows us to find the shortest path between any two vertices of a graph
Dijkstra's algorithm = BFS with PriorityQueue

https://www.programiz.com/dsa/dijkstra-algorithm
https://www.programiz.com/dsa/bellman-ford-algorithm
https://www.programiz.com/dsa/prim-algorithm
https://www.javatpoint.com/breadth-first-search-algorithm
'''











#####################################
    # Backtracking Algorithm #
#####################################

# Maze size
n = 4

def isValid(n, maze, x, y, res):
    if x >= 0 and y >= 0 and x < n and y < n and maze[x][y] == 1 and res[x][y] == 0:
        return True
    return False

def RatMaze(n, maze, move_x, move_y, x, y, res):
	# if (x, y is goal) return True
	if x == n-1 and y == n-1:
		return True

	for i in range(n):
        # Generate new value of x, y
		x_new = x + move_x[i]
		y_new = y + move_y[i]
		# Check if maze[x][y] is valid
		if isValid(n, maze, x_new, y_new, res):
			# mark x, y as part of solution path
			res[x_new][y_new] = 1
			if RatMaze(n, maze, move_x, move_y, x_new, y_new, res):
				return True
			res[x_new][y_new] = 0
	return False


def solveMaze(maze):
	# Creating a 4 * 4 2-D list
	res = [[0 for i in range(n)] for i in range(n)]
	res[0][0] = 1

	# x,y matrix for each direction
	move_x = [-1, 1, 0, 0]
	move_y = [0, 0, -1, 1]

	if RatMaze(n, maze, move_x, move_y, 0, 0, res):
		for i in range(n):
			for j in range(n):
				print(res[i][j], end=' ')
			print()
	else:
		print('Solution does not exist')


# Initialising the maze
maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]

solveMaze(maze)

