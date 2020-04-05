def build_pyramid():
    s = 9
    for i in range(1, 10, 2):
        print(" " * s + i * "*")
        s = s - 1


build_pyramid()
