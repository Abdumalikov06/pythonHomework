def invest(amount, rate, years):
    initial=1
    while initial<=years:
        amount=amount+amount*rate
        print(f"year{initial}: {amount:.2f}")
        initial+=1
i_amount=int(input("enter the principal amount: "))
i_rate=float(input("Enter the annual rate of return: "))
i_years=int(input("Enter the number of years to calculate: "))
invest(i_amount,i_rate,i_years)




