#  Numan Salahuddin, nsalahu@uwo.ca
# Student Number: 251264939


print("Welcome to my PC shop!")  # First we print out a welcoming.

# We then create lists for each variable.

SSD = [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]]
HDD = [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
CPU = [['1', 'Intel Core i7-11700K', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]]
MOTHERBOARD = [['1', 'MSI B550-A PRO', 197.46], ['2', 'MSI Z490-A PRO', 262.30]]
RAM = [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
GRAPHICS_CARD = [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]
PSU = [['1', 'Corsair RM750', 164.99]]
CASE = [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]
PREBUILTS = [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99], ['2', 'SkyTech Prism II Gaming PC', 2839.99],
             ['3', 'ASUS ROG Strix G10CE Gaming PC', 1099.99]]

# Declaring a global variable called final.
global final
final = []


# Creating function called pickItems(), Also the heart of the program.
def pickItems():
    # Creating a user-input system for ordering PCs, collects user inputs and prints the order.
    # Looping for the 1st choice.
    choice1 = 0
    while choice1 != 3:
        total = 0
        choice1 = int(input(
            "Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout(3)? "))
        print()
        # Conditions for 1st choice.
        if choice1 == 1:
            print("Great! Let's start building your PC!")
            print()
        # First choice will print pick a CPU.
            print("First, let's pick a CPU.")
            for i in CPU:
                print(i[0], ":", i[1] + ",", i[2])
        # Second Step pick any part you want from option 1 or 2.
            choice2 = ""
            while choice2 not in ('1', '2'):
                choice2 = input("Choose the number that corresponds with the part you want: ")
            for i in CPU:
                if choice2 == i[0]:
                    total += i[2]
                    print()
        # Second choice will print a statement to pick a motherboard. with conditions applied to choose from 1 or 2.
            print("Next, let's pick a compatible motherboard.")
            if choice2 == '2':
                temp = MOTHERBOARD[0]
                print(temp[0], ":", temp[1] + ",", temp[2])
            else:
                temp = MOTHERBOARD[1]
                print(temp[0], ":", temp[1] + ",", temp[2])
        # Third choice will print a statement to pick the part you want, with conditions applied to choose from 1 or 2.
            choice3 = ""

            while choice3 != ('1' if choice2 == '2' else '2'):
                choice3 = input("Choose the number that corresponds with the part you want: ")

            if choice3 == temp[0]:
                total += temp[2]
                print()
        # Printing to pick your RAM
            print("Next, let's pick your RAM.")
            for i in RAM:
                print(i[0], ":", i[1] + ",", i[2])
        # Fourth choice will print a statement to pick your RAM part, with conditions applied to choose from 1 or 2.
            choice4 = ""
            while choice4 not in ['1', '2']:
                choice4 = input("Choose the number that corresponds with the part you want: ")

            for i in RAM:
                if choice4 == i[0]:
                    total += i[2]
                    print()
        # Print statement to pick your PSU.
            print("Next, let's pick your PSU.")
            for i in PSU:
                print(i[0], ":", i[1] + ",", i[2])
        # Fifth choice will input asking you which part you want, with conditions applied to choose from either 1 or 2.
            choice5 = ""
            while choice5 != "1":
                choice5 = input("Choose the number that corresponds with the part you want: ")

            for i in PSU:
                if choice5 == i[0]:
                    total += i[2]
                    print()
        # Print statement choosing your PC case.
            print("Next, let's pick your case.")
            for i in CASE:
                print(i[0], ":", i[1] + ",", i[2])
        # Sixth choice will input a statement asking you to pick the part you want, with conditions applied to pick from option 1 or 2.
            choice6 = ""
            while choice6 not in ['1', '2']:
                choice6 = input("Choose the number that corresponds with the part you want: ")

            for i in CASE:
                if choice6 == i[0]:
                    total += i[2]
                    print()
        # Print Statement displaying to pick an HDD or SSD storage device.
            print("Next, let's pick an HDD (optional, but you must have atleast one SSD or HDD).")
            for i in SSD:
                print(i[0], ":", i[1] + ",", i[2])
        # Seventh choice will print a statement to pick your own storage with conditions applied to choose from 1, 2 or 3.
            # You can choose X, x as well to remove SSD.
            choice7 = ""
            while choice7 not in ('1', '2', '3', 'x', 'X'):
                choice7 = input("Choose the number that corresponds with the part you want (or X not to get an SSD): ")
            if choice7.lower() == "x":
                no_ssd = True
            else:
                no_ssd = False
                for i in SSD:
                    if choice7 == i[0]:
                        total += i[2]
                        print()
        # Same case as the 7th choice.
            print("Next, let's pick an HDD (optional, but you must have at least one SSD or HDD).")
            for i in HDD:
                print(i[0], ":", i[1] + ",", i[2])
        # Eight choice would show without the SSD, choose from 1 or 2 with conditions applied.

            choice8 = input("Choose the number that corresponds with the part you want: ")
            if no_ssd == True:
                while choice8 not in ('1', '2'):
                    choice8 = input("Choose the number that corresponds with the part you want (since you did not get an SSD, you must get an HDD): ")

            else:
                while choice8 not in ('1', '2', 'x', 'X'):
                    choice8 = input("Choose the number that corresponds with the part you want: ")
            if choice8.lower() != "x":
                for i in HDD:
                    if choice8 == i[0]:
                        total += i[2]
                        print()
            # Print statement pick your graphics card. if X or x is input then you won't get the graphics card.
            print("Finally, let's pick your graphics card (or X to not get a graphics card).")
            for i in GRAPHICS_CARD:
                print(i[0], ":", i[1] + ",", i[2])
        # Ninth Choice, choosing your graphics card part. Only 1 option or You can reject the option with x.
            choice9 = ""
            while choice9 not in ('X', 'x', '1'):
                choice9 = input("Choose the number that corresponds with the part you want: ")
            if choice9.lower() != "x":
                for i in GRAPHICS_CARD:
                    if choice9 == i[0]:
                        total += i[2]
                        print()
        # Goes to the final part of the order printing you have selected all parts with total cost shown.
            print("You have selected all your required parts! Your total for this PC is  ${:0.2f}".format(total))
            final.append(total)
        # You get pre-built PC options to choose from. No questions asked.
        elif choice1 == 2:
            print("Great! Let's pick a pre-built PC!")
            print()

            print("Which pre-built PC would you like to order?")  # choosing pre-built PC from 3 options in the list.
            for i in PREBUILTS:
                print(i[0], ":", i[1] + ",", i[2])  # Choosing from list, 0 being the first option(element of the list), 1 and 2.

            choice10 = ""
            while choice10 not in ('1', '2', '3'):
                choice10 = input("Choose the number that corresponds with the part you want: ")

            for i in PREBUILTS:
                if choice10 == i[0]:
                    total += i[2]
                    print()
        # printing the cost of Pre-built PC after checking out.
            print("Your total price for this prebuilt is $" + str(total))
            final.append(total)
        else:
            pass

# Returning the function
pickItems()
print(final)  # Printing final list of prices.