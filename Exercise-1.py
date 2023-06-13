#POV:You are working on a financial application for a company that handles daily sales transactions from multiple stores.
print("Welcome to the Daily Sales Calculator!")

#input sales amount for the day
sales=input("Please enter the sales amounts for today separated by spaces:")

#split the input string into list
sales_list = sales.split()

#convert the string into integer
sales_list = [int(amount) for amount in sales_list]

#calculate total sales
total_sales = sum(sales_list)

#calculate average sales
avg_sales = total_sales/len(sales_list)

#display result
print("Thank you for providing the sales data.")
print(f"Today's total sales amount is: Rupees {total_sales}") 
print(f"The average sales per transaction is: Rupees {avg_sales:.2f}")