#defining a math_operations functions
def math_operations(a,b):
#docstring to explain what the function does
    """this function performs addition and multiplication of two numbers that the user enters and return the sum and product
     a (float): The first number.
     b (float): The second number.
    After entering the two numbers, the function returns the sum as well as the product of the two numbers
    """
#use of lambda function to calculate the sum and product of two numbers
    add =lambda a,b:a+b
    prod=lambda a,b:a*b
    sum=add(a,b)
    prod_res=prod(a,b)
#returns the sum and product
    return sum,prod_res
#prints the docstring
print(math_operations.__doc__) 

def main():
    #the user inputs the values a and b
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
#call the math operation
    sum, prod_res = math_operations(a, b)
    #prints the returned sum and product
    print("\nThe sum is:", sum)
    print("The product is:", prod_res)
#calls the main function
main() 


