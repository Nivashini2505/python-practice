print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction_chose=input("You're at a cross road. Where do you want to go?Type '\"left\"'  or '\"right\"'\n" )
if(direction_chose=='left'):
    choose_next=input("You came to a lake. There is an island in the middle of the lake. Type '\"wait\"' to wait for a boat. Type '\"swim\"' to swim across\n")
    if(choose_next=='wait'):
        choose_door=input("You arrive at an island unharmed.There is a house with 3 doors.One red,one yellow and one blue.Which colour do you choose?\n")
        choose_door = choose_door.lower()
        if(choose_door=='blue'):
           print("Eaten by beasts.\nGame over!")
        elif (choose_door=="red"):
            print("Burned by fire.\nGame over!")
        elif(choose_door=='yellow'):
            print("You win!") 
        else:
            print("Game over!")          
    else:
        print("Attacked by trout.Game over")    
else:
    print("Fall into a hole.\nGame over!")                    