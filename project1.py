print("===KIVIK ADVANCED CALCULATOR===")
print("Available Operations : + , - , * , / (Press 'q' to terminate)\n")

while True :
    operation = input("Select an operation (+ , - , * , / or q) : ")

    if operation == "q" :
        print("[SYSTEM] : Shutting Down the calculator. Have a good day, madam!")
        break

    if operation not in ["+" , "-" , "*" , "/"] :
        print("[ERROR] : Invalid operation selected. Please try again later.")
        continue

    num1 = float(input("Please enter the 1st number : "))
    num2 = float(input("Please enter the 2nd number : "))

    if operation == "+" :
        print(f"[RESULT] : {num1} + {num2} = {num1 + num2}")
    
    elif operation == "-" :
        print(f"[RESULT] : {num1} - {num2} = {num1 - num2}")

    elif operation == "*" :
        print(f"[RESULT] : {num1} * {num2} = {num1 * num2}")

    elif operation == "/" :
        if num2 == 0 :
            print(f"[CRITICAL ERROR!] : Division by zero is mathematically undefined!")

        else :
            print(f"[RESULT] : {num1} / {num2} = {num1 / num2}")

    print("-" * 45)