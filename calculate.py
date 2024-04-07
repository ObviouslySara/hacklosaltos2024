def calculate_monthly_payment(principal, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12 / 100  
    total_payments = years * 12  

    monthly_payment = (principal * monthly_interest_rate * (1 + monthly_interest_rate)**total_payments) / ((1 + monthly_interest_rate)**total_payments - 1)

    return monthly_payment


cashflow = int(input("Money you have ready to invest:")) #have a set amount at the start anyway, like 250,000
price = int(input("Cost of house:")) #get price from the chosen one in a list
downpayment = int(input("Downpayment for house: ")) #player chooses how much they want to pay upfront
cashflow -= downpayment
principal = price - downpayment  
mortgage_plan = input("1, 2, 3") # user input, button pressed for given options
if mortgage_plan == "1":
    annual_interest_rate = 4.5  # mortgage plan
    years = 30  # mortgage plan
elif mortgage_plan == "2":
    annual_interest_rate = 5.1  # mortgage plan
    years = 20  # mortgage plan
elif mortgage_plan == "3":
    annual_interest_rate = 5.8  # mortgage plan
    years = 10  # mortgage plan
monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
print("monthly mortgage payment:", round(monthly_payment, 2))

rent = 0.01*price #use range slider here, between 0.005 and 0.013
cashflow = cashflow + rent - monthly_payment
print("Cashflow this year: " + str(cashflow))