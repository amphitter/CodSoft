def main():
    print(" ____Calculator____")
    print("Choose operation")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    
    choice = int(input("Enter the choice: "))
    
    if choice in [1, 2, 3, 4]:  # Corrected the range of choices
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:  # Changed comparisons to integers
            ans = num1 + num2
            operation = "addition"
        elif choice == 2:
            ans = num1 - num2
            operation = "subtraction"
        elif choice == 3:
            ans = num1 * num2
            operation = "multiplication"
        elif choice == 4:
            if num2 == 0:
                print("Error! Division by Zero")
            else:
                ans = num1 / num2
                operation = "division"
            
        print(f"The result of the {operation} is : {ans}")
    
    else:
        print("Invalid input")
            
if __name__ == "__main__":
    main()
