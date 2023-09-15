def jadualdarab():
    for x in range(95):
        print("*" , end="")
    print()

    print("\t\t\t\t\t\t\t\t\t\tJADUAL DARAB")

    for x in range(95):
        print("*" , end="")
    print()

    print("\t", end="")

    for i in range (1, 13):
        print(f"\t{i}\t", end="")
    print()

    for j in range (1, 13):
        print(f"{j}\t\t", end="")
        for i in range(1, 13):
            result = i * j
            print(f"{result}\t\t", end="")
        print()



if __name__ == "__main__":
    jadualdarab()
