# Chambered Steel

An accompanying website for a Buckshot Roulette-like card game.
Play it [here](https://shrub719.github.io/chambered-steel)!

## Usage

### Setup

The game requires you to have:

- Health counters (up to 5 per person)
- A deck of item cards to draw at the start of a round (I will upload mine whenever I find them)

### Starting

On start, the site begins a new game. At the start of the game, you are told:
- The number of lives/health each player has
- The number of items to draw
- The number of live shells, and the number of blank shells.

Tap to advance the game.

### In-game

Pass the device around between players.  
On their turn, a player can select an action if its corresponding card is played.  
The result of the action is then displayed.  
Some options, like `GLASS` and `PHONE`, should not be shown to other players.  
Lives are **red**; blanks are **blue**.

- `FIRE`: Fires the current shell, playing a sound. Tap the screen to fire.
- `EJECT`: Ejects the current shell, showing the polarity.
- `INVERT`: Inverts the polarity of the current shell in the chamber.
- `GLASS`: Shows the polarity of the next shell **without ejecting**.
- `PHONE`: Shows the polarity of a random shell at position three or later.
- `MEDICINE`: Flips a coin: randomly gives `+2 HEALTH` or `-1 HEALTH`.
- `END`: End the game early if only one player remains standing.

### Between games

After a game ends, the options very depending on whether there is one player standing
or play continues as normal.

- `NEXT ROUND`: New round, with new items and shells.
- `NEW GAME`: New game, with new items, shells and a **new number of lives/charges**.

