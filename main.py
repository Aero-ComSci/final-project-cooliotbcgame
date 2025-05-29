from epic import combatant
import random
import time


player = combatant("You", 5, 15, 25, 15, 100)
enemy = combatant("Enemy", 10, 15, 20, 15, 200)
ongoing = True

while ongoing:
    print("Here are the combatants and their stats!")
    combatants = [player, enemy]
    for i in combatants:
        print(i)

    youroptions = combatant.get_options(player)
    enemyoptions = combatant.get_options(enemy)
    randomnum = random.randint(0, 3)
    print("Here are your options! The first 3 are attacks, the last is a heal, healing health by the value")
    print(youroptions)
    picked = ""
    while not (picked == 1 or picked == 2 or picked == 3 or picked == 4):
        picked = int(input("What would you like to do? (Enter corresponding number) "))
    picked -= 1
    playermove = youroptions[picked]
    enemyoption = enemyoptions[randomnum]
    DamageTakenU = 0
    DamageTakenE = 0
    time.sleep(1)
    if picked == 0 or picked == 1 or picked == 2:
        print("You attack!")
        DamageTakenE += playermove
    elif picked == 3:
        print("You heal!")
        DamageTakenU -= playermove
    time.sleep(2)
    if randomnum == 0 or randomnum ==  1 or randomnum ==2:
        print("enemy attacks!")
        DamageTakenU += enemyoption
    elif randomnum == 3:
        print("Enemy defends!")
        DamageTakenE -= enemyoption
    time.sleep(2)
    player.hp += -1 * DamageTakenU
    enemy.hp += -1 * DamageTakenE
    print("You take " + str(DamageTakenU) + " damage!")
    print("Enemy takes " + str(DamageTakenE) + " damage!")
    if player.hp <= 0:
        print("You lost!")
        ongoing = False
    elif enemy.hp <= 0:
        print("you win!")
        ongoing = False
    elif enemy.hp <= 0 and player.hp <= 0:
        print("its a draw!")
        ongoing = False
    time.sleep(3)
    