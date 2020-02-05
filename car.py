command = ""
start = False
stop = False
while True:
    command = input("> ").lower()
    if command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif command == "start":
        if start:
            print("The car is already started")
        else:
            print("Car started...Ready to go!")
            start = True
            stop = False
    elif command == "stop":
        if stop:
            print("The car is already stopped")
        else:
            print("Car stopped")
            stop = True
            start = False
    elif command == "quit":
        break
    else:
        print("I don't understand that...")