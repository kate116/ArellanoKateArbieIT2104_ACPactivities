k, e = input("Enter two space-seperated characters: ").split()

asciik = ord(k)
asciie = ord(e)

greater_value = max(k,e)

print("-----------------------------------")
print(f"The character with greater value is: {greater_value}")
print("-----------------------------------")

print("Showing ASCII Values")
print(f"{k}:{asciik}")
print(f"{e}:{asciie}")

