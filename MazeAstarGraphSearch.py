# to create a maze and to operate an agent on the maze , pyamaze  module is used.
from pyamaze import maze, agent
# to implement a priority queue , heapq module is used.
import heapq

# For calculating the heuristic value of the node h(n).
# Manhattan distance used as heuristic value.
def heuristic(node):
    return abs(node[0]-1) + abs(node[1]-1)

# This is the main function which is used to implement the A* algorithm.
def find(maze: maze):
    # In graph search we need to maintain a closed set i.e explored list.(visited set)
    explored = set()
    # Frontier is the priority queue.
    frontier = []
    start = (maze.rows, maze.cols)
    # adjacent nodes of start nodes' are to be added to the frontier.
    # We maintain the path,current/exploring node.
    for direction in "NEWS":
        if maze.maze_map[start][direction]:
            if direction == 'E':
                child = (start[0], start[1]+1)
            if direction == 'W':
                child = (start[0], start[1]-1)
            if direction == 'N':
                child = (start[0]-1, start[1])
            if direction == 'S':
                child = (start[0]+1, start[1])
            heapq.heappush(frontier, (heuristic(
                child)+1, child, [start, child]))

    # In case of frontier is not empty we proceed as follows.

    while frontier:
        fun, node, path = heapq.heappop(frontier)
        explored.add(node)
        if node == (1, 1):
            return path
        for direction in "NEWS":
            if maze.maze_map[node][direction]:
                if direction == 'E':
                    child = (node[0], node[1]+1)
                if direction == 'W':
                    child = (node[0], node[1]-1)
                if direction == 'N':
                    child = (node[0]-1, node[1])
                if direction == 'S':
                    child = (node[0]+1, node[1])
                if child not in explored:
                    # if the child node is already explored then not added to the frontier.
                    heapq.heappush(frontier, (heuristic(child) +len(path)+1, child, path+[child]))
    # if the path is not found then the path is returned as None.
    return None


if __name__ == "__main__":
    # Input the size of the maze .
    n = int(input("Enter the size of the maze: "))
    # creating a maze of size n*n.
    m = maze(n, n)
    m.CreateMaze(theme='dark')
    a = agent(m,filled=True,shape='arrow', footprints=True)
    result = find(m)
    # This solves the maze and displays the path.
    print(result)
    if result:
        d = dict()
        for i in range(len(result)) :
            if result[i] == (1,1) :
                break
            d[result[i]] = result[i+1]
        # simulates the agent on the path.
        m.tracePath({
            a : d,
        },delay=200)
    else :
        print("NO SOLUTION EXITS")
    m.run()
