import random as rd
import copy
import time

class pokemon:
    def __init__(self):
        '''
        Creates a class to store pokemon data.
        Initialised with only 1 attribute, so that running
        readPokemonStats will import relevant hp, attack, defense, and name attributes.
        self.potionCounter keeps track of how many potions the player has used, and maxes
        out at 2 per game.
        Args: 
            None
        Returns: 
            None
        '''
        self.potionCounter = 0
        
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
        enemyPokemon.hp -= round(self.attack-(enemyPokemon.defense/1.5) + rd.randint(-5,5)) # subtracts current pokemon's attack damage from enemy's, 
                                                                                            # divided by a constant and adds a random integer between -5 and 5
                                                                                            # rounded to an integer number
                                                                                            
        
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
        if self.potionCounter >= 2:
            print("All potions have been used! Select another move!")
        elif self.hp == self.maxhp: # check if pokemon is full health
            print(f"{self.name} is already full health!")
        elif diff < 20: # check if pokemon will exceed maximum health after using potion
            print(f"{self.name} healed {diff} hitpoints!")
            self.hp += self.maxhp - self.hp # only heals the difference to full hp
            self.potionCounter += 1 # increases the counter for times the user has used a potion
        else:
            print(f"{self.name} healed 20 hitpoints!")
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
        print(f"{self.name} has run away") # fleeing 
        time.sleep(3) # pauses for 3 seconds before printing the next line
        print(f"{enemyPokemon.name} is victorious!")
        break # after printing the messages, calls a break to stop the gameplay loop
