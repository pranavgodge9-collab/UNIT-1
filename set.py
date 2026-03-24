#creating a set

set1 = {1,2,3,4,5}
print("Original set1 is :", set1)

print(set1[2])

set2 = {4,5,6,7,8}
print("Originl set2 is :",set2)

#Union of sets 
union = set1 | set2
print("Union of sets is :", union)

#Intersection of sets 
intersection = set1 & set2
print("Intersection of sets is :", intersection)

#Difference of sets 
difference = set1 - set2
print("Difference of sets is :", difference)
