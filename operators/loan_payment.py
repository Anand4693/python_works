
# loan amount

# tenure

# interest

# o/p EMI, total_interest, total_payable_amount

loan_amount = int(input("Enter the loan amount"))

tenure = int(input("Enter tenure in years"))

annual_interest = int(input("Enter interest in %"))

monthly_interest = (annual_interest / 12 ) / 100

tenure_monthly = tenure * 12


EMI = (loan_amount * monthly_interest * (1+monthly_interest)**tenure_monthly) / (1+monthly_interest)**tenure_monthly - 1

# print(monthly_interest)

print(EMI)