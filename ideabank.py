import sys


# print(sys.argv)
list = ["pomysł 1", "pomysł 2", "pomysł 3"]


if len(sys.argv) > 1:
    param1 = sys.argv[1]
    print(sys.argv[1])
    if param1 == "--list":
        for i in list:
            print(i)