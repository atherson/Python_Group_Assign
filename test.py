log_in = input("Kindly enter your ID Number: ")
log_in = int(log_in)

if log_in == 2435:
    set_rounds = int(input("Enter the maximum number of rounds one shoud have: "))
    while True:
        try:
            rounds = int(input("Enter the number of rounds: "))
            if 1<= rounds <= set_rounds:
                break
            else:
                print(f"The number should be less than or equal to", set_rounds )
        except ValueError:
            print("Invalid Input!")
else:
    set_rounds = 5
    print("5 is the default number of rounds".upper())
    while True:
        try:
            rounds = int(input("Enter the number of rounds: "))
            if 1<= rounds <= set_rounds:
                break
            else:
                print(f"The number should be less than or equal to", set_rounds )
        except ValueError:
            print("Invalid Input!")      
