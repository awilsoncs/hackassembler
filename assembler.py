import argparse
import parser
import code
import re

symbols = {
    "R0": "0",
    "R1": "1",
    "R2": "2",
    "R3": "3",
    "R4": "4",
    "R5": "5",
    "R6": "6",
    "R7": "7",
    "R8": "8",
    "R9": "9",
    "R10": "10",
    "R11": "11",
    "R12": "12",
    "R13": "13",
    "R14": "14",
    "R15": "15",
    "SP": "0",
    "LCL": "1",
    "ARG": "2",
    "THIS": "3",
    "THAT": "4",
    "SCREEN": "16384",
    "KBD": "24576"
}

ram_address = 16

verbose = False


def main():
    argparser = add_args()
    args = argparser.parse_args()

    file_name = args.source
    target_name = args.target

    verbose = args.verbose

    # build symbol table
    if verbose:
        print("Beginning symbol pass")
    with open(file_name, "r") as source:
        line = 0
        for command in source:
            command = clear_trash(command)
            if parser.command_type(command) in ["A_COMMAND", "C_COMMAND"]:
                line += 1
            elif parser.command_type(command) is "L_COMMAND":
                if verbose:
                    print("Pseudocommand found at line {0}: {1}".format(line, command))
                symbols[parser.symbol(clear_trash(command))] = str(line)
                print("Symbol {0} installed at line: {1}".format(parser.symbol(clear_trash(command)), line))

    # assemble code
    if verbose:
        print("Beginning assembly pass")
    with open(file_name, "r") as source, open(target_name, "w") as target:
        for command in source:
            command = clear_trash(command)
            if len(command) is not 0:
                target.write(get_code(command))


def get_code(command):

    command = clear_trash(command)

    output = ""
    if parser.command_type(command) == "A_COMMAND":
        output = "0" + address_of(parser.symbol(command)) + "\n"
    elif parser.command_type(command) == "L_COMMAND":
        pass
    elif parser.command_type(command) == "C_COMMAND":
        dest = code.dest(parser.dest(command))
        jump = code.jump(parser.jump(command))
        comp = code.comp(parser.comp(command))

        output = "111" + comp + dest + jump + "\n"
    else:
        raise ValueError("Code not a valid command: {0}".format(command))

    return output


def clear_trash(command):
    """Remove whitespace and comments"""
    return command.split("//")[0].strip()


def address_of(symbol):
    global ram_address

    pattern = re.compile("[0-9]+")
    if pattern.match(symbol):
        return "{0:b}".format(int(symbol)).zfill(15)

    if symbol in symbols.keys():
        return address_of(symbols[symbol])

    symbols[symbol] = str(ram_address)
    ram_address += 1
    return address_of(symbol)


def add_args():
    """Assign all arguments for the assembler"""
    parser = argparse.ArgumentParser(
        description="Assemble HACK files to machine code."
    )

    parser.add_argument("-v",
                        "--verbose",
                        help="display additional output",
                        action="store_true")
    parser.add_argument("source",
                        help="HACK file to be assembled")
    parser.add_argument("target",
                        help="name of file to be written")
    return parser


if __name__ == "__main__":
    main()
