numToDay = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

num = int(input("Enter number: "))
if num < 7:
    print(numToDay[num])
else:
    print("Invalid number!")

