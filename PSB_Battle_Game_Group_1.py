import random

print("Welcome to PSB Battle Game!\nIn the battle game, there will be a team of players against a team of AI players.\n"
      "Each player can choose to be a warrior or a tanker.\nThe warrior's damage will be higher compared to the tanker's. "
      "However, the tanker's defense is higher, so choose strategically. \nGood luck to all, and let the battle begin!\n")
print("-" * 90)

class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.health = 100
        self.defense = 0
        self.experience = 0
        self.level = 0
        self.coins = 0

    def select_class(self):
        while True:
            choice = input(f"{self.name}, select your class (1. Warrior 2. Tanker): ")
            if choice in ["1", "2"]:
                self.player_class = "Warrior" if choice == "1" else "Tanker"
                if self.player_class == "Warrior":
                    self.defense = 10  # Lower defense for warrior
                else:
                    self.defense = 30  # Higher defense for tanker
                break
            else:
                print("Invalid choice. Please choose 1 for Warrior or 2 for Tanker.")

    def inflict_damage(self, opponent):
        if opponent.health > 0:
            if self.player_class == "Warrior":
                damage = random.randint(15, 30) - opponent.defense // 2
            else:
                damage = random.randint(5, 15) - opponent.defense // 3
            damage = max(damage, 0)  # Ensure that damage can't be negative
            opponent.health -= damage
            self.coins += 1  # Increase coins whenever damage is inflicted
            print(f"{self.name} inflicts {damage} damage on {opponent.name}.")

    def gain_experience(self):
        if self.player_class == "Warrior":
            self.experience += random.randint(5, 10)
        else:
            self.experience += random.randint(3, 8)
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        print(f"{self.name} has leveled up to level {self.level}!")

    def __str__(self):
        return f"{self.name:<20} | {self.team:<10} | {self.player_class:<10} | {self.health:<10} | {self.defense:<10} | {self.experience:<15} | {self.level:<10} | {self.coins:<10}"

class AIPlayer(Player):
    def __init__(self):
        super().__init__(f"AI{random.randint(0, 99)}", "AI Team")
        self.player_class = random.choice(["Warrior", "Tanker"])
        if self.player_class == "Warrior":
            self.defense = 10
        else:
            self.defense = 30  # Higher defense for AI tanker

def main():
    players = []
    num_players = 3

    for i in range(num_players):
        player_name = input(f"Enter Player {i + 1}'s name: ")
        player = Player(player_name, "Group1")  # Changed team name to "Group1"
        player.select_class()
        players.append(player)

    ai_players = [AIPlayer() for _ in range(num_players)]

    gameplay(players, ai_players)
    print("\nGame Over!")
    display_winner(players, ai_players)

def gameplay(players, ai_players):
    while any(player.health > 0 for player in players) and any(ai_player.health > 0 for ai_player in ai_players):
        # Display the current game status
        print("\nTurn Start")
        print("-" * 90)
        print(f"{'Player Name':<20} | {'Team':<10} | {'Class':<10} | {'Health':<10} | {'Defense':<10} | {'Experience':<15} | {'Level':<10} | {'Coins':<10}")
        print("-" * 90)
        for player in players:
            print(player)
        for ai_player in ai_players:
            print(ai_player)
        print("-" * 90)

        # Players' turns
        for player in players:
            print(f"{player.name}'s turn:")
            opponent = random.choice(ai_players)  # Choose a random AI player as opponent
            player.inflict_damage(opponent)
            player.gain_experience()

        # AI players' turns
        for ai_player in ai_players:
            print(f"{ai_player.name}'s turn:")
            opponent = random.choice(players)  # Choose a random player as opponent
            ai_player.inflict_damage(opponent)
            ai_player.gain_experience()

        # Check for level up
        leveled_up_players = [player for player in players if player.level > 0]
        if leveled_up_players:
            print("\nPlayers who leveled up:")
            for player in leveled_up_players:
                print(f"{player.name} (Level {player.level})")

        print("\nTurn End")
        print("-" * 90)
        print(f"{'Player Name':<20} | {'Team':<10} | {'Class':<10} | {'Health':<10} | {'Defense':<10} | {'Experience':<15} | {'Level':<10} | {'Coins':<10}")
        print("-" * 90)
        for player in players:
            print(player)
        for ai_player in ai_players:
            print(ai_player)
        print("-" * 90)

def display_winner(players, ai_players):
    player_healths = [player.health for player in players]
    ai_healths = [ai_player.health for ai_player in ai_players]

    if any(player.health > 0 for player in players) and not any(ai_player.health > 0 for ai_player in ai_players):
        print("\nGroup 1 is the winner!")
    elif any(ai_player.health > 0 for ai_player in ai_players) and not any(player.health > 0 for player in players):
        print("\nAI Team is the winner!")
    else:
        print("\nIt's a tie!")

if __name__ == "__main__":
    main()
