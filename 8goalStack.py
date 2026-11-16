
initial_state = {
    "OnTable(A)",
    "OnTable(B)",
    "OnTable(C)",
    "Clear(A)",
    "Clear(B)",
    "Clear(C)",
    "HandEmpty"
}


goal_state = {
    "OnTable(A)",
    "On(B,A)",
    "On(C,B)"
}


state = initial_state.copy()


goal_stack = []

plan = []



def execute(action):

    global state

    if action == "PICKUP(A)":
        pre = {"OnTable(A)", "Clear(A)", "HandEmpty"}
        delete = {"OnTable(A)", "Clear(A)", "HandEmpty"}
        add = {"Holding(A)"}

    elif action == "PICKUP(B)":
        pre = {"OnTable(B)", "Clear(B)", "HandEmpty"}
        delete = {"OnTable(B)", "Clear(B)", "HandEmpty"}
        add = {"Holding(B)"}

    elif action == "PICKUP(C)":
        pre = {"OnTable(C)", "Clear(C)", "HandEmpty"}
        delete = {"OnTable(C)", "Clear(C)", "HandEmpty"}
        add = {"Holding(C)"}

    elif action.startswith("STACK("):
        x, y = action[6:-1].split(",")
        x, y = x.strip(), y.strip()

        pre = {f"Holding({x})", f"Clear({y})"}
        delete = {f"Holding({x})", f"Clear({y})"}
        add = {f"On({x},{y})", f"Clear({x})", "HandEmpty"}

    elif action.startswith("PUTDOWN("):
        x = action[8:-1]

        pre = {f"Holding({x})"}
        delete = {f"Holding({x})"}
        add = {f"OnTable({x})", f"Clear({x})", "HandEmpty"}

    else:
        return False

    if pre.issubset(state):

        state.difference_update(delete)
        state.update(add)

        plan.append(action)
        print("Action:", action)
        print("Current State:", state)

        return True

    return False


def goal_stack_planning():

    print("Initial State:", state)
    print("\nPlanning started...\n")

  
    goal_stack.extend([
        "On(C,B)",
        "On(B,A)",
        "OnTable(A)"
    ])

    while goal_stack:

        goal = goal_stack.pop()

        if goal in state:
            continue

        if goal == "On(B,A)":

            if "Clear(A)" not in state:
                print("Cannot achieve On(B,A): A is not clear")
                return False

            if "OnTable(B)" in state:
                execute("PICKUP(B)")
                execute("STACK(B,A)")

        elif goal == "On(C,B)":

            if "Clear(B)" not in state:
                print("Cannot achieve On(C,B): B is not clear")
                return False

            if "OnTable(C)" in state:
                execute("PICKUP(C)")
                execute("STACK(C,B)")

        else:
            print("Goal:", goal)

    if goal_state.issubset(state):

        print("\nGoal Configuration Achieved!")
        print("\nFinal State:", state)
        print("\nFinal Plan:", plan)

        return True

    print("\nGoal could not be achieved!")
    return False



goal_stack_planning()
