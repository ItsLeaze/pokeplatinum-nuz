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

# 25 Add New-Gen Sturdy
Add the effect of modern-gen Sturdy to the Sturdy ability. Pokemon with the ability endure the hit with 1 HP if their HP would have been reduced from 100% to 0.
TO TEST: normal oh-ko; pokemon does not endure if it wasn't full HP; pokemon dies to multi-hit or poison; idk about Fissure/Sheer Cold; Future Sight; Pursuit

# 26 Make all default berries on patches useless
All the initial berries on patches have been replaced with ones that don't have an effect.
Make the Floaroma Berry NPC always give Bluk Berry.
Make the Berry Man at Route 208 always give 50 Sitrus Berries.

# 27 Make max. sleep and confusion turns 4 instead of 5
-"-

# 28 Update some items
Make Quick Claw activation chance 30% instead of 20%.
Make Metronome boost the power by 20% per turn instead of 10%.
Make Light Clay increase the number of Light Screen and Reflect turns from 5 turns to 10 turns instead of 8 turns.

# 29 Update some moves
Make Constrict speed lowering chance 100% and Power 40.
Make Wrap type Grass.
Make Cut type Grass.
Make Rock Climb type Rock.
Make Double Slap hit twice instead of 2-5 times.
Make Comet Punch type Steel.
Make Spike Cannon type Ground.
Make Covet type Fairy.
Make Charm type Fairy.
Make Moonlight type Fairy.
Make Sweet Kiss type Fairy.
Make Gravity last 7 turns instead of 5.

# 30 Add Fairy Type moves
Add Moonblast.
Add Disarming Voice.
Add Draining Kiss.
Add Play Rough.

# 31 Add more Moves
Add Bulldoze.
Add Volt Switch.
Note: There is some Pursuit-specific trainer AI `Expert_Pursuit_CheckUturn` that I haven't dared to adjust to volt switch yet.

# 32 Weather changes
Overworld weather conditions are set permanently and cannot be overwritten by moves or abilities.
Weather setting abilities set weather for five turns instead of permanently.
The overworld "weather" Trick Room sets a permanent trick room at the start of battle.
Trainer AI only uses weather setting moves on turn 1 and if no weather is already set.

# 33 Status condition changes
Chance to lose a turn to being fully paralyzed changed from 1/4 to 1/8.
Chance to thaw a frozen Pokemon changed from 1/5 to 1/2 per turn.
Chance to lose a turn to being infatuated changed from 1/2 to 1/3.
The Speed of a paralyzed Pokémon is decreased by 50% (as opposed to 75%).

# 34 Move changes
Bide now unleashes after one turn instead of two.
Safeguard lasts for 7 turns instead of 5.
Lucky Chant lasts for 7 turns instead of 5.

# 35 Don't revive dead pokemon when healing party
-"-

# 36 Increase Crit Stages by +1 when having 2+ fainted Pokemon in the Party
-"-

# 37 Implement flex-spots for tainers
Trainers can have alternative Pokemon for the slots 2-5. When defined, there is a 50% chance for slots 2-5 being replaced by slots 7-10.

# 38 Revive last Pokemon on party heal if all Pokemon fainted
This avoids the game bugging out after wiping and going into a fight with 0 mons alive.

# 39 Add more Moves
Add Nuzzle.
Add Dazzling Gleam
