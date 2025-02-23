
#Question#1
cities = ("New York", "London", "Paris", "Tokyo", "Sydney")
print("First city:", cities[0])
print("Last city:", cities[-1])

# Question#2.
#cities[1] = "Berlin" 


#Question#3
numbers = (10, 20, 30, 40, 50)
#convert tuple into list
list1 = list(numbers)
list1[2] = 35  
numbers = tuple(list1)
print("tuple:", numbers)

#Question#4
colors = ("red", "blue", "green", "purple")
if "purple" in colors:
    print("Purple exist")
    
#Question#5
name, age, profession = ('Alice', 25, 'Doctor')
print("Name:", name)
print("Age:", age)
print("Profession:", profession)

# Question#7
numbers1 = (1, 5, 2, 5, 3, 5, 4, 5)
count = numbers1.count(5)
print("Occurrences of 5:", count)
