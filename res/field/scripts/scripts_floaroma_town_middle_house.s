#include "macros/scrcmd.inc"
#include "res/text/bank/floaroma_town_middle_house.h"


    ScriptEntry FloaromaTownMiddleHouse_PokemonBreederF
    ScriptEntry FloaromaTownMiddleHouse_Twin
    ScriptEntry FloaromaTownMiddleHouse_Clefairy
    ScriptEntryEnd

FloaromaTownMiddleHouse_PokemonBreederF:
    NPCMessage FloaromaTownMiddleHouse_Text_FloaromaTownWasABarrenDesolateHillLongAgo
    End

FloaromaTownMiddleHouse_Twin:
    NPCMessage FloaromaTownMiddleHouse_Text_DoYouThinkItsCuteHowPokemonPluckBerries
    End

FloaromaTownMiddleHouse_WhenAPokemonUsesPluckItEatsABerryHeldByItsFoe:
    Message FloaromaTownMiddleHouse_Text_WhenAPokemonUsesPluckItEatsABerryHeldByItsFoe
    WaitButton
    CloseMessage
    ReleaseAll
    End

FloaromaTownMiddleHouse_BagIsFull:
    Common_MessageBagIsFull
    CloseMessage
    ReleaseAll
    End

FloaromaTownMiddleHouse_Clefairy:
    PokemonCryAndMessage SPECIES_CLEFAIRY, FloaromaTownMiddleHouse_Text_ClefairyRii
    End
