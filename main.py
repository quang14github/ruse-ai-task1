from collections import deque
import matplotlib.pyplot as plt

# Define a function to check if a move is valid
def is_valid_move(matrix, visited, row, col):
    # Check if the move is within the matrix boundaries and the square is not a "1"
    return (
        0 <= row < len(matrix)
        and 0 <= col < len(matrix[0])
        and matrix[row][col] != 1
        and not visited[row][col]
    )


# Define a function to perform a Breadth-First Search
def bfs(start, dest, matrix, previous):
    # Initialize the visited matrix
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]

    # Define the directions for moving: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Create a queue for BFS
    queue = deque([(start[0], start[1])])

    # Mark the starting square as visited
    visited[start[0]][start[1]] = True

    while queue:
        row, col = queue.popleft()

        # Check if we reached the destination square
        if (row, col) == (dest[0], dest[1]):
            return True

        # Explore all possible directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if is_valid_move(matrix, visited, new_row, new_col):
                # Mark the new square as visited and add it to the queue
                visited[new_row][new_col] = True
                previous[new_row][new_col] = (row, col)
                queue.append((new_row, new_col))

    return False


# Example usage
matrix = [
    [0, 1, 1, 1],
    [0, 0, 1, 0],
    [1, 0, 1, 1],
    [0, 0, 0, 0],
]

# Define a matrix to store the previous square for each square
previous = [[(-1, -1)] * len(matrix[0]) for _ in range(len(matrix))]

# Define the starting and destination squares
start = (0,0)
dest = (3,3)

# Visualize the matrix
plt.imshow(matrix, cmap="binary")
plt.xticks(range(len(matrix[0])))
plt.yticks(range(len(matrix)))

# Draw gridlines starting from 0 to the length of the matrix and from 0 to the width of the matrix
for i in range(len(matrix) + 1):
    plt.axhline(i - 0.5, color="black", linewidth=2)
for i in range(len(matrix[0]) + 1):
    plt.axvline(i - 0.5, color="black", linewidth=2)

# Mark the starting and ending squares
plt.text(start[1], start[0], "Mouse", ha="center", va="center", color="black")
plt.text(dest[1], dest[0], "Cheese", ha="center", va="center", color="black")

# Check if there is a path from the starting square to the destination square
if bfs(start, dest, matrix, previous):
    # Retrieve the route from start to destination
    route = []
    current = dest
    while current != start:
        route.append(current)
        current = previous[current[0]][current[1]]
    route.append(start)
    route.reverse()
    # convert the route to a string
    str_route = [f"({row},{col})" for row, col in route]
    # Visualize the route
    route_x = [position[1] for position in route]
    route_y = [position[0] for position in route]
    plt.plot(route_x, route_y, color="red", linewidth=1)
    plt.title(f"Route: {str_route}")
    plt.show()
else:
    plt.title("The mouse cannot reach the cheese")
    plt.show()