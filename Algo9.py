PlayerName = ["Helen", "Adam", "Lidia", "Kwaku", "Priya", "Chan"]

shift = int(input("Enter number of times to shift: "))

# must update PlayerName, cannot create new array

for i in range(shift):
    PlayerName.insert(0, PlayerName.pop())
print(PlayerName)