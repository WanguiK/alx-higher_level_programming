#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def print_arguments():
        argv = sys.argv[1:]
        num_argv = len(argv)
        if num_argv == 0:
            print("{} arguments.".format(num_argv))
        else:
            if num_argv == 1:
                print("{} argument:".format(num_argv))
            else:
                print("{} arguments:".format(num_argv))
            for i, arg in enumerate(argv, start=1):
                print(i, ":", arg)
print_arguments()
