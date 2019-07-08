import random
enemies = ["lion","tiger","bear","wildebeest","alligator","hyena pack"]
lion_attacks = ["Bite","Claw","Charge","Chomp" ]
curr_enemy = []
enemy_health=[50,75,100,125,150,200]
attack_bonus = 0
armor = 0
level = 0
level_attacks = 0
level_damage = 0
onward = []
print("You are an African warrior, wandering through the Serengeti. You have been trained since youth in the martial arts and hunting. You are about to be tested.\n")
def enemy():
    chosen_enemy =""
    chosen_enemy = enemies[random.randint(0+level,2+level)]
    curr_enemy.insert(0,chosen_enemy)
    return print("A",chosen_enemy.title(),"has attacked!\n")
enemy()
attacks = ["slash" , "charge attack", "killing blow"]
print("Your attack choices are:",attacks[0].strip().title(),",",attacks[1].strip().title(),"or", attacks[2].strip().title(),"\n")
print(attacks[0].title(),"does 15 points of damage with a likely chance of hitting,",attacks[1].title(),"does 30 points of damage with a moderate chance of hitting, and",attacks[2].title(),"is fatal to your enemy, but has a very low chance of hitting your opponent\n")
def attack():
    health= 100 + armor
    while enemy_health[enemies.index(curr_enemy[0])] > 0:
            if health <= 0:
                break
            enemy_attack = lion_attacks[random.randint(0,1)+ level_attacks]
            enemy_attack_chance = random.randint(1,10)
            attack_chance = random.randint(1,10)
            print("Your attack choices are:",attacks[0].strip().title(),",",attacks[1].strip().title(),"or", attacks[2].strip().title(),"\n")
            attack_choice = input("Choose your attack by typing here:")
            if attack_choice.lower() == attacks[0]:
                if attack_chance < 9:
                    enemy_health[enemies.index(curr_enemy[0])] -= (15+attack_bonus)
                    print(attack_choice.title(),"worked!\n")
                    print(curr_enemy[0].title(), "health is at",enemy_health[enemies.index(curr_enemy[0])],"points\n")
                    print("Your health is at:",health,"points\n")
                else:
                    print(attack_choice.title(),"Missed!\n")
                    print(curr_enemy[0].title(), "health is at",enemy_health[enemies.index(curr_enemy[0])],"points\n")
                    print("Your health is at:",health,"points\n")
            if attack_choice.lower() == attacks[1]:
                if attack_chance > 5:
                    enemy_health[enemies.index(curr_enemy[0])] -= (30 + attack_bonus)
                    print(attack_choice.title(),"worked!\n")
                    print(curr_enemy[0].title(), "health is at",enemy_health[enemies.index(curr_enemy[0])],"points\n")
                    print("Your health is at:",health,"points\n")
                else:
                    print(attack_choice.title(), "Missed!\n")
                    print(curr_enemy[0].title(), "health is at",enemy_health[enemies.index(curr_enemy[0])],"points\n")
                    print("Your health is at:",health,"points\n")
            if attack_choice.lower() == attacks[2]:
                if attack_chance > 8:
                        enemy_health[enemies.index(curr_enemy[0])] = 0
                        print(attack_choice.title(),"worked!\n")
                else:
                        print("Attack Missed!\n")
                        print(curr_enemy[0].title(), "health is at",enemy_health[enemies.index(curr_enemy[0])],"points\n")
                        print("Your health is at:",health,"points\n")     
            if enemy_health[enemies.index(curr_enemy[0])] <= 0:
                break
            if enemy_attack == lion_attacks[0+level_attacks]:
                print(curr_enemy[0].title(), "used",lion_attacks[0+level_attacks], "\n")
                if enemy_attack_chance < 8:
                    print(lion_attacks[0+level_attacks].title(),"worked!\n")
                    health -= (15+level_damage)
                    print("Your health is at:",health,"points\n")
                    print(curr_enemy[0].title(), "health is at",enemy_health[enemies.index(curr_enemy[0])],"points\n")
                else:
                     print(curr_enemy[0].title(), "attack missed!\n")
                     print("Your health is at:",health,"points\n")
                     print(curr_enemy[0].title(), "health is at",enemy_health[enemies.index(curr_enemy[0])],"points\n")
            if enemy_attack == lion_attacks[1+level_attacks]:
                print(curr_enemy[0].title(), "used",lion_attacks[1+level_attacks],"\n")
                if enemy_attack_chance > 7:
                    print(lion_attacks[1+level_attacks].title(),"worked!\n")
                    health -= (30+level_damage)
                    print("Your health is at:",health,"points\n")
                    print(curr_enemy[0].title(), "health is at",enemy_health[enemies.index(curr_enemy[0])],"points\n")
                else:
                    print(curr_enemy[0].title(), "attack missed!\n")
                    print("Your health is at:",health,"points\n")
                    print(curr_enemy[0].title(), "health is at",enemy_health[enemies.index(curr_enemy[0])],"points\n")
    if enemy_health[enemies.index(curr_enemy[0])] <= 0:                
        print("You defeated the",curr_enemy[0].title(),"!\n")
        onward.insert(0,"yuh")
    else:
        print("You were defeated. GAME OVER!")
        onward.insert(0,"nuh")
        

    
attack()
level = 3
level_damage = 10
level_attacks = 2
if onward[0] == "yuh":
    print("You skin the",curr_enemy[0].title(),"and take it's pelt. It will be useful for trading at the market. You start the hike to sell your goods.\n")
    print("Once at the market, you have two vendors to trade with. You have your one pelt, and either vendor will trade different objects with you which will improve your combat.\n")
    vendor_choice = input("Will you choose to trade your pelt with Amaj or with Swikaya?\n")
    if vendor_choice.lower() == "amaj":
        armor =  50
        print("You have received light armor, adding 50 points to your overall health points!\n")
    else:
        attack_bonus = 20
        print("You have received an upgraded steel sword, increasing your Slash and Charge Attack damage by 20 points each!\n")
    
    print("You leave the market, feeling satisfied with the days kill and your upgrades\n")
    print("But as you near your village and walk past the watering hole, the worst thing imaginable happens\n")
    enemy()
    attack()
    if onward[0] == "yuh":
        print("You return to your village victorious over your enemies and bring honor to your family! THE END!")