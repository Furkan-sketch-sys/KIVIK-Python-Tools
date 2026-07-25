class Survivor:
    def __init__(self, name , health , stamina , weapon) :
        self.name = name
        self.health = health
        self.stamina = stamina
        self.weapon = weapon
        self.weapon_damage = 45
        self.medkit_count = 3


    def attack(self , enemy) :
        print(f"\n {self.name} attacked to zombie with {self.weapon}. Given damage {self.weapon_damage}")
        enemy.health -= self.weapon_damage

    def use_medkit(self) :
        if self.medkit_count > 0 :
            self.health += 45
            self.medkit_count -= 1
            print(f"\n You used medkit. Current health stability : {self.health}")

        else :
            print(f"\n There's not medkit to use.")


class Zombie :
    def __init__(self , name , damage , health) :
        self.name = name
        self.damage = damage
        self.health = health

    def attack(self , player) :
        player.health -= self.damage
        print(f"\n {self.name} attacked to you. Your current health stability {player.health}")


p1 = Survivor("Kyle Crane" , 100 , 75 , "Legendary Axe")
z1 = Zombie("Volatile" , 45 , 150)

print(f"\n {p1.name} faced with {z1.name} in Harran Streets.")


while p1.health > 0 and z1.health > 0 :
    print("-" * 30)
    print(f"Your current health : {p1.health} | Zombie's health : {z1.health}")
    print(f"1- Attack")
    print(f"2- Get Medkit immediately!")


    choice = input("What will you do? (1/2) : ")
    if choice == "1" :
        p1.attack(z1) 
        if z1.health > 0 :
            z1.attack(p1)
        else :
            print(f"\n Congrulations. {z1.name} is died.")

    elif choice == "2" :
        p1.use_medkit()
        z1.attack(p1)

    else :
        print(f"\n Invalid choice!")

    if p1.health <= 0 :
        print(f"\n You dead.... Zombies killed you. Maybe next time.")
