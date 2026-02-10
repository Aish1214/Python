#remember if you need to access any character within a paragraph or say a word then you need to use indexing and understand using the following example 
names = "Aishwarya, Varad"
#now you have to print only Aishwarya from these 2 words 
#why 10 because the rule is n to n-1
print(names[0:9])


#if you want to measure the length of the word or the paragraph understand by the following example
h = """Sure 😊 Here’s a short sample paragraph on a topic I like—**curiosity**:

Curiosity is the quiet engine behind almost everything we learn. It’s the reason a child keeps asking “why,” and the reason adults still pick up new skills long after school ends. When we’re curious, mistakes feel less like failures and more like clues, pushing us to explore a little deeper. Curiosity keeps life from becoming repetitive; it turns ordinary moments into opportunities to discover something new. In many ways, staying curious is a simple but powerful way to keep growing.

If you want it simpler, longer, or on a specific topic (school-level, story-style, etc.), just tell me!"""
print(len(h))

#String Slicing 
name = "Mango"
print(name[0:4])
print(name[:4])
print(name[:])
print(name[:5])

#negative Slicing 
print(name[-3:-1])
print(name[-1:-3])
print(name[-4:-2])
