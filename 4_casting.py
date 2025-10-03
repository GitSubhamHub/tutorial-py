x = "1"   #string
y = 55    #int
z = 24.01   #float
c = 26j #complex

# print(type(x))
# print(type(y))
# print(type(z))

#in certain situations we need python to consider a value in different datatype

#define integer to float/string by using construct function
y = float(55)
# print(type(y))

y = str(55)
# print(type(y))

y = complex(55)
# print(y)
# print(type(y))

#define float to integer/string
z = 24.01
z = int(24.01)
# print(z)
# print(type(z))

z = str(24.01)
# print(z)
# print(type(z))

z = complex(24.01)
# print(z)
# print(type(z))

#you cannot change from complex to other datatype
#you cannot change from text/alphabetic datatypes to int/float

# name = "ramesh"
# print(type(name))
# # name = int("ramesh")
