# Qno#1
fruits = ["Banana", "peach", "Mango", "cherry", ]

print("Second:", fruits[1])
print("Last:", fruits[-1])

# Qno#2
fruits.insert(0, "apple")
fruits.append("apple2")
print("Updated list:", fruits)

#Qno#3
del fruits[2]
print("List :", fruits)

# Qno#4
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
print("Updated list:", numbers)

# Qno#5
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print("New list:", concatenated_list)

# Qno#6
sliced_list = numbers[1:5]
print("Sliced List:", sliced_list)
#Qno7
list_2 = [10, "Hello", 3.14]
i=int(0)
for element in list_2:
    print("Type of",list_2[i],"  is",type(list_2[i]))
    i=i+1
