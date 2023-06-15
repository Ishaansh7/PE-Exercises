#POV:Imagine you are working on an algorithmic trading platform that analyzes market trends and predicts future stock prices. As part of your research, you need to generate the Fibonacci sequence up to a given number 'n' to study the patterns and correlations in stock price movements.
print("Welcome to the Fibonacci Sequence Generator!")
n = int(input("Please enter a number 'n' to generate the Fibonacci sequence up to that number: "))
n1 = 0
n2 = 1
count = 0
print(f"Thank you for providing the number {n}.")
print(f"The Fibonacci sequence up to {n} is: ")
while count < n:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1