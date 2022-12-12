# README

**Pokémon: Seven Generations**

Contributors: Sarayna Gandhi, David Grueber, Dylan Fox

# Game Description
Two players choose any Pokemon or its evolution from all seven generations (as included in Kaggle's "The Complete Pokemon Dataset"), then engage in a turn-based battle against each other. On any given turn, a player may run away (quit), use a healing potion to add 20 health, or attack the opposing player's Pokemon. An attacking Pokemon attempts to deal damage to a defending Pokemon equal to its basic attack value times a random multiplier between .1 and .7; the defending Pokemon successfully defends an amount of damage equal to its basic defense value times a random multiplier between .1 and .5, to ensure the game is engaging and not entirely pre-determined by choice of Pokemon. The game ends when a Pokemon either runs away (i.e. quits) or makes it to zero health points.

# List of Python packages used and their versions (e.g. numpy 1.21.5). 
- numpy version 1.21.5
- pandas version 1.4.2
- PIL version 9.3.0
- requests version 2.27.1
- matplotlib version 3.5.1
- IPython version 8.7.0
- copy and random packages (couldn't find their individual package versions, we think they're just included with Python version 3.11.12)

# Detailed description of the demo file. 
To run our demo file, called "pokemon_demo.ipynb", download the PokemonSevenGenerations zip file from GitHub. Open pokemon_demo.ipynb in Jupyter, and follow the instructions in the first cell to import the start_battle() function from the included pokemon_game.py file. Start the game by then calling the start_battle() function in its own cell (without any arguments). The two human players will first be prompted to enter their choice of Pokemon, after which the gameplay loop begins. During each turn, the game prompts one of the players for an action, as pictured here:

<img width="418" alt="Screen Shot 2022-12-11 at 10 30 02 PM" src="https://user-images.githubusercontent.com/114404654/206976579-003db6b7-00eb-42b3-a7f7-42fe495ac6e2.png">

Once the player makes an input, the game prints an image of each Pokemon and their health, as visualized by a health bar, at which point the turn is over. This output will look like this:

<img width="440" alt="Screen Shot 2022-12-11 at 10 32 51 PM" src="https://user-images.githubusercontent.com/114404654/206976973-a4fd8fd3-d34f-4af8-9bda-00a5da9a08d3.png">

The game will repeat the above process, continually prompting a player for an input and printing the appropriate health bar changes (and Pokemon images) until a Pokemon either dies or runs away.

# Scope and limitations, including ethical implications, accessibility concerns, and ideas for potential extensions.
The scope of this project was to implement a basic Pokemon battler using "real" data on Pokemon, published online. This game can be used for entertainment/nostalgia purposes, as it was designed to mimic old Nintendo games, or even as an educational tool to demonstrate introductory computer programming principles (and also Python syntax), such as inheritance and control flow constructions. Since we don't plan on commercializing, and this project was created for educational purposes, we believe it is ethical to publish it for the public to examine and use. On a conceptual level, our Pokemon game is the same as these old Nintendo games--a 1v1 turn-based battle. However, in the actual implementation of our game, it is much simpler than the Nintendo games of old: each player chooses only one Pokemon, instead of three; each Pokemon is equally effective against Pokemon of all types, instead of being especially powerful against or vulnerable to certain Pokemon types; and each Pokemon has one attack option, instead of multiple attacks each with different potetial abilities. Each of these features present good opportunities for potential extensions of our game. We would also like to implement clickable buttons in place of the default Python input() text box. In terms of accessibility, the one major barier to playing our game is that it must be run on JupyterNotebook or JupyterLab (and the zip file must be downloaded, of course). It can be used for free, and doesn't require any previous knowledge of Pokemon or of Python to play.

# References and acknowledgement.
We would like to acknowledge Nintendo for many years of entertainment! We would also like to acknowledge the Python Maraton YouTube channel, whose video (at https://www.youtube.com/watch?v=Pbs6jQZrZA4) we watched for inspiration. No code was copied or otherwise taken from their video. We would also like to thank Professor Harlin Lee and our TAs for their patient and inspiring teaching!

# (If appropriate) background and source of the dataset.
Sprite images: https://github.com/yaylinda/pokemon-sprite-scraper/blob/master/metadata.csv

Pokemon data: https://www.kaggle.com/datasets/rounakbanik/pokemon
