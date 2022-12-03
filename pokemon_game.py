import numpy as np
import pandas as pd
import ipywidgets as widgets
import ipywidgets as widgets

import pandas as pd

pokemonData = pd.read_csv("pokemon.csv")
pokemonData = pokemonData[:10]

def on_button_clicked(Button, playerNum):
    with outputs[playerNum]:
        print(f"Player {playerNum+1} chose {Button.description}!")
        print(pokemonData.loc[pokemonData['name'] == Button.description])#['hp'].values[0])
        desiredPokemonNames.append(Button.description)
        readPokemonStats(player1pokemon, Button.description)
        
def readPokemonStats(pokemon, name):
    pokemon.name = name
    pokemon.potionCounter = 0
    pokemon.maxhp = pokemonData.loc[pokemonData['name'] == name]['hp'].values[0]
    pokemon.hp = pokemon.maxhp
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

#// let each player choose their pokemon //
#-- present all pokemon options, raise an error if player 2 chooses the same pokemon as player 1

#// gameplay loop //
#turn = 0
#while both pokemon have health:
#    if turn is even:
#        player1's turn
#    if turn is odd:
#        player2's turn
#    turn += 1
#
#print("game is over")
#if turn is even, then player 1 is dead?
#if turn is odd, then player 2 is dead?
#
#takeATurn(player):
#    present user with attack and heal butttons
#    if attack:
#        subtract health from enemy player equal to attack damage
#    if heal:
#        if pokemon.hp + 20 > maxhealth
#            raiseException
#        add 20 health to player's pokemon
