#creating a python list
list1 = [0,"Ruth","Isah","Hasifah"]
print(list1)

#creating a python dictionary
dic1 = {"Name":"Olul Shawal","Located":"Tororo","Telephone":"0751545956"}
print(f"He comes from {dic1['Located']}!")

list1.append("Olul")
print(list1)

list2 = ["apple","orange","mango"]
print(list2)

list2.append("banana")
print(list2)

#creating a python set
my_set = {"apple","banana","orange"}
print(my_set)

#adding an item to a set
my_set.add("grape")
print(my_set)

#removing an item from a set
my_set.remove("banana")
print(my_set)

#concatnating two sets
set1 = {"apple", "banana"}
set2 = {"orange", "grape"}
set3 = set1.union(set2)
print(set3)