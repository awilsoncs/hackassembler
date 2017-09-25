def dest(command):
    """Return the dest code of a given command value"""

    values = {
        "": "000",
        "A": "100",
        "D": "010",
        "M": "001",
        "AD": "110",
        "MD": "011",
        "AM": "101",
        "AMD": "111"
    }

    if command in values:
        return values[command]
    raise ValueError("Dest code not found: {0}".format(command))


def comp(command):
    values = {
        "0": "0101010",
        "1": "0111111",
        "-1": "0111010",
        "D": "0001100",
        "A": "0110000",
        "!D": "0001101",
        "!A": "0110001",
        "-D": "0001111",
        "-A": "0110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "D+A": "0000010",
        "D-A": "0010011",
        "A-D": "0000111",
        "D&A": "0000000",
        "D|A": "0010101",
        "M": "1110000",
        "!M": "1110001",
        "-M": "1110011",
        "M+1": "1110111",
        "M-1": "1110010",
        "D+M": "1000010",
        "D-M": "1010011",
        "M-D": "1000111",
        "D&M": "1000000",
        "D|M": "1010101"
    }

    if command in values:
        return values[command]
    raise ValueError("Comp code not found: {0}".format(command))


def jump(command):
    values = {
        "": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111"
    }

    if command in values:
        return values[command]
    raise ValueError("Jump code not found: {0}".format(command))

