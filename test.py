def jadualdarab():
    print("*****************************************************************************")
    print("\t\t\t\t\t\t\t\tJADUAL DARAB")
    print("*****************************************************************************")

    for i in range(1, 11):
        print(i, end="\t\t")

    print("\n" + "-" * 90)  # Add a line of hyphens to separate horizontal and vertical sections

    for j in range(1, 11):
        for i in range(1, 11):
            print(j * i, end="\t\t")  # Use tabs to separate the multiplication results
        print()

if __name__ == "__main__":
    jadualdarab()
