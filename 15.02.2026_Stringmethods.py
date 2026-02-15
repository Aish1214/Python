#strings are immutable
a ="Aishwarya"
print(len(a))

#Uppercase 
print(a.upper())

#lowercase 
print(a.lower())

#rstrip 
#removing trailing characters
b = "Aishwarya@@ @@@ She is cute" 
print(b.rstrip("@"))
#hence it removed the signs @ from back 

#replace
#so if you are trying to replace n number of words within the code then all words will be replaced 
#note the following example 
c ="Aish"
d= "aish"
print(c.replace("Aish", "Harish"))
print(d.replace("aish","Poonam"))

#Split
print(b.split(" "))

#Captitalize
print(d.capitalize())

#centre 
#aligning in centre 
e = "Welcome to my world"
print(e.center(55))
#we need to mention the number or quantity of spacing according to which the alignment is done 

#Count
#how many times a speciifc character has occured within one sentence or variable 
v = "Aishwarya Sandeep Funaguskar"
print(v.count("a"))

#endswith 
print(v.endswith("a"))
print(v.endswith("r"))

#finding if the string endswith index values 
print(a.endswith("a", 0, 9))


#find
print(v.find("Sandeep"))

#both index and find values throwing an exception error 
print(v.find("z"))

print(v.index("is"))

#isalnum describes if the string is alphanumeric or not a-z, A-Z
n = "AishwaryaSandeepFunaguskar"
print(n.isalnum())

#isalpha - similar to isalnum
print(n.isalpha())

#islower
print(v.islower())
j ="varad"
print(j.islower())

#isprintable
print(v.isprintable())

#isspaces
d = "       "
print(d.isspace())

#istitled
print(v.istitle())

#isupper 
print(v.isupper())

#startswith
print(v.startswith("Aishwarya"))

#swapcase
h = "HARISH"
i = "tuntun"
print(h.swapcase())
print(i.swapcase())

#title
print(i.title())