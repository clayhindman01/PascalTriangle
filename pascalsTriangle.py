#Takes n from user input and returns the nth row of Pascals Triangle

#Driver Method
def main():
    #Validates the input to make sure its an integer
    try:
        n = int(input("Enter a positive integer: "))
    except:
        main()

    #Checks that the number isn't negative
    try:
        if n < 0:
            main()
        else:
            n += 1
            nth_row = get_pascal_row(n)
            print(*nth_row, sep=" ")
    except:
        main()

#Calculates the nth row of Pascal's Triangle using recursion
def get_pascal_row(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        newRow = [1]
        previousRow = get_pascal_row(n - 1)
        for i in range(len(previousRow) - 1):
            newRow.append(previousRow[i] + previousRow[i + 1])
        newRow += [1]
    return newRow

main()