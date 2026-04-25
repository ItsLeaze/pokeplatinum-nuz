#include "macros/scrcmd.inc"
#include "res/text/bank/hearthome_city_southeast_house_2f.h"


    ScriptEntry HearthomeCitySoutheastHouse2F_AceTrainerF
    ScriptEntry HearthomeCitySoutheastHouse2F_Clefairy
    ScriptEntryEnd

HearthomeCitySoutheastHouse2F_AceTrainerF:
    NPCMessage HearthomeCitySoutheastHouse2F_Text_IHaveSomethingForYourPokemon
    End

HearthomeCitySoutheastHouse2F_BagIsFull:
    Common_MessageBagIsFull
    CloseMessage
    ReleaseAll
    End

HearthomeCitySoutheastHouse2F_Clefairy:
    PokemonCryAndMessage SPECIES_CLEFAIRY, HearthomeCitySoutheastHouse2F_Text_ClefairyCryPippi
    End

    .balign 4, 0
