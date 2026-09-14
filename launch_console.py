name = input("What's your name? ")
print("Welcome to " + name + "'s Launch Console!")

running = True
while running:
    print("1) About me")
    print("2) My goals")
    print("3) Favorite Color")
    print("4) Exit")
    choice = input("Pick 1-3: ")
    if choice == "1":
        print(f"I am {name} and I am a senior at Fordson High School. ")
    elif choice == "2":
        print("My goals are to get into the University of Michigan Ann Arbor and get a degree in mechanical or Aerospace Engineering.")
    elif choice == "3"
        print("My favorite color is green")
    elif choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("Please pick 1, 2, 3, or 4.")
