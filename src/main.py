from src.file_handler import FileHandler
from src.invalid_data_exception import InvalidDataException


def example1():
    for i in range(3):
        try:
            x = int(input("enter a number: "))
            y = int(input("enter another number: "))
            print(x, '/', y, '=', x / y)
        except ValueError:
            print("Values of x and y must be numbers.")
        except ZeroDivisionError:
            print("Value of y must not be 0.")


def example2(L):
    print("\n\nExample 2")
    sum = 0
    sumOfPairs = []
    try:
        for i in range(len(L) + 1):
            sumOfPairs.append(L[i] + L[i + 1])
        print("sumOfPairs = ", sumOfPairs)
    except IndexError:
        print("List index out of range")
    except TypeError:
        print("List must contain only numbers.")


def printUpperFile(fileName):
    try:
        file = open(fileName, "r")
    except FileNotFoundError as e:
        print(e)
    else:
        for line in file:
            print(line.upper())
        file.close()


def main():
    example1()
    L = [10, 3, 5, 6, 9, 3]
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])
    try:
        example3([10, 3, 5, 6])
    except NameError as e:
        print(e)
    printUpperFile("doesNotExistYest.txt")
    printUpperFile("./Dessssktop/misspelled.txt")
    try:
        FileHandler("", 11, 111)
    except InvalidDataException as e:
        print(e)


if __name__ == "__main__":
    main()
