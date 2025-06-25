def calculator():
    print("CALCULATOR")
    
#TAKING INPUTS FOR NUMBER
    num1 = float(input("Enter First Number : "))
    num2 = float(input("Entetr Second Number : "))
    
    while True:
        operation = input("Enter:-\n+ :- ADDITION\n- :- SUBTRACTION\n* :- MULTIPLICATION\n/ :- DIVIDATION\nc :- CONTINUE\ne :- EXIT\n")
#FOR ADDITION
        if operation == "+":
            soln = num1+num2
            print(num1, "+", num2 , "=", soln)
					
#FOR SUBTRACTION
        elif operation == "-":
            soln = num1-num2
            print(num1, "-", num2 , "=", soln)
					
#FOR MULTIPLICATION
        elif operation == "*":
            soln = num1*num2
            print(num1, "X", num2 , "=", soln)
					
#FOR DIVISION
        elif operation == "/":
            soln = num1/num2
            print(num1, "/", num2 , "=", soln)
					
#FOR CONTINUING THE CALCULATION
        elif operation == "c":
            num1 = soln
            num2 = float(input("Enter Next Number: "))
            operation
					
#FOR EXITING THE CALCULATION
        elif operation == "e":
            print("Closing the CALCULATION!!")
            break

        else:
            print("PLEASE ENTER + - * / c or e\nNOW RESTART")


calculator()
