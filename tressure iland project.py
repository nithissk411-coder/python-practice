print("welcome to the tressure iland\nyour mission is to find the tressure")
input1= input("enter 'left' or 'right':")
if input1 == "left":
    input2 = input("you have come to a lake \nenter 'swim' or 'wait'")
    if input2 == "wait":
        input3 = input("you have crossed the lake choose a door:red,yello,blue")

        if input3 == "red":
            print("you have caught a red door")
        elif input3 == "blue":
            print("you have caught a blue door")
        elif input3 == "yello":
            print("you win")
        else:
            print("you lose")
    else:
        print("you have been attacked by a angry trout\n Game over")
else:
    print("you have fall into a hole\Game over")






