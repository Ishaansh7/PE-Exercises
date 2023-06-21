#POV:Imagine you are working on a text analysis tool for a digital marketing agency. As part of this tool, you need to develop a feature that helps content creators and marketers understand the distribution of characters within their text. This feature will assist in optimizing content, identifying keywords, and enhancing search engine optimization (SEO) strategies.
from collections import Counter
print("Welcome to the Character Counter!")
c=input("Please enter a string to count the occurrences of each character: ")
count=Counter(c)
print("Thank you for providing the string.")
print("Character count: ")
print(str(count))