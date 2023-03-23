age = int(input("Age of the dog in years: "))
if age <= 2:
    human = age * 12
    print("human equlvalent: " + str(human))
else:
    human = 24 + ((age - 2) * 6)
    print("human equlvalent: " + str(human))