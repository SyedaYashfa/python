# Qno#1
set1 = {1, 2, 3, 4, 5}
print("Set of unique numbers:", set1)

# Qno#2
set1.add(6)
set1.remove(3)
print("New set:", set1)

# Qno#3
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)

#Qno#4
list1 = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(list1)
print("Unique elements:", unique_set)

# Qno#5
element = 3
if element in set1:
    print("Element Exist in set that is:",element)
else:
    print("Element Not Exist in set:",element)

# Qno#6
vowels = {'a', 'e', 'i', 'o', 'u'}
if "z" in vowels:
    print("Exist")
else:
    print("Not Exist in vowels")

# Qno#7
    sample_set = {1, 2, 3}
  #  sample_set.add([4, 5]) 


# Qno# 8
set1 = {5, 3, 1, 4, 2}
list1 = sorted(set1)
print("Sorted list from set:", list1)
