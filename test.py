def jadualdarab():
    for x in range(79):
        print("*", end="")
    print()

    print("\t\t\t\t\t\t\t\tJADUAL DARAB")

    for x in range(79):
        print("*", end="")
    print()

    for i in range(1, 11):
        print("\t", end="")
        for j in range(1, 11):
            result = i * j
            print(result, end="\t\t")
        print()

if __name__ == "__main__":
    jadualdarab()
