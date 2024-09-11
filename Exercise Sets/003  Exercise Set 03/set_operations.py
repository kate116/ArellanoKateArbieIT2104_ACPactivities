set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

print("Answers for Set Difference:")
difference_set1 = set1.difference(set2)
print(difference_set1)
difference_set2 = set2.difference(set1)
print(difference_set2)

print("\nAnswer for Union of Sets:")
union1 = set1.union(set2)
print(union1)

print("\nAnswer for Symmetric Difference:")
symdif1 = set1.symmetric_difference(set2)
print(symdif1)


print("\nAnswers for Set Intersection:")
intersect = set1.intersection(set2)
print(intersect)


