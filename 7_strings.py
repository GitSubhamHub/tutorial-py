#assigning 
name = "ramesh"
x = "this is a random string"

#multiline
x = """this is the first sentence and 
this is the second sentence"""
print(x)

#indexing and negative indexing
name = "ramesh"

#  r    a    m    e    s    h   
#  0    1    2    3    4    5   #indexing
# -6   -5   -4   -3   -2   -1   #negative indexing

print(name[2])       #this prints 2nd character of the string
print(name[-5])      #this prints -5th character of the string
print(name[2:])      #this prints from m to end of string
print(name[:2])      #this prints everything before m

#slicing
#just print ame
print(name[1:4])  #included:excluded this is the syntax

#modification (upper, lower, strip)
name = "ramesh"
print(name.upper())

name = name.upper()
print(name)

lowername = name.lower()
print(lowername)

fname = "ramesh         "
fname = fname.strip()  #this functin will simply remove all spaces before and after string 
lname = "kumar"
print(fname + " " + lname)

#replace
item = "chair"
print(item.replace("c","k"))
print(item.replace("r","oo"))

#split
message = "hi, this is ramesh, and i am a developer"
print(message.split(","))