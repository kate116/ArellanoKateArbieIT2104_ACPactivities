
name = (input("Enter a string: "))
vowels = 'aeiouAEIOU'
found_vowels = []

for char in name:
    if char in vowels:
        found_vowels.append(char)

if found_vowels:
    print(f"{found_vowels}")
else:
    print("No vowels found in the name.")
