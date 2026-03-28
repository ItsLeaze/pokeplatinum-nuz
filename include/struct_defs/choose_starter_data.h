#ifndef POKEPLATINUM_STRUCT_020425E0_H
#define POKEPLATINUM_STRUCT_020425E0_H

#include "game_options.h"

typedef struct ChooseStarterData {
    int species;
    u16 pokemon1;
    u16 pokemon2;
    u16 pokemon3;
    const Options *options;
} ChooseStarterData;

#endif // POKEPLATINUM_STRUCT_020425E0_H
