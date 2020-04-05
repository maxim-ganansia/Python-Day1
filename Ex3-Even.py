def is_even(number):
    if number % 2 == 0:
        print("True")
        return True
    else:
        print("False")
        return False


while True:
    try:
        number = int(input("Please enter a number : "))
        is_even(number)
        break
    except ValueError:
        print("Sorry this is not an integer !!! ByeBye")
        exit()
