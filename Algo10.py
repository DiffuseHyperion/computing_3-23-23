import time

display = "" # idk what question wants me to do with the message but ok

message = input("Enter message: ")
flashes = int(input("Enter flashes: "))
if (len(message) > 20):
    print("You cannot have a message longer than 20 characters!")
    quit() # man too used to return; in java :((((

for i in range(flashes): # would have done async thread but lazy
    display = message
    print(display)
    time.sleep(1)
    display = ""
    print(display)
    time.sleep(1)

