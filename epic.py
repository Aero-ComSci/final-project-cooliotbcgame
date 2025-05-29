class combatant:
    
    def __init__(self, name, atk, atk2, atk3, def1, hp):
        self.name = name
        self.atk = atk
        self.atk2 = atk2
        self.atk3 = atk3
        self.def1 = def1
        self.hp = hp
    
    def __str__(self):
        bob = ""
        bob += str("Combatant: " + self.name + ": ")
        bob += str("Attack 1: " + str(self.atk) + ", ")
        bob += str("Attack 2: " + str(self.atk2) + ", ")
        bob += str("Attack 3: " + str(self.atk3) + ", ")
        bob += str("Heal: " + str(self.def1) + ", ")
        bob += str("Health: " + str(self.hp) + ", ")
        return bob

    def get_options(self):
      Atks = []
      Atks.append(self.atk)
      Atks.append(self.atk2)
      Atks.append(self.atk3)
      Atks.append(self.def1)
      return Atks
        
    def get_health(self):
        billy = []
        billy.append(self.hp)
        return billy