# Chambered Steel

An accompanying website for a Buckshot Roulette-like card game.
Play it [here](https://shrub719.github.io/chambered-steel)!

## Usage

### Setup

The game requires you to have:

- Health counters (up to 5 per person)
- A deck of item cards to draw at the start of a round
    - The recommended deck is 4 of each card in `cards/`

### Starting

On start, the site begins a new game. At the start of the game, you are told:
- The number of lives/health each player has
- The number of items to draw per player
- The number of live shells, and the number of blank shells

Distribute health counters to players and deal
the required number of item cards face up in front of each player.  
Players with more than 8 item cards should discard until they have 8.

Tap to begin the round.

### In-game

Players take turns holding the gun. On their turn, 
they can play item cards with certain effects before shooting themselves or another
player.  
If they have shot themselves with a blank, it remains their turn. Otherwise
play continues.  
Anybody shot with a live shell loses 1 health; reaching 0 health eliminates
you, until a **new game** (not round) is started. Health cannot go above
the current maximum when using healing items.  

Pass the device around to the player currently taking their turn.  
The options on the site allow for the player to apply and view the effects of
certain items, or to fire the gun. Some options should not be shown to other players when used. These are marked with a 👁️.  
Lives are **red**; blanks are **blue**.

- `FIRE`: Fires the current shell, playing a sound. Tap the screen to fire.
- `EJECT`: Ejects the current shell, showing the polarity.
- `INVERT`: Inverts the polarity of the current shell in the chamber.
- `GLASS`: 👁️ Shows the polarity of the next shell **without ejecting**.
- `PHONE`: 👁️ Shows the polarity of a random shell at position three or later.
- `MEDICINE`: Flips a coin: randomly gives `+2 HEALTH` or `-1 HEALTH`.
- `HISTORY`: Displays a game log, used for administration.
- `END`: End the game early if only one player remains standing.

### Between games

After a game ends, the options very depending on whether there is one player standing
or play continues as normal.

- `NEXT ROUND`: New round, with new items and shells.
- `NEW GAME`: New game, with new items, shells and a **new number of lives/charges**.

