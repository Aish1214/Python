#Type casting means converting from one data type to another. There are 2 types of typecasting 
# a] Explicit typecasting b] Implicit Typecasting

# Explicit typecasting means developer does it by own. Let's understand it by an example 

string = "15"
number = 7
string_number = int(string) # throws an error if the string is not an valid integer
sum = number + string_number
print("The sum of both number is " ,sum)


#Implicit Typecasting means python language automatically changes the data type 
a = 10.9
print(type(a))

b = 8
print(type(b))

print(a + b)
#this is how int has been itself converted to float by python automatically without giving any command