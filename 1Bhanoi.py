
from collections import deque


def tower_of_hanoi(n):


    start = (tuple(range(n, 0, -1)), (), ())
    goal = ((), (), tuple(range(n, 0, -1)))

    
    queue = deque([(start, [])])

    visited = {start}

    rods = ['A', 'B', 'C']

    while queue:

        state, path = queue.popleft()

        # Check goal state
        if state == goal:
            print("Goal State Reached!\n")

            for step, move in enumerate(path, 1):
                print(f"Step {step}: Move disk {move[0]} "
                      f"from {move[1]} to {move[2]}")

            print("\nTotal Moves:", len(path))
            return

  
        for i in range(3):

          
            if not state[i]:
                continue

            disk = state[i][-1]

            for j in range(3):

                if i == j:
                    continue

               
                if not state[j] or disk < state[j][-1]:

                    new_state = [list(rod) for rod in state]

             
                    new_state[i].pop()
                    new_state[j].append(disk)

                    new_state = tuple(
                        tuple(rod) for rod in new_state
                    )

                    if new_state not in visited:

                        visited.add(new_state)

                        move = (disk, rods[i], rods[j])

                        queue.append((
                            new_state,
                            path + [move]
                        ))



n = int(input("Enter number of disks: "))

tower_of_hanoi(n)
