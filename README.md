# 🧭 Maze Solver using DFS and BFS

A Python-based visualization of **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** algorithms to solve randomly generated mazes using the `pyamaze` library. This project helps understand and compare the behavior, path length, search space, and performance of both algorithms.

## 🧠 Features

- Generates a random maze with **custom dimensions**
- Solves the maze from **bottom-right** to **top-left**
- Uses both:
  - 🔵 **DFS (Depth-First Search)** — explores deeper paths first
  - 🟡 **BFS (Breadth-First Search)** — explores level by level
- Visual path tracing and performance comparison:
  - ✅ Path Length
  - 🔍 Search Space Size
  - ⏱️ Execution Time (via `timeit`)

## 🖥️ Libraries Used

- [`pyamaze`](https://github.com/srbhr/pyamaze) – for maze generation and visualization
- `timeit` – to measure execution time
- `collections.deque` – efficient queue for BFS

## 🔧 How It Works

1. A maze is generated using `m.CreateMaze()`
2. Two functions – `dfs()` and `bfs()` – solve the maze
3. Each algorithm:
   - Builds the full search path
   - Traces the shortest valid path
4. Both paths are displayed with separate agents and colors
5. Statistics are shown directly on the maze:
   - Path lengths
   - Search path lengths
   - Execution times

## 📦 Installation

1. Install the required package:
   ```bash
   pip install pyamaze
   ```

2. Clone the repository and run the script:
   ```bash
   python maze_solver.py
   ```

## 📸 Visual Representation

- **Cyan Agent**: BFS Path  
- **Yellow Agent**: DFS Path  
- Stats (path length, search effort, time) appear as text labels on the maze.

## 🧪 Example Outputs

| Metric               | DFS             | BFS             |
|----------------------|------------------|------------------|
| Path Length          | Shorter in some cases | Optimal in most cases |
| Search Path Length   | Explores deep | Explores wide |
| Execution Time       | Fast | Usually faster |

## 💡 Educational Use Cases

- Data structure & algorithm learning
- AI pathfinding demos
- Maze solving challenges
- Visualization of traversal strategies

## 🛠️ To Do

- Add support for A* and Dijkstra's algorithm
- Export results as images or logs
- Allow user-defined start/end points
