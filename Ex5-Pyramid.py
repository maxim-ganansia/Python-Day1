# def build_pyramid():
#    s = 9
#    for i in range(1, 10, 2):
#        print(" " * s + i * "*")
#        s = s - 1


# build_pyramid()


def build_pyramid():
    for i in range(rows):
        print(" "*(rows - i - 1) + "*" * (2 * i + 1))


rows = 5
build_pyramid()
