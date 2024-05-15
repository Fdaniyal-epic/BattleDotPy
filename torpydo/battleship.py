import random
import os
import colorama
import platform

from colorama import Fore, Back, Style
from torpydo.ship import Color, Letter, Position, Ship
from torpydo.game_controller import GameController
from torpydo.telemetryclient import TelemetryClient

print("Starting")

myFleet = []
enemyFleet = []

def main():
    TelemetryClient.init()
    TelemetryClient.trackEvent('ApplicationStarted', {'custom_dimensions': {'Technology': 'Python'}})
    colorama.init()
    print(Fore.YELLOW + r"""
                                    |__
                                    |\/
                                    ---
                                    / | [
                             !      | |||
                           _/|     _/|-++'
                       +  +--|    |--|--|_ |-
                     { /|__|  |/\__|  |--- |||__/
                    +---------------___[}-_===_.'____                 /\
                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _
 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7
|                        Welcome to Battleship                         BB-61/
 \_________________________________________________________________________|""" + Style.RESET_ALL)

    initialize_game()

    start_game()

def start_game():
    global myFleet, enemyFleet
    # clear the screen
    if(platform.system().lower()=="windows"):
        cmd='cls'
    else:
        cmd='clear'   
    os.system(cmd)
    print(r'''
                  __
                 /  \
           .-.  |    |
   *    _.-'  \  \__/
    \.-'       \
   /          _/
   |      _  /
   |     /_\
    \    \_/
     """"""""''')

    while True:
        print()
        print("Player, it's your turn")
        position = parse_position(input("Enter coordinates for your shot :"))
        is_hit = GameController.check_is_hit(enemyFleet, position)
        if is_hit:
            print(Fore.RED + r'''
                \          .  ./
              \   .:"";'.:..""   /
                 (M^^.^~~:.'"").
            -   (/  .    . . \ \)  -
               ((| :. ~ ^  :. .|))
            -   (\- |  \ /  |  /)  -
                 -\  \     /  /-
                   \  \   /  /''' + Style.RESET_ALL)
            
        else:
            print(Fore.BLUE + r'''
                \          .  ./
              \   .:"";'.:..""   /
                 (M^^.^~~:.'"").
            -   (/  .    . . \ \)  -
               ((| :. ~ ^  :. .|))
            -   (\- |  \ /  |  /)  -
                 -\  \     /  /-
                   \  \   /  /''' + Style.RESET_ALL)

        # print(enemyFleet)
        print("Yeah ! Nice hit !" if is_hit else "Miss")
        TelemetryClient.trackEvent('Player_ShootPosition', {'custom_dimensions': {'Position': str(position), 'IsHit': is_hit}})

        position = get_random_position()
        is_hit = GameController.check_is_hit(myFleet, position)
        print()
        print(f"Computer shoot in {str(position)} and {'hit your ship!' if is_hit else 'miss'}")
        TelemetryClient.trackEvent('Computer_ShootPosition', {'custom_dimensions': {'Position': str(position), 'IsHit': is_hit}})
        if is_hit:
            print(Fore.RED + r'''
                \          .  ./
              \   .:"";'.:..""   /
                 (M^^.^~~:.'"").
            -   (/  .    . . \ \)  -
               ((| :. ~ ^  :. .|))
            -   (\- |  \ /  |  /)  -
                 -\  \     /  /-
                   \  \   /  /''' + Style.RESET_ALL)
            
        else:
            print(Fore.BLUE + r'''
                \          .  ./
              \   .:"";'.:..""   /
                 (M^^.^~~:.'"").
            -   (/  .    . . \ \)  -
               ((| :. ~ ^  :. .|))
            -   (\- |  \ /  |  /)  -
                 -\  \     /  /-
                   \  \   /  /''' + Style.RESET_ALL)

def parse_position(input: str):
    letter = Letter[input.upper()[:1]]
    number = int(input[1:])
    position = Position(letter, number)

    return Position(letter, number)

def get_random_position():
    rows = 8
    lines = 8

    letter = Letter(random.randint(1, lines))
    number = random.randint(1, rows)
    position = Position(letter, number)

    return position

def initialize_game():
    initialize_myFleet()

    initialize_enemyFleet()

def initialize_myFleet():
    global myFleet

    myFleet = GameController.initialize_ships()

    myFleet[0].positions.append(Position(Letter.B, 4))
    myFleet[0].positions.append(Position(Letter.B, 5))
    myFleet[0].positions.append(Position(Letter.B, 6))
    myFleet[0].positions.append(Position(Letter.B, 7))
    myFleet[0].positions.append(Position(Letter.B, 8))

    myFleet[1].positions.append(Position(Letter.E, 5))
    myFleet[1].positions.append(Position(Letter.E, 6))
    myFleet[1].positions.append(Position(Letter.E, 7))
    myFleet[1].positions.append(Position(Letter.E, 8))

    myFleet[2].positions.append(Position(Letter.A, 3))
    myFleet[2].positions.append(Position(Letter.B, 3))
    myFleet[2].positions.append(Position(Letter.C, 3))

    myFleet[3].positions.append(Position(Letter.F, 8))
    myFleet[3].positions.append(Position(Letter.G, 8))
    myFleet[3].positions.append(Position(Letter.H, 8))

    myFleet[4].positions.append(Position(Letter.C, 5))
    myFleet[4].positions.append(Position(Letter.C, 6))


    # myFleet = GameController.initialize_ships()

    # print("Please position your fleet (Game board has size from A to H and 1 to 8) :")

    # for ship in myFleet:
    #     print()
    #     print(f"Please enter the positions for the {ship.name} (size: {ship.size})")

    #     for i in range(ship.size):
    #         position_input = input(f"Enter position {i+1} of {ship.size} (i.e A3):")
    #         ship.add_position(position_input)
    #         TelemetryClient.trackEvent('Player_PlaceShipPosition', {'custom_dimensions': {'Position': position_input, 'Ship': ship.name, 'PositionInShip': i}})

def initialize_enemyFleet():
    global enemyFleet

    # preset 1
    enemyFleet0 = GameController.initialize_ships()

    enemyFleet0[0].positions.append(Position(Letter.B, 4))
    enemyFleet0[0].positions.append(Position(Letter.B, 5))
    enemyFleet0[0].positions.append(Position(Letter.B, 6))
    enemyFleet0[0].positions.append(Position(Letter.B, 7))
    enemyFleet0[0].positions.append(Position(Letter.B, 8))

    enemyFleet0[1].positions.append(Position(Letter.E, 5))
    enemyFleet0[1].positions.append(Position(Letter.E, 6))
    enemyFleet0[1].positions.append(Position(Letter.E, 7))
    enemyFleet0[1].positions.append(Position(Letter.E, 8))

    enemyFleet0[2].positions.append(Position(Letter.A, 3))
    enemyFleet0[2].positions.append(Position(Letter.B, 3))
    enemyFleet0[2].positions.append(Position(Letter.C, 3))

    enemyFleet0[3].positions.append(Position(Letter.F, 8))
    enemyFleet0[3].positions.append(Position(Letter.G, 8))
    enemyFleet0[3].positions.append(Position(Letter.H, 8))

    enemyFleet0[4].positions.append(Position(Letter.C, 5))
    enemyFleet0[4].positions.append(Position(Letter.C, 6))

    # preset 2
    enemyFleet1 = GameController.initialize_ships()

    enemyFleet1[0].positions.append(Position(Letter.A, 7))
    enemyFleet1[0].positions.append(Position(Letter.B, 7))
    enemyFleet1[0].positions.append(Position(Letter.C, 7))
    enemyFleet1[0].positions.append(Position(Letter.D, 7))
    enemyFleet1[0].positions.append(Position(Letter.E, 7))

    enemyFleet1[1].positions.append(Position(Letter.B, 1))
    enemyFleet1[1].positions.append(Position(Letter.C, 1))
    enemyFleet1[1].positions.append(Position(Letter.D, 1))
    enemyFleet1[1].positions.append(Position(Letter.E, 1))

    enemyFleet1[2].positions.append(Position(Letter.H, 1))
    enemyFleet1[2].positions.append(Position(Letter.H, 2))
    enemyFleet1[2].positions.append(Position(Letter.H, 3))

    enemyFleet1[3].positions.append(Position(Letter.H, 5))
    enemyFleet1[3].positions.append(Position(Letter.H, 6))
    enemyFleet1[3].positions.append(Position(Letter.H, 7))

    enemyFleet1[4].positions.append(Position(Letter.D, 4))
    enemyFleet1[4].positions.append(Position(Letter.D, 5))
    # preset 3
    enemyFleet2 = GameController.initialize_ships()

    enemyFleet2[0].positions.append(Position(Letter.A, 5))
    enemyFleet2[0].positions.append(Position(Letter.B, 5))
    enemyFleet2[0].positions.append(Position(Letter.C, 5))
    enemyFleet2[0].positions.append(Position(Letter.D, 5))
    enemyFleet2[0].positions.append(Position(Letter.E, 5))

    enemyFleet2[1].positions.append(Position(Letter.H, 4))
    enemyFleet2[1].positions.append(Position(Letter.H, 5))
    enemyFleet2[1].positions.append(Position(Letter.H, 6))
    enemyFleet2[1].positions.append(Position(Letter.H, 7))

    enemyFleet2[2].positions.append(Position(Letter.E, 2))
    enemyFleet2[2].positions.append(Position(Letter.F, 2))
    enemyFleet2[2].positions.append(Position(Letter.G, 2))

    enemyFleet2[3].positions.append(Position(Letter.D, 7))
    enemyFleet2[3].positions.append(Position(Letter.E, 7))
    enemyFleet2[3].positions.append(Position(Letter.F, 7))

    enemyFleet2[4].positions.append(Position(Letter.A, 8))
    enemyFleet2[4].positions.append(Position(Letter.B, 8))

    # preset 4
    enemyFleet3 = GameController.initialize_ships()

    enemyFleet3[0].positions.append(Position(Letter.D, 6))
    enemyFleet3[0].positions.append(Position(Letter.E, 6))
    enemyFleet3[0].positions.append(Position(Letter.F, 6))
    enemyFleet3[0].positions.append(Position(Letter.G, 6))
    enemyFleet3[0].positions.append(Position(Letter.H, 6))

    enemyFleet3[1].positions.append(Position(Letter.D, 8))
    enemyFleet3[1].positions.append(Position(Letter.E, 8))
    enemyFleet3[1].positions.append(Position(Letter.F, 8))
    enemyFleet3[1].positions.append(Position(Letter.G, 8))

    enemyFleet3[2].positions.append(Position(Letter.A, 3))
    enemyFleet3[2].positions.append(Position(Letter.A, 4))
    enemyFleet3[2].positions.append(Position(Letter.A, 5))

    enemyFleet3[3].positions.append(Position(Letter.H, 2))
    enemyFleet3[3].positions.append(Position(Letter.H, 3))
    enemyFleet3[3].positions.append(Position(Letter.H, 4))

    enemyFleet3[4].positions.append(Position(Letter.F, 2))
    enemyFleet3[4].positions.append(Position(Letter.G, 2))

    # preset 5
    enemyFleet4 = GameController.initialize_ships()

    enemyFleet4[0].positions.append(Position(Letter.A, 1))
    enemyFleet4[0].positions.append(Position(Letter.B, 2))
    enemyFleet4[0].positions.append(Position(Letter.C, 3))
    enemyFleet4[0].positions.append(Position(Letter.D, 4))
    enemyFleet4[0].positions.append(Position(Letter.E, 5))

    enemyFleet4[1].positions.append(Position(Letter.H, 3))
    enemyFleet4[1].positions.append(Position(Letter.H, 4))
    enemyFleet4[1].positions.append(Position(Letter.H, 5))
    enemyFleet4[1].positions.append(Position(Letter.H, 6))

    enemyFleet4[2].positions.append(Position(Letter.A, 7))
    enemyFleet4[2].positions.append(Position(Letter.B, 7))
    enemyFleet4[2].positions.append(Position(Letter.C, 7))

    enemyFleet4[3].positions.append(Position(Letter.F, 8))
    enemyFleet4[3].positions.append(Position(Letter.G, 8))
    enemyFleet4[3].positions.append(Position(Letter.H, 8))

    enemyFleet4[4].positions.append(Position(Letter.F, 6))
    enemyFleet4[4].positions.append(Position(Letter.G, 6))

    enemyFleet = random.choice([enemyFleet0, enemyFleet1, enemyFleet2, enemyFleet3, enemyFleet4])

if __name__ == '__main__':
    main()
