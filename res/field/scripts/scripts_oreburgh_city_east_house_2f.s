#include "macros/scrcmd.inc"
#include "res/text/bank/oreburgh_city_east_house_2f.h"


    ScriptEntry OreburghCityEastHouse2F_Gentleman
    ScriptEntry OreburghCityEastHouse2F_Youngster
    ScriptEntry OreburghCityEastHouse2F_Unused
    ScriptEntry OreburghCityEastHouse2F_ScientistM
    ScriptEntryEnd

OreburghCityEastHouse2F_Gentleman:
    NPCMessage OreburghCityEastHouse2F_Text_TheOreburghMineIsOperatedWithTheUtmostCare
    End

OreburghCityEastHouse2F_Youngster:
    NPCMessage OreburghCityEastHouse2F_Text_HereIWantYouToHaveThis
    End

OreburghCityEastHouse2F_YouKnowHowPokemonStayInsideTheirPokeBalls:
    Message OreburghCityEastHouse2F_Text_YouKnowHowPokemonStayInsideTheirPokeBalls
    WaitButton
    CloseMessage
    ReleaseAll
    End

OreburghCityEastHouse2F_BagIsFull:
    Common_MessageBagIsFull
    CloseMessage
    ReleaseAll
    End

OreburghCityEastHouse2F_Unused:
    End

OreburghCityEastHouse2F_ScientistM:
    NPCMessage OreburghCityEastHouse2F_Text_CoalIsCarriedOutOfTheOreburghMineOnAFullyAutomatedSystem
    End

    .balign 4, 0
