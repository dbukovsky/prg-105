def main():
    bottles = 99
    while bottles > 0:
        if bottles == 1:
            print(str(bottles) + " of beer on the wall")
            print(str(bottles) + " of beer")
            print("If one of those bottles should happen to fall")
        else:
            print(str(bottles) + " of beer on the wall")
            print(str(bottles) + " of beer")
            print("If one of those bottles should happen to fall")
        bottles -= 1
        if bottles == 1:
            print(str(bottles) + " bottle of beer on the wall\n")
        else:
            print(str(bottles) + " bottles of beer on the wall\n")

            print("No bottles of beer on the wall. ")


main()
