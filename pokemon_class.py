import random as rd
import copy

class pokemon:
    def __init__(self):
        '''
        Creates a class to store pokemon data.
        Initialised with no attributes, so that running
        readPokemonStats will import relevant hp, attack, defense, and name attributes.
        Args: 
            None
        Returns: 
            None
        '''
     
        
    def useAttack(self, enemyPokemon):
        '''
        attack method will be used during the gameplay loop and is a simple
        function that subtracts the health of the enemy pokemon based on the current
        pokemon's attack value, enemy pokemon's defence value, and a random
        spread to make the game more interesting.
        Args:
            enemyPokemon: pokemon class object other than the current user's
        Returns:
            None
        '''
        
        enemy_defense = enemyPokemon.defense*rd.uniform(0.1,0.5) # defense will be a randomly rolled multiple between 0.1 and 0.5 the pokemon's stats
        self_attack = self.attack*rd.uniform(0.1,0.7) # damage has a higher roll, between 0.1 and 0.7 to reduce the probability attack < defense
        
        if enemy_defense > self_attack: # if defense is higher than attack, attack is less effective and only rolls between 0.1 to 0.5
            self_attack = self.attack*rd.uniform(0.1,0.5)
        
        self.damage = round(self_attack - enemy_defense) # final damage inflicted is based on the calculations above
        
        if self.damage < 0: # damage cannot be negative to prevent healing a pokemon by attacking it
            self.damage = 0
        
        enemyPokemon.hp -= self.damage # subtracting the final calculated damage from enemy pokemon's health
        
    def usePotion(self):
        '''
        potion method is used to heal the current user's pokemond by 20hp.
        If self.hp is at the maximum health, self.maxhp, the potion will not be used,
        and user will be asked for another input. Potion will only heal 20hp or until
        maximum health.
        Args:
            None
        Returns:
            None
        '''
        diff = self.maxhp - self.hp # checks the difference between current health and maximum health
        if self.potionCounter > 2:
            print("All potions have been used! Select another move!")
            raise ValueError
        elif self.hp == self.maxhp: # check if pokemon is full health
            print(f"{self.pokemon_name.upper()} is already full health!")
            raise ValueError
        elif diff < 20: # check if pokemon will exceed maximum health after using potion
            print(f"{self.pokemon_name.upper()} healed {diff} hitpoints!")
            self.hp += self.maxhp - self.hp # only heals the difference to full hp
            self.potionCounter += 1 # increases the counter for times the user has used a potion
        else:
            print(f"{self.pokemon_name.upper()} healed 20 hitpoints!")
            self.hp += 20 # increases health by 20 otherwise if health is below thresholds
            self.potionCounter += 1 # increases the counter for times the user has used a potion
            
    def run(self, enemyPokemon):
        '''
        Players can use run if they wish to forfeit the battle.
        Running this method will break the gameplay loop and announce
        the enemy player as victorious.
        Args:
            enemyPokemon: pokemon class object other than the current user's
        Returns:
            None
        '''
        print(f"{self.pokemon_name.upper()} has run away") # fleeing 
        print(f"{enemyPokemon.pokemon_name.upper()} is victorious!") # declares enemy victorious after fleeing
