
# QNO#1
student = {"name": "Alice", "age": 20, "grade": "A"}
print("Grade:", student["grade"])

# QNO#2
student["school"] = "High School"
print("dictionary:", student)

#QNO#3
#update the age
student["age"] = 21
print("dictionary:", student)

# Question#4
phonebook = {"Sarah": "123-456", "Alishba": "789-012", "Yashfa": "345-678"}
if "John" in phonebook:
    print("John exist",phonebook[John])
else:
    print("Not exist")

#QNo#5

del student["grade"]
print("Dictionary:", student)

# QNo#6
list_1 = list(student.keys())
print("Keys in dictionary:", list_1)

