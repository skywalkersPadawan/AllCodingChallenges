def performCommands(commands):
    result = []
    for cmd in commands:
        parts = cmd.split()
        if parts[0] == "insert":
            i, e = int(parts[1]), int(parts[2])
            result.insert(i, e)
        elif parts[0] == "print":
            print(result)
        elif parts[0] == "remove":
            e = int(parts[1])
            result.remove(e)
        elif parts[0] == "append":
            e = int(parts[1])
            result.append(e)
        elif parts[0] == "sort":
            result.sort()
        elif parts[0] == "pop":
            result.pop()
        elif parts[0] == "reverse":
            result.reverse()


# here we will be testing the function with the example input
if __name__ == "__main__":
    n = int(input())
    commands = []
    for i in range(n):
        cmd = input()
        commands.append(cmd)

    performCommands(commands)
