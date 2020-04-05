def is_parsable(x):
    if x.isdigit():
        print("WIN")
        return True
    else:
        print("LOOSE")
        return False


is_parsable(input("user Input : "))
