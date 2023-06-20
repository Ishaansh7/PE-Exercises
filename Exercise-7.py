#POV:Imagine you are working on a data analysis tool for a scientific research institute. As part of the tool, you need to develop a feature that helps researchers quickly identify the range of values in a given dataset. This feature will enable scientists to understand the minimum and maximum values within their data, facilitating further analysis and insights.
print("Welcome to the Range Finder!")
input_value=input("Please enter a list of integers, separated by commas: ")
value_list=[]
for num in input_value.split(','):
        value = int(num)
        value_list.append(value)
a=max(value_list)
b=min(value_list)
print("Thankyou for providing list of integers.")
print("The largest number in the list is: ",a)
print("The smallest number in the list is: ",b)