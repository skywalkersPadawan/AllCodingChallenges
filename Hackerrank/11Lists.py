def performCommands(commands):
    result = []
    for cmd in commands:
        parts = cmd.split()
        if parts[0] == "insert":
            i, e = int(parts[1]), int(parts[2])
            result.insert(i, e)

            # this is an example of a single line coment section under the main line
            """ this is an example of a multiline comment section under the main file"""
