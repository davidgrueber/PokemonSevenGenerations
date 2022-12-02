import numpy as np
import pandas as pd
import ipywidgets as widgets
import ipywidgets as widgets

import pandas as pd

pokemonData = pd.read_csv("pokemon.csv")
pokemonData = pokemonData[:10]

class pokemon:
    def __init__(self):
        self.name = 'pokemon1'
        self.hp = 'health1'

def on_button_clicked(Button, playerNum):
    with outputs[playerNum]:
        print(f"Player {playerNum+1} chose {Button.description}!")
        print(pokemonData.loc[pokemonData['name'] == Button.description])#['hp'].values[0])
        desiredPokemonNames.append(Button.description)
        readPokemonStats(player1pokemon, Button.description)
        
def readPokemonStats(pokemon, name):
    pokemon.name = name
    pokemon.hp = pokemonData.loc[pokemonData['name'] == name]['hp'].values[0]
    pokemon.attack = pokemonData.loc[pokemonData['name'] == name]['attack'].values[0]
    pokemon.defense = pokemonData.loc[pokemonData['name'] == name]['defense'].values[0] 
    
buttons = [widgets.Button(description = name) for name in pokemonData["name"]]
outputs = [widgets.Output(), widgets.Output()]

player1pokemon = pokemon()
player2pokemon = pokemon()
players = [player1pokemon, player2pokemon]
desiredPokemonNames = []

for playerNum in range(len(players)):
    print(f"Player {playerNum+1}, please choose your Pokemon:")
    for option in range(len(buttons)):
        display(buttons[option])
        buttons[option].on_click(on_button_clicked(buttons[option], playerNum))
        readPokemonStats(players[playerNum], buttons[option].description)
    display(outputs[playerNum])

print(f"Player 1's pokemon has {player1pokemon.attack} attack points")
print(f"Player 2's pokemon has {player2pokemon.attack} attack points")
    #    buttons[option].on_click(on_button_clicked(buttons[option], players[playerNum]))
    #    print(buttons[option])
    #    display(output)
    
#print("Player 2, please choose your Pokemon:")
#for option in range(len(buttons)):
#    display(buttons[option])
#    buttons[option].on_click(on_button_clicked)
#display(output)
