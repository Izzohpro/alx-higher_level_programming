#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # Print from directory sorted name
    for name in sorted(dir(hidden_4)):
        # print names that doesn't start with __
        if name[:2] != '__':
            print("{}".format(name))
