
import heapq


goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])

            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_pos, 3)

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance



def get_neighbors(state):

    neighbors = []
    zero = state.index(0)

    row, col = divmod(zero, 3)

    moves = [
        (-1, 0),  
        (1, 0),   
        (0, -1),  
        (0, 1)   
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_pos = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def astar(start):

 
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, [start]))

    visited = {}

    while pq:

        f, g, state, path = heapq.heappop(pq)

        if state in visited and visited[state] <= g:
            continue

        visited[state] = g

       
        if state == goal:

            print("Goal Reached!")

            for step, s in enumerate(path):
                print("\nStep", step)
                for i in range(0, 9, 3):
                    print(s[i:i+3])

            print("\nTotal Moves:", g)
            return

    
        for neighbor in get_neighbors(state):

            new_g = g + 1
            new_h = heuristic(neighbor)
            new_f = new_g + new_h

            if neighbor not in visited or new_g < visited[neighbor]:

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    print("No solution exists!")


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

astar(start)
