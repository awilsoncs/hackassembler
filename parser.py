def command_type(command):
    if command == "":
        return "NONE"
    if command[0] == "@":
        return "A_COMMAND"
    elif command[0] == "(":
        return "L_COMMAND"
    else:
        return "C_COMMAND"


def symbol(command):
    if command_type(command) == "A_COMMAND":
        return command[1:]
    elif command_type(command) == "L_COMMAND":
        return command[1:-1]
    else:
        raise ValueError()


def dest(command):
    if command_type(command) is not "C_COMMAND":
        raise ValueError()
    if "=" not in command:
        return ""

    n = command.find("=")
    return command[:n]


def comp(command):
    start = command.find("=")
    end = command.find(";")

    if end < 0:
        end = len(command)

    return command[start+1:end]


def jump(command):
    if ";" not in command:
        return ""

    n = command.find(";")
    return command[n+1:]