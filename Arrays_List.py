if __name__ == '__main__':
    N = int(input())  # Number of commands
    my_list = []  # Initialize the list

    # Define functions for each command
    commands = {
        'insert': lambda x: my_list.insert(int(x[1]), int(x[2])),
        'print': lambda x: print(my_list),
        'remove': lambda x: my_list.remove(int(x[1])),
        'append': lambda x: my_list.append(int(x[1])),
        'sort': lambda x: my_list.sort(),
        'pop': lambda x: my_list.pop(),
        'reverse': lambda x: my_list.reverse()
    }

    # Iterate through each command
    for _ in range(N):
        command = input().split()  # Split the input command into parts
        commands[command[0]](command)
