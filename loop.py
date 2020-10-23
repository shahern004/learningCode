correct = "IndyPy"
tries = 0

keepGoing = True
while(keepGoing):

    tries = tries + 1
    print ("Try #",tries)

    guess = input("What is the Password? ")
    if guess ==correct:
        print("That's correct!  here's the treasure!")
        keepGoing = False

    elif tries >=3:
        print("Too many wrong tries. launching the missiles")
        keepGoing = False
    /// testing a change