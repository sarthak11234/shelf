

environment = {
    'A': 'Dirty',
    'B': 'Dirty'
}


location = 'A'


def vacuum_agent(location, status):
    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Right'
    elif location == 'B':
        return 'Left'


print("Initial Environment:", environment)

while 'Dirty' in environment.values():

    status = environment[location]

    action = vacuum_agent(location, status)

    print("\nLocation:", location)
    print("Status:", status)
    print("Action:", action)

    if action == 'Suck':
        environment[location] = 'Clean'
    elif action == 'Right':
        location = 'B'
    elif action == 'Left':
        location = 'A'

    print("Environment:", environment)

print("\nAll rooms are clean!")
print("Final Environment:", environment)
