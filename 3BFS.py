
from collections import deque



def bfs(initial, goal):

    queue = deque([(initial, [])])
    visited = set()

    while queue:

        state, path = queue.popleft()

      
        state_key = tuple(tuple(stack) for stack in state)

        if state_key in visited:
            continue

        visited.add(state_key)

     
        if state == goal:
            print("Goal State Reached!")
            print("\nSteps to reach goal:")

            for i, step in enumerate(path):
                print(i + 1, step)

            print("\nTotal Moves:", len(path))
            return

        for i in range(len(state)):

            if not state[i]:
                continue

            block = state[i][-1]

            for j in range(-1, len(state)):

                if i == j:
                    continue

                new_state = [list(stack) for stack in state]

                new_state[i].pop()

                if j == -1:
                    new_state.append([block])
                else:
                    new_state[j].append(block)

           
                new_state = [stack for stack in new_state if stack]

                new_state.sort()

                new_state = tuple(tuple(stack) for stack in new_state)

                if new_state not in visited:
                    queue.append((
                        [list(stack) for stack in new_state],
                        path + [new_state]
                    ))

    print("No solution found!")

initial_state = [['A'], ['B'], ['C']]


goal_state = [['A', 'B', 'C']]


bfs(initial_state, goal_state)
