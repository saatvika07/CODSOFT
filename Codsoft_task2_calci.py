print("***Calculator***")
print("\nSelect operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while(1):
    choice = int(input("\nEnter your choice: "))
    if (choice in [1, 2, 3, 4]):
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            print(num1,"+",num2,"=",num1+num2)
        elif choice == 2:
            print(num1,"-",num2,"=",num1-num2)
        elif choice == 3:
            print(num1,"*",num2,"=",num1*num2)
        elif choice == 4:
            print(num1,"/",num2,"=",num1/num2)
        next_calculation = input("Do you want to continue? (yes/no): ")
        if next_calculation == "no":
              break
    else:
        print("Invalid Input")

