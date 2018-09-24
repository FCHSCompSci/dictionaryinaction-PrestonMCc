from pip._vendor.distlib.compat import raw_input
from pygame import *
import pygame
import sys

mixer.init()
mixer.music.load('Skyrim intro music Dovahkiin.ogg')


def quest_ans():
    quest = {
        "Blind Cliff Cave": "Go into Blind Cliff Cave and take back control from the bandits for the town Karthwasten",
        "The Man Who Cried Wolf": "Speak to Falk Firebeard in Solitude"
    }
    return quest


def inven_weapons():
    weapons = {
        'Elven Sword': ' - Melee' + '\n' + ' - Damage: ' + str(11),
        'Drainspell Bow': ' - Range' + '\n' + ' - Damage: ' + str(14),
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


def mid_adven():
    ais = True
    while ais:  # Start of first quest

        insert_quest = input('----------------------------------------------------------------------\n'
                             'To get started on a quest enter the quest you would like to complete.\n'
                             '----------------------------------------------------------------------')
        if insert_quest == "Blind Cliff Cave":
            mixer.music.stop()

            mixer.init()
            mixer.music.load('Sad Ambient Medieval Music - The Final Labor.ogg')
            mixer.music.play()

            print('\nFast traveling...\n')
            pygame.time.wait(10000)
            print('\nFast traveling...\n')
            pygame.time.wait(10000)
            print('\nFast traveling...\n')
            pygame.time.wait(1000)
            print('\nFast traveling...\n')
            blind_cliff()

        if insert_quest == "The Man Who Cried Wolf":
            mixer.music.stop()

            mixer.init()
            mixer.music.load('Sad Ambient Medieval Music - The Final Labor.ogg')
            mixer.music.play()

            print('\nFast traveling...\n')
            pygame.time.wait(10000)
            print('\nFast traveling...\n')
            pygame.time.wait(10000)
            print('\nFast traveling...\n')
            pygame.time.wait(1000)
            print('\nFast traveling...\n')
            cried_wolf()

    return mid_adven()


def blind_cliff():
    print('---------------------------------------------------------------------------------\n'
          'You have now fast traveled to the Blind Cave, there is going to be bandits inside.\n '
          'You will need to eliminate and report back to Karthwasten to inform the leader.\n'
          '-------------------------------------------------------------------------------\n\n')

    enter_cave = input('Do you want to enter the cave. Yes or no?')

    if enter_cave[0].lower() == "y":
        mixer.music.stop()
        mixer.music.load('Skyrim Music - Cave 2.ogg')
        mixer.music.play()
        print('============================================\n'
              'Alright you have now entered the Blind Cave.\n'
              'The cave is dark, gloomy, and musty cave air fills yours nose\n'
              '=============================================================\n\n')

    elif enter_cave[0].lower() == "n":
        print('come back to the quest anytime by selecting it under the quest option.')

    # insert mid_adven

    else:
        print('That is not a option')

    ais = True
    while ais:
        my_weapons = inven_weapons()
        weapondrawn = input('Which weapon do you have drawn? To check your weapons enter weapons.')

        if weapondrawn == "weapons":
            for keys, values in my_weapons.items():
                print("─────────────────────────", "\n", keys)
                print(values, "\n", '─────────────────────────')

        elif weapondrawn in my_weapons:
            print('==================================================================================\n'
                  'You head slowly down further into the cave with your ' + weapondrawn + ' drawn\n'
                  '==================================================================================')
            blindcliff2()
        elif weapondrawn not in my_weapons:
            print('\n' + 'You do not have that weapon.' + '\n')

    return blind_cliff()


def blindcliff2():
    blindchoice1 = input('You enter a open area, but you cant see because it to dark. Do you [Equip a torch]'
                         'or choose to [Walk around in the dark]\n')
    if blindchoice1 == 'Equip a torch':
        print('A group of deadly skeevers were lurching in the dark! '
              'They notice the torch and get in attack position!\n')
        op()


def op():
        skeevattack = input('You can [attack] or you can try to run[run]!')
        if skeevattack == "attack":
            print('\n\n=============================\n'
                  'This is the end of the alpha,\n'
                  'Thank you for testing :)\n'
                  'If youd like you can try the other quest\n'
                  '========================================')
            exit()
        elif skeevattack == "run":
            print('\n\n=============================\n'
                  'This is the end of the alpha,\n'
                  'Thank you for testing :)\n'
                  'If youd like you can try the other quest\n'
                  '========================================')
            exit()
        else:
            print('---------------------- \n Enter valid command \n ---------------------')

        return op()


def cried_wolf():
    asi = True
    while asi:
        print('---------------------------------------------------------------------------------\n'
              'You have now fast traveled to the town of Solitude\n'
              'You need to talk to Falk Firebeard to get your next instructions\n'
              '-------------------------------------------------------------------------------\n\n')
        criedwolfchoice = input('Do you want to talk to Falk Firebeard, yes or no')
        if criedwolfchoice[0].lower() == "y":
            print('\n\n=============================\n'
                  'This is the end of the alpha,\n'
                  'Thank you for testing :)\n'
                  'If youd like you can try the other quest\n'
                  '========================================')
            exit()
        if criedwolfchoice[0].lower() == "n":
            print('\n\n=============================\n'
                  'This is the end of the alpha,\n'
                  'Thank you for testing :)\n'
                  'If youd like you can try the other quest\n'
                  '========================================')
            exit()
        else:
            print('---------------------- \n Enter vaild command \n ---------------------')


def main_menu():  # Main Menu UI
    ans = True
    while ans:
        print("""
        --------
        1.Quest
        2.Inventory(buggy,work in progress)
        3.Exit to game
        --------
        """)
        ans = raw_input("What would you like to do? Enter number for choice. ")
        if ans == "1":
            my_quest = quest_ans()
            for keys, values in my_quest.items():
                print("─────────────────────────", "\n", keys + ":")
                print('✗' + values, "\n", '─────────────────────────')
            pygame.time.wait(700)
        elif ans == "2":
            print('--------------------------'
                  '\nYou are now in your bag')
            inven_menu()
        elif ans == "3":
            print("\n Returning to game...")
            pygame.time.wait(700)
            mid_adven()
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
         4.Go to Main Menu
         --------------
        """)
        ads = raw_input("What would you like to do? Enter number for choice. ")
        if ads == "1":
            my_weapons = inven_weapons()
            for keys, values in my_weapons.items():
                print("─────────────────────────", "\n", keys)
                print(values, "\n", '─────────────────────────')
            pygame.time.wait(700)
        elif ads == "2":
            my_spells = inven_spells()
            for keys, values in my_spells.items():
                print("─────────────────────────", "\n", keys)
                print(values, "\n", '─────────────────────────')
            pygame.time.wait(700)
        elif ads == "3":
            my_potions = inven_potions()
            for keys, values in my_potions.items():
                print("─────────────────────────", "\n", keys)
                print(values, "\n", '─────────────────────────')
            pygame.time.wait(700)
        elif ads == "4":
            print('---------------------- \n Going to Main Menu \n ---------------------')
            ads = None
        else:
            print(" ───────────────────────────── \n Not Valid Choice Try again \n ─────────────────────────────", )
            ads = None


def start_skyrim():  # Starting the Main game
    mixer.music.play()
    ain = True
    while ain:
        newgame = input('Do you want to play skyrim? Yes or no?')
        if newgame[0].lower() == "y":
            pygame.time.wait(700)
            print("alright lets play!")
            pygame.time.wait(700)
            break
        elif newgame[0].lower() == "n":
            print("alright, goodbye")
            break
        else:
            print("Give a valid command")
            ain = True


start_skyrim()


def start_adven():  # First adventure and Menu tutorial
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


start_adven()
