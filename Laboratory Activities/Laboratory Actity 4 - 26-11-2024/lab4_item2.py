try:
    size = int(input("Enter the size of the array: "))
    arr = [0.0] * size

    print("Enter the elements of the array: ")
    for i in range(size):
        arr[i] = float(input())

    n = int(input("Enter the index of the element to print: "))
    print(f"Element at index {n}: {arr[n]:.2f}")

except IndexError:
    print(f"Index {n} is invalid.")
except ValueError:
    print("Invalid input. Please enter numeric values.")
