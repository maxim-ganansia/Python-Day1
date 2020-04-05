def is_parsable(x):
    if x.isdigit():
        return True
    else:
        return False


def build_pyramid_with_height_direction(input, direction):
    if is_parsable(input) and int(input) > 0:
        rows = int(input)
        if direction.lower() == "up":
            for i in range(rows):
                print(" " * (rows - i - 1) + "*" * (2 * i + 1))
        elif direction.lower() == "down":
            for i in reversed(range(rows)):
                print(" " * (rows - i - 1) + "*" * (2 * i + 1))
    else:
        print("Please enter a integer greater than 0")
        exit()


rows = input("Please enter the height of our pyramid : ")
direction = input('please enter a direction of our pyramid : up or down : ')
build_pyramid_with_height_direction(rows, direction)
