from pip._vendor.distlib.compat import raw_input
import time


def quest_ans():
    quest = {
        "Blind Cliff Cave": "Go into Blind Cliff Cave and take back control from the bandits for the town Karthwasten",
        "The Man Who Cried Wolf": "Speak to Falk Firebeard in Solitude"
    }
    return quest


def inven_weapons():
    weapons = {
        '- Elven Sword': ' - Melee' + '\n' + ' - Damage: ' + str(11),
        '- Drainspell Bow': ' - Range' + '\n' + ' - Damage: ' + str(14),
    }
    return weapons


def inven_spells():
    spells = {
        '- Fireball': ' -Destruction projectile' + '\n' + ' - Damage:' + str(40) + '\n' + ' - Magicka Cost:' + str(133),
        '- Sparks': ' -Destruction projectile' + '\n' + ' - Damage:' + str(32) + '\n' + ' - Magicka Cost:' + str(76),
    }
    return spells


def inven_potions():
    potions = {
        '- Minor Healing Potion:': " - Restore 25 points of Health " + '\n' + " - Quantity: " + str(2),
        '- Potion of Plentiful Healing:': " - Restore 75 points of Health " + '\n' + " - Quantity: " + str(1),
        '- Potion of Magicka:': " - Restore 50 points of Magicka " + "\n" + " - Quantity: " + str(1),
    }
    return potions


def blind_cliff():
    print('---------------------------------------------------------------------------------\n'
          'You have now fast traveled to the Blind Cave, there is going to be bandits inside.\n '
          'You will need to eliminate and report back to Karthwasten to inform the leader.\n'
          '-------------------------------------------------------------------------------')

    enter_cave = input('Do you want to enter the cave. Yes or no?')

    if enter_cave[0].lower() == "y":
        print('Alright you have now entered the Blind Cave.'
              'The cave is dark, gloomy, and musty cave air fills yours nose')

        weapondrawn = input('Which weapon do you have drawn? To check your weapons open the menu ')


        print('you head slowly down the ramp with your ')

    elif enter_cave[0].lower() == "n":
        print('come back to the quest anytime by selecting it under the quest option.')

    else:
        print('That is not a option')
        return blind_cliff()


def cried_wolf():
    print('---------------------------------------------------------------------------------\n'
          'You have now fast traveled to the town of Solitude\n'
          'You need to talk to Falk Firebeard to get your next instructions\n'
          '-------------------------------------------------------------------------------\n\n')

    return cried_wolf()


def main_menu():  # Main Menu UI
    ans = True
    while ans:
        print("""
        --------
        1.Quest
        2.Inventory
        3.Exit/Quit
        --------
        """)
        ans = raw_input("What would you like to do? Enter number for choice. ")
        if ans == "1":
            my_quest = quest_ans()
            for keys, values in my_quest.items():
                print("─────────────────────────", "\n", keys + ":")
                print('✗' + values, "\n", '─────────────────────────')
            time.sleep(7)
        elif ans == "2":
            print('--------------------------'
                  '\nYou are now in your bag')
            inven_menu()
        elif ans == "3":
            print("\n Returning to game...")
            time.sleep(.5)
            ans = None
        else:
            print(" ─────────────────────────────", "\n", "Not Valid Choice Try again", "\n",
                  "─────────────────────────────", )
            ans = True


def inven_menu():  # Inventory Menu UI
    ads = True
    while ads:
        print("""
         ---------
         1.Weapons
         2.Spells
         3.Potions
         4.Exit to game
         5.Go to Main Menu
         --------------
        """)
        ads = raw_input("What would you like to do? Enter number for choice. ")
        if ads == "1":
            my_weapons = inven_weapons()
            for keys, values in my_weapons.items():
                print("─────────────────────────", "\n", keys)
                print(values, "\n", '─────────────────────────')
            time.sleep(6)
        elif ads == "2":
            my_spells = inven_spells()
            for keys, values in my_spells.items():
                print("─────────────────────────", "\n", keys)
                print(values, "\n", '─────────────────────────')
            time.sleep(6)
        elif ads == "3":
            my_potions = inven_potions()
            for keys, values in my_potions.items():
                print("─────────────────────────", "\n", keys)
                print(values, "\n", '─────────────────────────')
            time.sleep(7)
        elif ads == "4":
            print('---------------------- \n Exiting to game \n ---------------------')
            ads = None
        elif ads == "5":
            print('---------------------- \n Going to Main Menu \n ---------------------')
            main_menu()
        else:
            print(" ───────────────────────────── \n Not Valid Choice Try again \n ─────────────────────────────", )
            ads = None


def start_skyrim():  # Starting the Main game
    ain = True
    while ain:
        newgame = input("Do you want to play skyrim? Yes or no? ")
        if newgame[0].lower() == "y":
            time.sleep(.5)
            print("alright lets play!")
            time.sleep(1)
            break
        elif newgame[0].lower() == "n":
            print("alright, goodbye")
            break
        else:
            print("Give a valid command")
            ain = True


start_skyrim()


def first_adven():  # First adventure and Menu tutorial
    ais = True
    while ais:
        tutorial_menu = input('\nHello Dragon Born! You are about to embark on your first quest. '
                              '\nYou have 2 side quest, enter Menu to open the Menu and see your quest. ')
        if tutorial_menu[0].lower() == "m":
            print('-------------------------------------------------------------------------------'
                  '\nThis is the menu, you can access your Inventory, Quest, and quit the game here.\n'
                  'Look at the quest so you can pick one later, exit/quit to get started on a quest.\n'
                  '-------------------------------------------------------------------------------')
            main_menu()
            ais = None
        else:
            print('---------------------- \n Enter Menu to continue \n ---------------------')

    while True:  # Start of first quest
        insert_quest = input('----------------------------------------------------------------------\n'
                             'To get started on a quest enter the quest you would like to complete.\n'
                             '----------------------------------------------------------------------')
        if insert_quest == "Blind Cliff Cave":
            time.sleep(1)
            print('\nFast traveling...\n')
            blind_cliff()
        elif insert_quest == "The Man Who Cried Wolf":
            time.sleep(1)
            print('\nFast traveling...\n')
            cried_wolf()
        else:
            print('That quest does not exist or you do not have it yet.')


first_adven()

