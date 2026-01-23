#Variables with numbers don't need quotes
x = 7
y = 5
print(x + y)

#Adding quotes in print statement will just pass your variables as strings and won't work
t = 4
u = 1
print("t + u")

#Stings need quotes
q = "Ryan"
print(q)

# You can't use + when variables are a string and number, ERROR!
w = 5
r = "Ryan"
#print(w + r)
print(str(w) + r) #use str to redefine the integer variable as a string

# To change a number string into an integer using int
a = "5"
s = 7
print(int(a) + s)
