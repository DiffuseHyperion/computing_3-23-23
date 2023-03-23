bears = int(input("Enter number of teddy bears made: "))
hours = int(input("Enter number of hours worked: "))

wage_bears = bears * 2
wage_hours = hours * 5
print("Wages: $" + str(max(wage_bears, wage_hours)))