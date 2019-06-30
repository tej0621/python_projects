import random
import sys
import copy
from colorama import Fore

from root.character_maker import Player

screen_width = 100

# Display title screen and give options ###
 
#############
# FUNCTIONS #
#############

###### Title screen ######
global error
error = False
print(
    Fore.RED + "     ***** *    **   ***                         ***         **                    ***** **            ***** *    **   ***                           *   ")
print(
    Fore.RED + "  ******  *  *****    ***                         ***         **                ******  **** *      ******  *  *****    ***     *     *            **     ")
print(
    Fore.RED + " **   *  *     *****   ***                         **         **               **   *  *  ***      **   *  *     *****   ***   ***   **            **     ")
print(Fore.RED + "*    *  **     * **      **                        **         **              *    *  *    *      *    *  **     * **      **   *    **            **     ")
print(
    Fore.RED + "    *  ***     *         **    ****   ***  ****    **         **         ****     *  *                *  ***     *         **      ********        **                ***  ****   ")
print(
    Fore.RED + "   **   **     *         **   * ***  * **** **** * **     *** **        * ***  * ** **               **   **     *         ** *** ******** ****    **  ***      ***   **** **** *")
print(
    Fore.RED + "   **   **     *         **  *   ****   **   ****  **    *********     *   ****  ** **               **   **     *         **  ***   **   * ***  * ** * ***    * ***   **   **** ")
print(
    Fore.RED + "   **   **     *         ** **    **    **         **   **   ****     **    **   ** ******           **   **     *         **   **   **  *   ****  ***   ***  *   ***  **  ")
print(
    Fore.RED + "   **   **     *         ** **    **    **         **   **    **      **    **   ** *****            **   **     *         **   **   ** **         **     ** **    *** **    ")
print(
    Fore.RED + "   **   **     *         ** **    **    **         **   **    **      **    **   ** **               **   **     *         **   **   ** **         **     ** ********  **   ")
print(
    Fore.RED + "    **  **     *         ** **    **    **         **   **    **      **    **   *  **                **  **     *         **   **   ** **         **     ** *******   **   ")
print(
    Fore.RED + "     ** *      *         *  **    **    **         **   **    **      **    **      *                  ** *      *         *    **   ** **         **     ** **        **   ")
print(
    Fore.RED + "      ***      ***      *    ******     ***        **   **    **       ******   *****                   ***      ***      *     **   ** ***     *  **     ** ****    * ***  ")
print(
    Fore.RED + "      ******** ********      ****       ***       *** * *****          ****   *  *****                  ******** ********      *** * ** *******   **     **  *******   ***   ")
print(
    Fore.RED + "         ****     ****                              ***   ***                 *    ***                     ****     ****         ***      *****     **    **   *****     ")
print(
    Fore.RED + "                                                                              *                                                                           *           ")
print(
    Fore.RED + "                                                                               **                                                                        *        ")
print(
    Fore.RED + "                                                                                                                                                        *      ")
print(
    Fore.RED + "                                                                                                                                                       *      ")
blank = input("###    PRESS ENTER TO CONTINUE    ###")

global player
global p
global witch_1
global witch_2

global die
global hit


def title_screen_selection():
    op = input(">>")
    if op.lower() == "play":
        start_game()
    elif op.lower() == "help":
        help_menu()
    elif op.lower() == "quit":
        sys.exit()
    while op.lower() not in ["play", "help", "quit"]:
        print("please enter a valid command")
        op = input(">>")
        if op.lower() == "play":
            start_game()
        elif op.lower() == "help":
            help_menu()
        elif op.lower() == "quit":
            sys.exit()


def title_screen():
    print("############ WELCOME TO THE WORLD OF WITCHER ###########")
    print("########################################################")  # tobe filled
    print("                        -PLAY-                          ")
    print("                        -HELP-                          ")
    print("                        -QUIT-                          ")
    title_screen_selection()


def help_menu(): 
    print("######################################")
    print("######### WELCOME TO HELP ############")
    print("######################################")
    print(" HEY YOU DIDN'T WRITE ANY INSTRUCTIONS")  # MORE INSTRUCTIONS TO BE FILLED


#####player setup######


def start_game():
    global flag
    flag = False  # The variable flag is used to avoid error inputs
    while flag is False:  # Initially flag is set to false a while loop is executed until flag is set to true
        print("")
        print("        LET THE GAME BEGIN          ")
        print("        1) (C)reate player          ")
        print("        0) (Q)uit                           ")
        print("Type 1 for first option and 0 for second option")
        op = input("What would you like to do? >>")
        if op in ("C", "c", "1"):
            flag = True                     # In case of proper execution of statements flag is set to true
            create_player()

        elif op in ("quit", "0"):
            quit()

        else:              # In case of error an error message is displayed and loop is executed again for proper input
            print("you made an error along the way so start over all characters")


p = 0
player = []


def create_player():
    global single_player
    global multi_player
    global num_players
    global flag
    flag = False
    while flag is False:
        num_players = input("how many players you like to create ? minimum 1 to maximum 4 >")
        if int(num_players) in range(1, 5):
            flag = True
        else:
            print("invalid input give something between 1 and 4")
            flag = False
        if num_players == "1":
            single_player = True
            multi_player = False
        else:
            multi_player = True
            single_player = False
    flag = False
    p = 0
    while flag is False:
        while p < int(num_players):
            player.append(Player(input("please enter your name >"), input("please enter your gender\nmale\nfemale \n>")))
            print("     Choose your Race     Choose your profession ")
            print("        1)  Human            1)  Swordsmen ")
            print("        2)  Elf              2)  Archer")
            print("        3)  Beastman         3)  Mage  ")
            print("        4)  Undead           4)  Rogue ")
            player[p].stats_gen(input("please enter your race >"), input("please enter your profession >"))

            print(f" Your character stats \n NAME : {player[p].player_name} \n Gender : {player[p].G}")
            print(f' Race : {player[p].R}  Profession : {player[p].P}')
            print(f' Attack : {player[p].S} Health : {player[p].H} ')
            print(f"Agility : {player[p].D} Intelligence : {player[p].W}")
            print(f" Skills : {player[p].skill} Status effects : {player[p].status_effect}")
            if error is False:
                flag = True
                p += 1
            elif error is True:
                print(f"you made an error while entering inputs for player{p}\n now reenter the  for")

        print("  story intro  ")  # place holder
        print("Now players introduce your character")
        print("For better experience give your character a back story and personality and physical likeness")
        print("set the scene")  # place holder

        print("what will you do?")

        act_1()


def status():
    global flag
    flag = False
    while flag is False:
        pl = int(input("player >"))
        if pl in range(0, 5):
            print(f" Your character stats \n NAME : {player[pl].player_name} \n Gender : {player[pl].G}")
            print(f' Race : {player[pl].R}  Profession : {player[pl].P}')
            print(f' Attack : {player[pl].S} Health : {player[pl].H} ')
            print(f"Agility : {player[pl].D} Intelligence : {player[pl].W}")
            print(f" Skills : {player[pl].skill}")
            flag = True
        else:
            print("error type a number of the player you want see")


def act_1():
    global flag
    flag = False
    global choose
    global met_her
    print("a)Knock the door \nb)Peek through the window \nc)run a perception check\nd)Ignore the house walk into the forest\n")
    while flag is False:
        choose = input("NOTE: IF You run a perception check you roll a 20 die based on your wisdom and your roll you notice every thing to nothing \nchoose your option and type it as a b c or d")
        while choose in ("a", "b", "c", "d"):
            global path_1
            if choose == "a":
                flag = True
                print("You chose to knock the door")
                print(" conversation")  # place holder
                met_her = True
                choose = input("e)No its not safe for you out there we'll find our way\nf)Lead the way lady")
                if choose == "e":
                    path_1 = False
                    act_2()
                elif choose == "f":
                    path_1 = True
                    act_2()
            elif choose == "b":
                flag = True
                print("You chose to peek through the window")
                print("what you see through the window")
                choose = input("a)Knock the door \nb)Peek through the window \nc)run a perception check\nd)Ignore the house walk into the forest")
            elif choose == "c":
                flag = True
                print("You chose to do a perception check")
                global blank
                blank = input("## PRESS ENTER TO ROLL THE DICE ##")
                die = random.randint(1, 20)
                print("you rolled >", die)
                if die in range(1, 6):
                    print("what your perception reviles ")
                    print("what you see through the window")
                elif die in range(6, 11):
                    print("what your perception reviles ")
                    print("what you see through the window")
                elif die in range(11, 16):
                    print("what your perception reviles ")
                    print("what you see through the window")
                elif die in range(16, 21):
                    print("what your perception reviles ")
                    print("what you see through the window")
                else:
                    flag = False
                    print("some thing went wrong during die roll quitting ,Take a look at code in act 1 line 180")
                choose = input("a)Knock the door\nd)Ignore the house walk into the forest")
            elif choose == "d":
                flag = True
                path_1 = False
                act_2()
        if choose not in ("a", "b", "c", "d"):
            print("error enter a valid input")


def attack():
    global flag
    global die
    global hit
    global ap
    flag = False
    while flag is False:
        die = random.randint(1, 6)
        ap = int(attacker.S) + int(die)
        if ap < int(target.A):
            hit = False
        elif ap > int(target.A):
            hit = True
            target.H = int(target.H) - ap
            if target.H <= 0:
                target.staus[0] = "dead"
                print(f"{target.name} is dead")
        flag = True


def act_2():
    global target
    global attacker
    global wraith
    global wraith_1
    global wraith_2
    global wraith_3
    global dex
    global markp
    global markw
    global pd
    pd = 0
    global md
    md = 0
    wraith_1 = Player("wraith_1", "female")
    wraith_1.stats_gen("undead", "wraith")
    global die
    if single_player is True:
        if path_1 is True:
            print("scene2.1 attack of wraiths")
        if path_1 is False:
            print("reach the alter")
            if met_her is True:
                print("That Bitch")
                print("Close its Witch")
            else:
                pass
            print("scene2.2 attack of wraiths")
        print("do a dexterity roll")
        input("Press Enter to roll the die")
        die = random.randint(1, 6)
        if int(player[0].D) + int(die) > 15:
            print("You evaded the attack")
            print("get ready for counter attack")
            dex = True

        else:
            print("You tried to evade but you are not fast enough")
            dex = False
        while player[0].H > 0 and wraith_1.H > 0:
            if dex is False:
                attacker = copy.deepcopy(wraith_1)
                target = copy.deepcopy(player[0])
                attack()
                player[0] = copy.deepcopy(target)
                if hit is True and int(player[0].H) <= 0:
                    print(f"you took {ap}points of necrotic damage and you died .....\nStart again I guess")
                    start_game()
                elif hit is True and int(player[0].H) > 0:
                    print(f"you took {ap}points of necrotic damage")
                elif hit is False:
                    print("as wraith materialized from its phantom form you using your weapon you managed to block it")
                dex = True
            if dex is True:
                target = copy.deepcopy(wraith_1)
                attacker = copy.deepcopy(player[0])
                input("press enter to roll the die")
                attack()
                wraith_1 = copy.deepcopy(target)
                if hit is True and wraith_1.H > 0:
                    print(f"you have successfully landed a counter attack you did {ap}points of damage")
                elif hit is True and wraith_1.H <= 0:
                    print(f"you have successfully landed a counter attack you did {ap}points of damage")
                    print("Wraith is dead")
                    act_3()
                elif hit is False:
                    print("As you attacked the wraith vanished and reemerged behind you evading you attack")
                    print("Now it is wraiths turn to attack you from behind")
                dex = False
    elif multi_player is True:
        global choose
        if path_1 is True:
            print("scene2.1 attack of wraiths")
        if path_1 is False:
            print("reach the alter")
            if met_her is True:
                print("That Bitch")
                print("Close its Witch")
            else:
                pass
            print("scene2 attack of wraiths")
        if int(num_players) > 2:
            wraith_2 = Player("wraith_2", "female")
            wraith_2.stats_gen("undead", "wraith")
            wraith_3 = Player("wraith_2", "female")
            wraith_3.stats_gen("undead", "wraith")
            wraith = [wraith_1, wraith_2, wraith_3]
        else:
            wraith_2 = Player("wraith_2", "female")
            wraith_2.stats_gen("undead", "wraith")
            wraith = [wraith_1, wraith_2]
        choose = input("1)alert everybody\n2)Take action to gain the upper had by surprise attack")
        if choose == "1":
            print(f"You alert everybody by shouting {player[int(num_players) - 1].name}lookout a wraith behind you")
            input("Press Enter to roll an evasion roll -need roll less, less is better")
            die = random.randint(0, int(num_players))
            if int(die) < int(num_players) - 1:
                print(f"{player[int(die)].name} attacked it which gave {player[int(num_players) - 1].name} enough time to evade")
            elif int(die) == int(num_players) - 1:
                print(f"{player[int(num_players) - 1].name} managed evade the attack barely, it was a close call")
            elif int(die) == int(num_players):
                target = copy.deepcopy(player[int(num_players) - 1])
                attacker = copy.deepcopy(wraith_1)
                attack()
                player[int(num_players) - 1] = copy.deepcopy(target)
                if hit is True and int(player[int(num_players) - 1].H) <= 0:
                    print(f"you took {ap}points of necrotic damage and you died .....\nStart again I guess")
                    start_game()
                elif hit is True and int(player[int(num_players) - 1].H) > 0:
                    print(f"you took {ap}points of necrotic damage")
                elif hit is False:
                    print("as wraith materialized from its phantom form you using your weapon you managed to block it")

        print("do a initiative roll")
        input("Press Enter to roll the die")
        die = random.randint(1, 20)
        if int(die) > 12:
            print("You took the initiative to attack")
            markp = 0
            markw = 0
            dex = True
        else:
            print("You tried to evade but you are not fast enough")
            markp = 0
            markw = 0
            dex = False
        while player[markp].H > 0 and wraith[markw].H > 0:
            if dex is False:
                attacker = copy.deepcopy(wraith[markw])
                target = copy.deepcopy(player[markp])
                attack()
                player[markp] = copy.deepcopy(target)
                if hit is True and int(player[markp].H) <= 0:
                    print(f"The wraith in its corporeal form reaches and through the chest grabs heart of {player[markp].name} \nand he took {ap}points of necrotic damage which killing him.....")
                    pd += 1
                elif hit is True and int(player[markp].H) > 0:
                    print(f"The wraith in its corporeal form reaches and through the chest grabs heart of {player[markp].name} but he managed to resist it and he took {ap}points of necrotic damage")
                elif hit is False:
                    print("as wraith materialized from its phantom form you using your weapon you managed to block it")
                dex = True
                markp += 1
                if markp > len(player) - 1:
                    markp = 0
                while player[markp] < 0:
                    markp += 1
                    if markp > len(player) - 1:
                        markp = 0
                if pd >= len(player):
                    print("all players died")
                    print("GAME OVER")
                    start_game()
            if dex is True:
                target = copy.deepcopy(wraith[markw])
                attacker = copy.deepcopy(player[markp])
                input("press enter to roll the die")
                attack()
                wraith[markw] = copy.deepcopy(target)
                if hit is True and wraith[markw].H > 0:
                    print(f"you have successfully landed a counter attack you did {ap}points of damage")
                elif hit is True and wraith[markw].H <= 0:
                    print(f"you have successfully landed a counter attack you did {ap}points of damage")
                    print("Wraith is dead")
                    md += 1
                elif hit is False:
                    print("As you attacked the wraith vanished and reemerged behind you evading you attack")
                    print("Now it is wraiths turn to attack you from behind")
                dex = False
                markw += 1
                if markw > len(wraith) - 1:
                    markw = 0
                while wraith[markw].H < 0:
                    markw += 1
                    if markw > len(wraith) - 1:
                        markw = 0
                if md >= len(wraith):
                    print("all the wraiths are dead\nCongratulations you proceed to act 3 ")
                    act_3()


def act_3():
    global target
    global attacker
    global witch
    global witch_2
    global witch_1
    global dex
    global markp
    global markw
    global pd
    pd = 0
    global cn
    cn = 0
    if len(player) > 0:
        witch_1=Player("witch_1", "female")
        witch_1.stats_gen("undead", "witch")
        witch = [witch_1]
    if len(player) > 1:
        witch_2 = Player("witch_2", "female")
        witch_2.stats_gen("undead", "witch")
        witch = [witch_1, witch_2]
    if path_1 is False:
        print()
    elif path_1 is True:
        print()
    print("in cave")
    while player[markp].H > 0 and wraith[markw].H > 0:
        if dex is False:
            attacker = copy.deepcopy(witch[markw])
            target = copy.deepcopy(player[markp])
            attack()
            player[markp] = copy.deepcopy(target)
            cn += 1
            if hit is True and int(player[markp].H) <= 0:
                print(f"The witch gathered ball of Arkaine dark magic and shoots at {player[markp].name} and does {ap}points Hex damage killing him .....")
                pd += 1
            elif hit is True and int(player[markp].H) > 0:
                print(f"The witch gathered ball of Arkaine dark magic and shoots at {player[markp].name} but he manage to resist the spell and took {ap}points Hex damage")
            elif hit is False:
                print("as witch tries to attack you with her claws using your weapon you managed to block it")
            dex = True
            markp += 1
            if markp > int(num_players) - 1:
                markp = 0
            while player[markp] < 0:
                markp += 1
                if markp > int(num_players) - 1:
                    markp = 0
            if pd == int(num_players):
                print("all players died")
                print("GAME OVER")
                start_game()
        if dex is True:
            target = copy.deepcopy(witch[markw])
            attacker = copy.deepcopy(player[markp])
            input("press enter to roll the die")
            attack()
            witch[markw] = copy.deepcopy(target)
            cn += 1
            if hit is True and witch[markw].H > 0:
                print(f"you have successfully landed a counter attack you did {ap}points of damage")
            elif hit is True and witch[markw].H <= 0:
                print(f"you have successfully landed a counter attack you did {ap}points of damage")
                print("Witch is about to dead , how do you want to finish her explain the finishing  move in a great detail to your peers")
                md += 1
                if cn <= 5:
                    print("Seeing her sister defeated so swiftly the other which retreats and turns into flock of ravens exits through the opening at the top of the cave \ncackling and saying 'Till next time adventurers'")
            elif hit is False:
                print("As you attacked the which turns into a flock of ravens and disperses")
                print("Now it is witches turn to attack you from behind")
            dex = False
            markw += 1
            if markw > len(witch) - 1:
                markw = 0
            while wraith[markw].H < 0:
                markw += 1
                if markw > len(witch) - 1:
                    markw = 0
            if md == len(witch):
                print("all the wraiths are dead\nCongratulations you finished your quest ")
                start_game()


title_screen()
