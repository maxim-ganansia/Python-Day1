def build_pyramid():
    for i in range(rows):
        print(" "*(rows - i - 1) + "*" * (2 * i + 1))


rows = 5
build_pyramid()
