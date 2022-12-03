import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
import matplotlib.image as mpimg
import random

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
    try:
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
        
    except KeyError:
        print("wrong name")
