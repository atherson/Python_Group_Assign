gross_pay = int(input("What is your gross pay: "))
no_of_dependants = int(input("What is the number of dependants: "))

if gross_pay <= 10_000:
    if no_of_dependants < 3:
        tax_payable1 = gross_pay * 0
        net_pay1 = gross_pay - tax_payable1
        print("Your gross pay is: " , gross_pay)
        print("Your Number of Dependants is: ",  no_of_dependants)
        print("Your tax payable is: ",  tax_payable1)
        print("Your net pay is: ", net_pay1)
    else:
        tax_payable2 = gross_pay * 0
        net_pay2 = gross_pay - tax_payable2
        print("Your gross pay is: " , gross_pay)
        print("Your Number of Dependants is: ",  no_of_dependants)
        print("Your tax payable is: ",  tax_payable2)
        print("Your net pay is: ", net_pay2)

elif gross_pay >10000 and gross_pay <=20000:
    if no_of_dependants < 3:
        tax_payable3 = gross_pay * 0.15
        net_pay3 = gross_pay - tax_payable3
        print("Your gross pay is: " , gross_pay)
        print("Your Number of Dependants is: ",  no_of_dependants)
        print("Your tax payable is: ",  tax_payable3)
        print("Your net pay is: ", net_pay3)
    else:
        tax_payable4 = gross_pay * 0.1
        net_pay4 = gross_pay - tax_payable4
        print("Your gross pay is: " , gross_pay)
        print("Your Number of Dependants is: ",  no_of_dependants)
        print("Your tax payable is: ",  tax_payable4)
        print("Your net pay is: ", net_pay4)
else:
    if no_of_dependants < 3:
        tax_payable5 = gross_pay * 0.35
        net_pay5 = gross_pay - tax_payable5
        print("Your gross pay is: " , gross_pay)
        print("Your Number of Dependants is: ",  no_of_dependants)
        print("Your tax payable is: ",  tax_payable5)
        print("Your net pay is: ", net_pay5)
    else:
        tax_payable6 = gross_pay * 0.25
        net_pay6 = gross_pay - tax_payable6
        print("Your gross pay is: " , gross_pay)
        print("Your Number of Dependants is: ",  no_of_dependants)
        print("Your tax payable is: ",  tax_payable6)
        print("Your net pay is: ", net_pay6)



