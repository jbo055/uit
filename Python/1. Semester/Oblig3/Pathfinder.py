import random

def create_grid(size, goal_value, grading_factor):
    grid = [[0 for _ in range(size)] for _ in range(size)]
    goal_x, goal_y = random.randint(0, size-1), random.randint(0, size-1)
    grid[goal_x][goal_y] = goal_value

    for i in range(size):
        for j in range(size):
            if (i, j) != (goal_x, goal_y):
                distance = abs(goal_x - i) + abs(goal_y - j)
                grid[i][j] = max(0, goal_value - grading_factor * distance)
    
    return grid, (goal_x, goal_y)

def find_path(grid, start, goal):
    path = [start]
    current = start

    while current != goal:
        x, y = current
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        valid_neighbors = [(nx, ny) for nx, ny in neighbors if 0 <= nx < len(grid) and 0 <= ny < len(grid)]
        next_step = max(valid_neighbors, key=lambda pos: grid[pos[0]][pos[1]])
        path.append(next_step)
        current = next_step

    return path

def main():
    size = 10
    goal_value = 200
    grading_factor = 10

    grid, goal = create_grid(size, goal_value, grading_factor)
    start = (random.randint(0, size-1), random.randint(0, size-1))

    path = find_path(grid, start, goal)
    print(f"Start: {start}")
    print(f"Goal: {goal}")
    print(f"Path: {path}")

if __name__ == "__main__":
    main()