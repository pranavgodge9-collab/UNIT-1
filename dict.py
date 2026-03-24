#creting a dictionary
dict = {"name":"pranav","age":19,"city":"pune"}
print("Original dictionary is :",dict)

print(dict["name"])
print(dict["city"])

dict["age"]=18
print(dict)

del dict["city"]
print(dict)

merged_dict = dict | {"city":"Pune"}
print(merged_dict)