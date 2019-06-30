class Player:
    def __init__(self, player_name, G):
        self.player_name = player_name  ## name of the player
        self.R = ""     ## R  is for race
        self.P = ""     ## P  is for profession
        self.G = G      ## Gender
        self.S = 0      ## Strength
        self.H = 0      ## Health
        self.D = 0      ## Dexterity
        self.W = 0      ## Wisdom
        self.status_effect = ["Alive", "no statuses applied yet"]
        self.skill = []

    def stats_gen(self, R, P):
            self.R = R
            self.P = P
            if R.lower() == "human":
                self.H = 20
                self.S = 10
                self.D = 10
                self.W = 20
            elif R.lower() == "elf":
                self.H = 15
                self.S = 10
                self.D = 30
                self.W = 25
            elif R.lower() == "halfling":
                self.H = 25
                self.S = 14
                self.D = 20
                self.W = 15
            elif R.lower() == "undead":
                self.H = 25
                self.S = 13
                self.D = 10
                self.W = 30

            if P.lower() == "swordsmen":
                self.A = 18
                self.skill = ["fast_attack" , "heavy_attack", "taunt", "rage"]
            elif P.lower() == "archer":
                self.A = 13
                self.skill = ["attack", "dragon_piercer", "arrow_barrage", "smoke_bomb"]
            elif P.lower() == "mage":
                self.A = 14
                self.skill = ["magic_ball", "heal", "shield", "magical_catastrophe"]
            elif P.lower() == "rogue":
                self.A = 16
                self.skill = ["shadow_step", "sneak_attack", "slip", "assassination"]
            elif P.lower() == "wraith":
                self.A = 15
                self.skill = ["sole Dissipation", "Ethereal form", "Flash"]
            elif P.lower() == "witch":
                self.A = 15
                self.skill = ["curse confusion", "curse of reaper", "Swarm"]




