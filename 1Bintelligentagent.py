


class ModelBasedAgent:

    def __init__(self, grid, start, goal):
        self.grid = grid
        self.position = start
        self.goal = goal

       
        self.visited = set()
        self.internal_map = {}

    def update_state(self):
      
        self.visited.add(self.position)

        self.internal_map[self.position] = self.grid[
            self.position[0]
        ][self.position[1]]

    def get_action(self):
        row, col = self.position

       
        moves = [
            (-1, 0, "UP"),
            (1, 0, "DOWN"),
            (0, -1, "LEFT"),
            (0, 1, "RIGHT")
        ]

        for dr, dc, action in moves:
            new_row = row + dr
            new_col = col + dc
            new_pos = (new_row, new_col)

          
            if (0 <= new_row < len(self.grid) and
                0 <= new_col < len(self.grid[0])):

               
                if (self.grid[new_row][new_col] != 1 and
                    new_pos not in self.visited):
                    return action, new_pos

        return None, None

    def navigate(self):
        print("Starting Position:", self.position)
        print("Goal Position:", self.goal)

        while self.position != self.goal:

            self.update_state()

            action, new_pos = self.get_action()

            if action is None:
                print("No unvisited path found!")
                return

            print("Current Position:", self.position)
            print("Action:", action)

           
            self.position = new_pos

        self.update_state()

        print("\nGoal Reached!")
        print("Final Position:", self.position)
        print("Visited Cells:", self.visited)
        print("Internal Map:", self.internal_map)



grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

agent = ModelBasedAgent(grid, start, goal)
agent.navigate()
