# Chambered Steel

An accompanying program for a Buckshot-Roulette-like card game.

## Usage

On start, the program begins a new game. At the start of the game, you are told:
- The number of lives/charges each player has
- The number of items to draw
- The number of live shells, and the number of blank shells.

Hit `Enter` to advance the game.

### In-game

Pass the device around between players.  
On their turn, a player can select an action by typing in its menu number and pressing `Enter`. 
The result of the action is then displayed.  
Some commands, like `GLASS` and `PHONE`, require the player to press `Enter` again to clear the screen before passing 
to the next player.

Commands beginning with `!` are not in-game actions, but special game master commands.

0. `FIRE`: Fires the current shell, showing the polarity and playing a sound.
1. `EJECT`: Ejects the current shell, showing the polarity.
2. `INVERTER`: Inverts the polarity of the current shell in the chamber.
3. `GLASS`: Shows the polarity of the next shell **without ejecting**.
4. `PHONE`: Shows the polarity of a random shell at position three or later.
5. `MEDICINE`: Flips a coin: randomly prints `+2 HEALTH` or `-1 HEALTH`.
6. `UNDO`: Undoes the last action that changed the shell order in case of mistakes.
7. `END`: End the game early if only one player remains standing.
8. `! SHELL COUNT`: Shows the number of shells left in the gun.
9. `! SHOW`: Shows the number of lives and the number of blanks left in the gun.
10. `! FULL VIEW`: Shows the order of shells left in the gun.


### Between games

After a game ends, the options very depending on whether there is one player standing
or play continues as normal.

0. `NEXT ROUND`: New round, with new items and shells.
1. `NEW GAME`: New game, with new items, shells and a **new number of lives/charges**.
2. `EXIT`: Quit the program.
