#!/usr/bin/python3
a = 1
b = 2

if __name__ == "__main__":
    from add_0 import add

    result = add(a, b)

    print("{:d} + {:d} = {:d}\n".format(a, b, result))
