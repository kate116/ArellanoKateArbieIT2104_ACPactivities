def perfectNum(i):
    if i < 1:
        return False
    
    divisorSum = sum(n for n in range(1, i) if i % n == 0)
    return divisorSum == i

userInput = input("Enter a number: ")

if userInput.isdigit():
    number = int(userInput)
    if perfectNum(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")
else:
    print("Please enter a valid integer.")