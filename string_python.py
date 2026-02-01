#All about the strings in python 
name = "Aishwarya" 
friend = "Varad"
print("Hey, " +name)

#to print the sentence using the comma 
print('He said, \"I want to eat an apple.\"')

#Using the double quote and single quote for the multiline string
st = """  

Sure 😊
Here’s a short sample paragraph on a topic I like—**curiosity**:

Curiosity is the quiet engine behind almost everything we learn. It’s the reason a child keeps asking “why,” and the reason adults still pick up new skills long after school ends. When we’re curious, mistakes feel less like failures and more like clues, pushing us to explore a little deeper. Curiosity keeps life from becoming repetitive; it turns ordinary moments into opportunities to discover something new. In many ways, staying curious is a simple but powerful way to keep growing.

If you want it simpler, longer, or on a specific topic (school-level, story-style, etc.), just tell me!

"""
print(st)

#Indexing. Hence the string is the array of the characters and also we can directly access the parts of the string
# H = 0 // a = 1 // r = 2
h = "Harish"
print(h[2])

#looping in the string 
for character in h:
    print(character)