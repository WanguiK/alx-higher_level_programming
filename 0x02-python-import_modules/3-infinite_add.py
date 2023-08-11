#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def add_arguments(argvs):
        total = 0
        for arg in argvs:
            total += int(arg)
        return total
    argvs = sys.argv[1:]
    result = add_arguments(argvs)
    print(result)
