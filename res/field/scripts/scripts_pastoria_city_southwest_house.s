#include "macros/scrcmd.inc"
#include "res/text/bank/pastoria_city_southwest_house.h"


    ScriptEntry PastoriaCitySouthwestHouse_PokemonBreederF
    ScriptEntry PastoriaCitySouthwestHouse_Twin
    ScriptEntryEnd

PastoriaCitySouthwestHouse_PokemonBreederF:
    PlaySE SEQ_SE_CONFIRM
    LockAll
    FacePlayer
    GoTo PastoriaCitySouthwestHouse_PlantingIsGood
    End

PastoriaCitySouthwestHouse_PlantingIsGood:
    Message PastoriaCitySouthwestHouse_Text_PlantingIsGood
    WaitButton
    CloseMessage
    ReleaseAll
    End

PastoriaCitySouthwestHouse_BagIsFull:
    Common_MessageBagIsFull
    CloseMessage
    ReleaseAll
    End

PastoriaCitySouthwestHouse_Twin:
    NPCMessage PastoriaCitySouthwestHouse_Text_SisterGathersBerries
    End

    .balign 4, 0
