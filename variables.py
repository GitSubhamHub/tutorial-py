#learning variables and datatypes in Python

#create and assigning varables in python
name = "subham"
bucket = "water"
age = 23
sept = 24.2025

#print output
print(name)
print(bucket)
print(age)
print(sept)

#Identify datatype and print it 
print(type(name))
print(type(bucket))
print(type(age))
print(type(sept))

#typecasting
age = 19
print(type(age))

age = str(19)
print(type(age))

age = float(19)
print(type(age))

print(age)

#assigning multiple values to multiple variables in a single line
name, bucket, age, sept = "awasthi", "water1", 22, 21.2025

print(name)
print(bucket)
print(age)
print(sept)

#printing  multiple values using single print function using(,+)

print(name, bucket, age, sept)

print(bucket + name)   #concatenation
#cannot use concatenation for two different datatypes

#naming syntax
# dont use numbers in the begining of variable (2abs)
# dont use spl characters (*abc)
# Variable are case sensitive (Subham and subham are two different variables)