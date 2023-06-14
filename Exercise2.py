#POV: Imagine you are working on a text analysis tool for a language learning application. One of the essential features you need to implement is a vowel counter that helps users understand the distribution of vowels in a given sentence. This feature will assist language learners in improving their pronunciation and recognizing common vowel patterns.
print("Welcome to the Vowel Counter!")

#enter sentance here
input=input("Please enter a sentence to count the number of vowels: ")

vowels=0 #initializing 

#to traverse the string
for i in input :
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1

#to calculate percentage of vowels
percentage = vowels/len(input)*100

#display result
print("Thank you for providing the sentence.")
print(f"The number of vowels in the sentence is: {vowels} ")
print(f"The percentage of vowels in the sentence is: {percentage:.2f}%")
