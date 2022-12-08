import numpy as np
import pandas as pd
import matplotlib.image as mpimg
import random
import matplotlib.pyplot as plt
from PIL import Image
import requests
from pokemon_class import pokemon
from IPython.display import clear_output as clear

pokemonData = pd.read_csv("pokemon.csv")
pokemonData_png = pd.read_csv("metadata.csv")
pokemonData = pokemonData[['abilities', 'hp', 'name', 'attack', 'defense']]
pokemonData = pokemonData.apply(lambda x: x.astype(str).str.lower())
pokemonData = pokemonData.sort_values('name')
pokemonData_png = pokemonData_png.sort_values('filename')
pokemonData.insert(0, 'sprite_url', pokemonData_png['sprite_url'])
pokemonData = pokemonData.set_index('name')

def display_pokemon(my_poke1, current_hp1, my_poke2, current_hp2):
    '''
    Displays the competing Pokemon and their HP bars.
    Args:
        my_poke1: string with the name of Player 1's Pokemon
        current_hp1: Player 1's Pokemon's current health (string or int)
        my_poke2: string with Player 2's Pokemon
        current_hp2: Player 2's Pokemon's current health (string or int)
    Returns:
        None
    Example:
        my_poke1: "pikachu"
        my_poke2: "charizard"
        Function will display pixelart sprite of Pikachu and Charizard, with an HP bar of their current health
        Health cannot exceed 255 or fall below 0.
    '''
    # set pokemon names to lowercase
    my_poke1 = my_poke1.lower()
    my_poke2 = my_poke2.lower()
    # set maximum health to integer value of each pokemon's health from data
    max_hp1 = int(pokemonData.loc[my_poke1].loc['hp'])
    max_hp2 = int(pokemonData.loc[my_poke2].loc['hp'])
    # set current health to an integer
    current_hp1 = int(current_hp1)
    current_hp2 = int(current_hp2)

    # check if current hps exceed max, and if so, set to max
    if current_hp1 > max_hp1:
        current_hp1 = max_hp1
    if current_hp2 > max_hp2:
        current_hp2 = max_hp2

    # check if current hps are negative, and if so, set to zero
    if current_hp1 < 0:
        current_hp1 = 0
    if current_hp2 < 0:
        current_hp2 = 0

    # create 2x2 figure for displaying pokemon and health
    fig, ax = plt.subplots(2,2, gridspec_kw={'height_ratios': [5,0.5]})
    # first column is first pokemon and its health bar
    ax[1,0].set(title = my_poke1.upper())
    # second column is second pokemon and its health bar
    ax[1,1].set(title = my_poke2.upper())

    # show pokemon from urls
    url1 = pokemonData.loc[my_poke1].loc['sprite_url']
    url2 = pokemonData.loc[my_poke2].loc['sprite_url']
    im1 = Image.open(requests.get(url1, stream=True).raw)
    im2 = Image.open(requests.get(url2, stream=True).raw)
    ax[0,0].imshow(im1)
    ax[0,1].imshow(im2)

    # display heart image
    heart = mpimg.imread('pokemon_heart.png')
    ax[1,0].imshow(heart, extent=(-13, -1, 0, 10))
    ax[1,1].imshow(heart, extent=(-13, -1, 0, 10))

    # turn off axes
    ax[0,0].axis('off')
    ax[0,1].axis('off')
    ax[1,0].axis('off')
    ax[1,1].axis('off')

    # set hp colors, green = full health
    hp_color1 = 'green'
    hp_color2 = 'green'

    # change hp colors based on percentage of current pokemon hp
    if current_hp1 <= max_hp1*0.5:
        hp_color1 = 'orange'
    if current_hp1 <= max_hp1*0.1:
        hp_color1 = 'red'
    if current_hp2 <= max_hp2*0.5:
        hp_color2 = 'orange'
    if current_hp2 <= max_hp2*0.1:
        hp_color2 = 'red'

    # health bars for both pokemon
    ax[1,0].axvspan(0, current_hp1, color = hp_color1)
    ax[1,1].axvspan(0, current_hp2, color = hp_color2)
    ax[1,0].axvspan(0, max_hp1, color = hp_color1, alpha = 0.25)
    ax[1,1].axvspan(0, max_hp2, color = hp_color2, alpha = 0.55)

    # add amount of remaining health
    ax[1,0].text(max_hp1 + 2, 1, f"{current_hp1}/{max_hp1}", fontsize = 14, color = hp_color1)
    ax[1,1].text(max_hp2 + 2, 1, f"{current_hp2}/{max_hp2}", fontsize = 14, color = hp_color2)

    fig.tight_layout()
    plt.show()
        
    return None
       
def readPokemonStats(pokemon, pokemon_name):
    """
    COMMENT THIS with function description, args, return, example
    """
    # COMMENT BELOW HERE TOO
    pokemon.pokemon_name = pokemon_name
    pokemon.potionCounter = 0
    pokemon.maxhp = int(pokemonData.loc[pokemon_name].loc['hp'])
    pokemon.hp = int(pokemon.maxhp)
    pokemon.attack = int(pokemonData.loc[pokemon_name].loc['attack'])
    pokemon.defense = int(pokemonData.loc[pokemon_name].loc['defense'])
    
def takeTurn(attackingPokemon, defendingPokemon):
    '''
    Allows users/players to choose/input the moves they want to use against their opponent's Pokemon.
    Prints amount of damage dealt, amount healed, and whether a Pokemon runs (thus ending the game).
    
    Args:
        attackingPokemon: instance of the pokemon class; the pokemon whose move the user/player inputs
        defendingPokemon: instance of the pokemon class; the pokemon "receiving" an attack, if attackingPokemon deals damage
    Returns:
        None
    Example:
        attackingPokemon = pikachu
        defendingPokemon = charmander
        Output: "pikachu, choose your move:
                - run
                - attack
                - potion"
        User Input: attack
        Output: "pikachu dealt 20 damage to charmander"
        
    '''
    # COMMENT THIS NONSSNESE:

    try:
        move = input(f"{attackingPokemon.pokemon_name.upper()}, choose your move:\n- run\n- attack\n- potion\n").lower()
        if move == "run":
            attackingPokemon.run(defendingPokemon)
            raise Exception("Game is over!")
        elif move == "attack":
            attackingPokemon.useAttack(defendingPokemon)
            print(f"{attackingPokemon.pokemon_name.upper()} dealt {attackingPokemon.damage} damage to {defendingPokemon.pokemon_name.upper()}.")
        elif move == "potion":
            attackingPokemon.usePotion()
            print(f"{attackingPokemon.pokemon_name.upper()} has {3 - attackingPokemon.potionCounter} potions left!")
        elif move == "clear output":
            # clears previous output
            clear(wait = False)
            raise ValueError
        else:
            print("Sorry! Please input a valid move. Your options are run, attack, and potion.")
            raise ValueError

    except ValueError:
        takeTurn(attackingPokemon, defendingPokemon)
        
player1pokemon = pokemon()
player2pokemon = pokemon()

while True:
    player1pokemon_name = input("Player 1, which Pokemon do you send into battle?\n(If you don't know any, we recommend Charmander, Squirtle, or Bulbasaur!)\n").lower()
    
    try:
        readPokemonStats(player1pokemon, player1pokemon_name)
        break
    except KeyError:
        print("That Pokemon doesn't exist! Please try again:")
        
while True:
    player2pokemon_name = input("Player 2, which Pokemon do you send into battle?\n(If you don't know any, we recommend Chikorita, Cyndaquil, or Totodile!)\n").lower()

    try:
        readPokemonStats(player2pokemon, player2pokemon_name)
        break
    except KeyError:
        print("That Pokemon doesn't exist! Please try again:")
    
turn = 0

while int(player1pokemon.hp) > 0 and int(player2pokemon.hp) > 0:
    display_pokemon(player1pokemon.pokemon_name, player1pokemon.hp, player2pokemon.pokemon_name, player2pokemon.hp)
    
    if turn % 2 == 0:
        takeTurn(player1pokemon, player2pokemon)
    else:
        takeTurn(player2pokemon, player1pokemon)
    turn += 1
    
if int(player1pokemon.hp) <= 0:
    print(f"{player1pokemon.pokemon_name.upper()} has fainted! Player 2 won.")
else:
    print(f"{player2pokemon.pokemon_name.upper()} has fainted! Player 1 won.")

display_pokemon(player1pokemon.pokemon_name, player1pokemon.hp, player2pokemon.pokemon_name, player2pokemon.hp)
