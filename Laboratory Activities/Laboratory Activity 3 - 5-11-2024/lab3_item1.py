def roman_to_integer(roman):
    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    total = 0
    prev = 0

    for char in reversed(roman.upper()):
        current = roman_values[char]
        total += current if current >= prev else -current
        prev = current

    return total

romanNum = input("Enter a Roman numeral: ")
print(f"The integer value of {romanNum} is {roman_to_integer(romanNum)}")
