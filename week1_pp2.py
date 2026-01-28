#Syntaxes
print("Hello world")
print("Hi")
print(3)
print(3 + 789)
print("I am", 17, "years old")

#1
if 5 > 2:
    print("Five is greater than two")
#2
word = "jkfsl"
if word.isdigit():
    print("True")
else:
    print("False")
#3
age = int(input())
if age >= 18:
    print("You are adult")
else:
    print("You are underage")
#4 
if True:
    print("Always true")
#5 
if 11 + 9 < 21:
    print("False")

#Variables

#1
Var1 = 15

#2
Var2 = "Neo"

#3 
Var3 = 13 + 2

#4
boolVar = True #boolean variable

#5
Var4 = str(3) #Var4 will be '3'
Var5 = int(3) #Var5 will be 3
Var6 = float(3) #Var6 will be 3.0

#type of variables
Var7 = 5
Var8 = "jlkjk"
print(type(Var7)) #int
print(type(Var8)) #str

#Rules for Python variables:

#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#A variable name cannot be any of the Python keywords.


#Many values to multiple variables
Var9, Var10, Var11 = "Black", "White", "Green"
print(Var9) #Black
print(Var10) #White
print(Var11) #Green

#One value to Multiple Variables
Var12 = Var13 = Var14 = "Gold"



#Unpack a collection
fruits = ["apple", "banana", "cherry"]
Var15, Var16, Var17 = fruits
#Var15 = apple Var16 = banana Var17 = cherry

#Output Variables
Var18 = "My name is..."
print(Var18) #Output: My name is...

Var19 = "My", Var20 = "name", Var21 = "is..."
print(Var19, Var20, Var21) #Output: My name is...

print(Var19 + Var20 + Var21) #Output: Mynameis...

#Global Variables 
Var22 = input() #Global variable

def call():
    print(f"My name is {Var22}")

call()


def call2():
    Var22 = "Daryn" #Local value
    print(f"My name is {Var22}") #My name is Daryn

print(f"My name is {Var22}") #Entered name

Var23 = "Big"

def call3():
    global Var23
    Var23 = "Small"

call3()
print(f"The shelf is a {Var23}")

#Specify a Variable Type

x = int(1) # x will be 1
y = int(7.3) # x will be 7
z = int("3") # x will be 3

x1 = float(1) # x1 will be 1.0
y1 = float(7.3) #y1 will be 7.3
z1 = float("4") #z1 will be 4.0

x2 = str(1) # x2 will "1"
y2 = str(7.2) # y2 will be "7.2"

#Strings
string = """fwewkmklj   
wfewfwfjfwjijewfjqdqd"""
#Multiline string (same with ''')
print(string)

word2 = "Hello World"
print(word2[0]) #First one
print(word2[1]) #e
print(word2[::-1]) #inverse
print(word2[-1]) #last one

#Looping through a string
for i in word2:
    print(i)
"""
H
e
l
l
o
 
W
o
r
d
"""

#len() function Shows length of variable
length = len(word2)
print(length) #Output: 11

#Check String
print("wold" in word2) #Output: True


