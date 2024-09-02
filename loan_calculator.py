'''
Write a simple Python function to calculate the projected monthly balance on a loan of value W, at interest rate X taken out for Y months with a monthly payment of Z.

The function should display the interest charged and the remaining balance each month, for
the duration of the loan.
'''

def calculate_loan(W,X,Y,Z):

    loan_value = W
    months = Y
    payment_monthly = Z
    annual_interest_rate = X/100
    monthly_interest = annual_interest_rate/12

    for month in range(months):
        
        interest_charged = monthly_interest * loan_value

        # Check whether a final payment can be made to settle the balance
        if payment_monthly >= loan_value + interest_charged: 
            loan_value = 0
            display_balance(month, interest_charged,loan_value)
            break
        
        loan_value = loan_value + interest_charged - payment_monthly

        display_balance(month, interest_charged,loan_value)

def display_balance(month, interest_charged,loan_value):
    print(f"-- Month {month + 1} --")
    print(f"Interest Charged: £{interest_charged:.2f}")
    print(f"Total Remaining Balance: £{loan_value:.2f}")
    if loan_value==0:
        print(f"Loan Fully Paid in Month {month + 1}")

def main():
    # Retrieve inputs from the command line
    W = float(input("Please enter the Total Loan Amount: £"))
    X = float(input("Please enter the Interest Rate: "))
    Y = int(input("Please enter the Loan Term in months: "))
    Z = float(input("Please enter the Monthly Payment Amount: £"))

    calculate_loan(W, X, Y, Z)

if __name__ == "__main__":
    main()