passengers = int(input("Enter no of passengers: "))
distance = int(input("Enter distance of journey: "))

cost = distance * 2 + 1
if passengers >= 5:
    cost *= 1.5
print(cost)