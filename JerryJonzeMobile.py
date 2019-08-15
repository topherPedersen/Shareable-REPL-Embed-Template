import random
import time

length_of_pause = 2

##################################
print("")
print("Jerry Jonze Pro Football")
print("by Topher Pedersen")
print("")
time.sleep(length_of_pause)

##################################
print("You are Jerry Jonze, the")
time.sleep(length_of_pause)
print("billionaire oil tycoon")
time.sleep(length_of_pause)
print("and owner of the most")
time.sleep(length_of_pause)
print("valuable sports team in")
time.sleep(length_of_pause)
print("the world. As owner,")
time.sleep(length_of_pause)
print("general manager, and")
time.sleep(length_of_pause)
print("coach, you will be")
time.sleep(length_of_pause)
print("calling the plays for")
time.sleep(length_of_pause)
print("Dallas...")
time.sleep(length_of_pause)
print()
time.sleep(length_of_pause )

##################################
print("Dallas is currently down")
time.sleep(length_of_pause)
print("by 3 points and on their")
time.sleep(length_of_pause)
print("own 20 yard line in the")
time.sleep(length_of_pause)
print("NFC Championship Game.")
time.sleep(length_of_pause)
print("2 minutes are left on the")
time.sleep(length_of_pause)
print("clock to go 80 yards,")
time.sleep(length_of_pause)
print("score, and win the game..")
time.sleep(length_of_pause)
print()
time.sleep(length_of_pause)

yard_line = 20
down = 1
yards_to_go = 10
game_over = False

while game_over == False:
    play_selected = input("Enter 'run' or 'pass'>>> ")
    yards_gained = random.randint(1, 10)
    yards_to_go = yards_to_go - yards_gained
    yard_line = yard_line + yards_gained

    if yards_to_go <= 0:
        down = 1
        yards_to_go = 10
        yards_gained = str(yards_gained) # cast integer as string

        print("You gain " + yards_gained + " yards.")
        print("First down!")
    else:
        down = down + 1
        yards_gained = str(yards_gained)
        print("You gain " + yards_gained + " yards.")
        
    if yard_line >= 100:
        print("Touchdown.. Dallas advances")
        print("to Super Bowl 54!")
        print()
        print()
        game_over = True
    elif yard_line < 100 and down > 4:
        print("Turnover on downs...")
        print("You lose.")
        print()
        print()
        game_over = True