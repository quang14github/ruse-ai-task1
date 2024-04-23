# Mouse and Cheese in a Maze

This project is a Python implementation of a maze-solving algorithm for a mouse to find a piece of cheese. The goal is to find the shortest path possible for the mouse to reach the cheese.

## Getting Started

To run the code, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/quang14github/ruse-ai-task1
   ```

2. Navigate to the project directory:

   ```shell
   cd ruse-ai-task1
   ```

3. Make sure that you have Python and pip:

   ```shell
   python --version
   ```

   or

   ```shell
   python3 --version
   ```

   and

   ```shell
   pip --version
   ```

   or

   ```shell
   pip3 --version
   ```

4. Install matplotlib library:

   ```shell
   pip install matplotlib
   ```

5. Run the `main.py` script:

   ```shell
   python main.py
   ```

## Algorithm

The algorithm used in this project is a modified version of the breadth-first search (BFS) algorithm. It explores all possible paths from the starting point (mouse) to the destination (cheese) in a maze.

## Usage

1. Modify the matrix variable to represent your maze. The maze should be a rectangular grid, where each character represents a cell. Use the following symbols:

- `1`: Wall (impassable)
- `0`: Path (passable)

2. Modify the `start` and `destination`:

- `start = (3,0)`
- `dest = (3,3)`
