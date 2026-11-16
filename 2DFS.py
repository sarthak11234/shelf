
def water_jug_dfs(capacity_a, capacity_b, target):

    stack = [(0, 0)]
    visited = set()
    parent = {}

    while stack:

        state = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        a, b = state

        
        if a == target or b == target:
            path = []

            while state is not None:
                path.append(state)
                state = parent.get(state)

            path.reverse()

            print("Solution Found:")
            for step in path:
                print(step)

            return

       
        next_states = [
            (capacity_a, b), 
            (a, capacity_b),  
            (0, b),          
            (a, 0),           
            (a - min(a, capacity_b - b),
             b + min(a, capacity_b - b)),  
            (a + min(b, capacity_a - a),
             b - min(b, capacity_a - a))  
        ]

        for next_state in next_states:

            if next_state not in visited:
                if next_state not in parent:
                    parent[next_state] = state

                stack.append(next_state)

    print("No solution exists!")



capacity_a = 4
capacity_b = 3
target = 2

water_jug_dfs(capacity_a, capacity_b, target)
