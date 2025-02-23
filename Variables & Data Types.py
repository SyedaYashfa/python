# Question#1
x = 10
y = 20.5
z = "Hello World"

print("Type of x:", type(x))
print("Type of y:", type(y))
print("Type of z:", type(z))


# Question#2
x = 12.7
y = int(x)
z = str(x)

print("Int:", y)
print("String:", z)

# Question#3
x = '25'
y = int(x)
z = float(x)

print("Int:", y)
print("Float:", z)

#Question#4
a = 10 
b = 'Hello'  
c = 3.14  
if type(a)==int or type(a)==str or type(a)==float:
    print("Immutable")
else:
    print("Mutable")    
#types
print("TYPE of a",type(a))
print("TYPE of b",type(b))
print("TYPE of c",type(c))

# Question#5

a=int()
variables_dictionary = {
    "x": x,
    "y": y,
    "z": z,
    "a": a,
    
}

print("Dictionary of variables:", variables_dictionary)