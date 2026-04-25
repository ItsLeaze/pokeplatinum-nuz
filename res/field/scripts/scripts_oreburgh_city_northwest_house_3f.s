#include "macros/scrcmd.inc"
#include "res/text/bank/oreburgh_city_northwest_house_3f.h"


    ScriptEntry OreburghCityNorthwestHouse3F_Lass
    ScriptEntry OreburghCityNorthwestHouse3F_Psyduck
    ScriptEntryEnd

OreburghCityNorthwestHouse3F_Lass:
    PlaySE SEQ_SE_CONFIRM
    LockAll
    FacePlayer
    GoTo OreburghCityNorthwestHouse3F_ThatItemIntensifiesThePowerOfRockTypeMoves
    ReleaseAll
    End

OreburghCityNorthwestHouse3F_ThatItemIntensifiesThePowerOfRockTypeMoves:
    BufferItemName 0, ITEM_HARD_STONE
    Message OreburghCityNorthwestHouse3F_Text_ThatItemIntensifiesThePowerOfRockTypeMoves
    WaitButton
    CloseMessage
    ReleaseAll
    End

OreburghCityNorthwestHouse3F_BagIsFull:
    Common_MessageBagIsFull
    CloseMessage
    ReleaseAll
    End

OreburghCityNorthwestHouse3F_Psyduck:
    PokemonCryAndMessage SPECIES_PSYDUCK, OreburghCityNorthwestHouse3F_Text_PsyduckDuuuck
    End

    .balign 4, 0
