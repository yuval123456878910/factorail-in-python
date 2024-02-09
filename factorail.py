math = input()

factorailSetings = None
time = None
forQB = None

if math == "!":
    try:

        # 0 meen end in that cocolatore #

        print("in factorail in that cocolatore 0 mine end")
        factorailSetings = int(input())
        time = factorailSetings
        forQB = factorailSetings
        
    except:
        print("you need a number")

    while time > 0:
        print(forQB * (factorailSetings - 1))

        forQB =  forQB * (factorailSetings - 1)

        factorailSetings = factorailSetings - 1

        time = time - 1

    

