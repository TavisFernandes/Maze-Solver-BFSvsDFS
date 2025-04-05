from pyamaze import maze, agent, COLOR, textLabel
from timeit import timeit
from collections import deque

def dfs(maze):
    stack = [(maze.rows, maze.cols)]
    visited = set()
    search_path = []
    dfs_path = {}
    fwd_dfs_path = []
    
    while stack:
        cell = stack.pop()
        if cell in visited:
            continue
        visited.add(cell)
        search_path.append(cell)
        if cell == (1, 1):
            break
        
        for direction in 'ESNW':  # East, South, North, West
            if maze.maze_map[cell][direction]:
                next_cell = (cell[0] + (direction == 'S') - (direction == 'N'),
                             cell[1] + (direction == 'E') - (direction == 'W'))
                if next_cell not in visited:
                    stack.append(next_cell)
                    dfs_path[next_cell] = cell
    
    cell = (1, 1)
    while cell != (maze.rows, maze.cols):
        fwd_dfs_path.append(cell)
        cell = dfs_path.get(cell, (maze.rows, maze.cols))
    fwd_dfs_path.reverse()
    
    return search_path, dfs_path, fwd_dfs_path

def bfs(maze):
    queue = deque([(maze.rows, maze.cols)])
    visited = set()
    search_path = []
    bfs_path = {}
    fwd_bfs_path = []
    
    while queue:
        cell = queue.popleft()
        if cell in visited:
            continue
        visited.add(cell)
        search_path.append(cell)
        if cell == (1, 1):
            break
        
        for direction in 'ESNW':  # East, South, North, West
            if maze.maze_map[cell][direction]:
                next_cell = (cell[0] + (direction == 'S') - (direction == 'N'),
                             cell[1] + (direction == 'E') - (direction == 'W'))
                if next_cell not in visited:
                    queue.append(next_cell)
                    bfs_path[next_cell] = cell
    
    cell = (1, 1)
    while cell != (maze.rows, maze.cols):
        fwd_bfs_path.append(cell)
        cell = bfs_path.get(cell, (maze.rows, maze.cols))
    fwd_bfs_path.reverse()
    
    return search_path, bfs_path, fwd_bfs_path

m = maze(20, 30)
m.CreateMaze(1, 30, loopPercent=100)

search_path_dfs, dfs_path, fwd_dfs_path = dfs(m)
search_path_bfs, bfs_path, fwd_bfs_path = bfs(m)

textLabel(m, 'DFS Path Length', len(fwd_dfs_path) + 1)
textLabel(m, 'BFS Path Length', len(fwd_bfs_path) + 1)
textLabel(m, 'DFS Search Length', len(search_path_dfs) + 1)
textLabel(m, 'BFS Search Length', len(search_path_bfs) + 1) 

a = agent(m, footprints=True, color=COLOR.cyan, filled=True)
b = agent(m, footprints=True, color=COLOR.yellow)
m.tracePath({a: fwd_bfs_path}, delay=100)
m.tracePath({b: fwd_dfs_path}, delay=100)

t1 = timeit(stmt='dfs(m)', number=1000, globals=globals())
t2 = timeit(stmt='bfs(m)', number=1000, globals=globals())

textLabel(m, 'DFS Time', t1)
textLabel(m, 'BFS Time', t2)

m.run()
