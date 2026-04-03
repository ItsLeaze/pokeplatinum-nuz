# Changelog

## 1 Shortcut the Rowan Intro
Some steps of the Rowan Intro are now skipped.

## 2 Add Fairy Type
Fairy Type was added and can now be assigned to Pokemon and moves.
It was also added to the Poketch Move-Tester.

## 3 Update Type Effectiveness to Gen6
The type effectiveness has been updated to Gen6.

## 4 Allow setting opposing Trainer Pokemon natures
The nature can now be explicitly set in the trainer json files.

## 5 Make HMs forgettable
HM moves can now be forgotten.

## 6 Make TMs reusable
TMs no longer disappear after using them.

## 7 Remove necessity for Pokemon having HM moves for field effects
Instead, a the player can always perform field moves, no matter the Party.

## 8 Add IV display in summary and mark nature affinities in stats
In the stats page of a Pokemon's summary, you can now press A to toggle between stats and IVs.
Stats decreased by the nature are also marked red, increased stats are marked blue.

# 9 Add possibility to explicitly set ability on Trainer Pokemon
The ability can now explicitly be set in the trainer json files (selecting out of the Pokemon's abilities).
Also, the "power" property can now be omitted, setting it to 255 by default (all 31 IVs).

# 10 Add Running Shoes from the start of the game
The player can now run right from the start of a new game.

# 11 Set Battle Style Set and Fast Text as default options
-"-

# 12 Set Critical Hit Multiplier to 1.5 instead of 2
A critical strike now does (baseDamage*150)/100 damage.
Sniper Crits do 225% damage.

# 13 Double HP bar speed
The HP bar now moves twice as fast.

# 14 Remove EV gains from battles and vitamins
-"-

# 15 Shorten Start Story
The start story was shortened (WIP for testing)

# 16 Add possibility for custom starter selection
This allows for multiple briefcases with a selection of three custom Pokemon in the game.

# 17 Limit the encounters per route to 1 AND allow received eggs to go to the box if the party is full
**TODO: test thoroughly with wild, double and trainer battles**

A wild battle will now only be started if the player has not previously encountered a wild pokemon in the same location, going by the location's name.
When the player receives an egg (e.g. from Cynthia), it will be transferred to the box if the party is full.

# 18 Avoid duplicate encounters; defensively check for duplicates before setting a location as encountered
**TODO: test thoroughly with wild, double, honey, radar, safari and trainer battles**

A wild battle will now only be started if it has Pokemon the player hasn't yet captured.

# 19 Auto-Heal before every Battle
Auto-Heal all involved parties before every battle.

# 20 Fix Dupe Checking to consider evolutionary trees
**TODO: run test with all pokemon and caught states (especially complex trees like Evee)**

Now, an encounter is counted as a duplicate if the player has previously caught any Pokemon in the same evolutionary tree of the encountered Pokemon.
In a double battle, both wild Pokemon have to be a duplicate for the battle to be avoided.

# 21 Add Mobile Box Item
**TODO: test with actual item received at start of game**

**TODO: test in different locations (especially E4, where it must not work)**

There is now an item allowing the player to access the PCBox and move Pokemon from anywhere except the Elite 4.

# 22 Replace Battle Style Option with Nuzlocke Enable/Disable Option
Instead of the Battle Style Option, there is now an option to enable/disable nuzlocke QOL Features like dupe filtering and encounter limiting.
Battle Style is now always SET. By default, nuzlocke features are disabled.

# 23 Add hard-coded level cap
When a pokemon would level up above the level of the next gym leader, it's EXP is limited to 1 EXP below that level-up threshold.

# 24 Add a Cap Candy item and give after starter selection
The player is now given a cap candy item after the starter selection. The cap candy item is not removed on use and levels up the selected pokemon until it either:
- learns the next move
- evolves or
- reaches the level cap

The player is also given the Mobile box item and Pokeballs after the starter selection.

# 23 Add New-Gen Sturfy
Add the effect of modern-gen Sturdy to the Sturdy ability. Pokemon with the ability endure the hit with 1 HP if their HP would have been reduced from 100% to 0.
TO TEST: normal oh-ko; pokemon does not endure if it wasn't full HP; pokemon dies to multi-hit or poison; idk about Fissure/Sheer Cold; Future Sight; Pursuit
