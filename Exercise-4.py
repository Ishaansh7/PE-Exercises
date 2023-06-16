#POV:Imagine you are working on a content management system for a publishing company that handles various articles and blog posts. As part of the system, you need to develop a feature that allows users to sort a list of article titles in alphabetical order. This feature will enable content creators and editors to easily organize and manage their content library.
print("Welcome to the Article Title Sorter!")
input_string=input("Please enter a list of article titles, separated by commas: ")
title_list=input_string.split(",")
print(title_list)
sorted_list=sorted(title_list)
print("Thank you for providing the article titles.")
print("The sorted list of titles is:")
for sorted_list in title_list:
        print("-",sorted_list)