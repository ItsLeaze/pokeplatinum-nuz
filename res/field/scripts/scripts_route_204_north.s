#include "macros/scrcmd.inc"
#include "res/text/bank/route_204_north.h"


    ScriptEntry Route204North_Youngster
    ScriptEntry Route204North_AceTrainerF
    ScriptEntry Route204North_ArrowSignpostFloaromaTown
    ScriptEntryEnd

Route204North_Youngster:
    NPCMessage Route204North_Text_AreYouRaisingDifferentKindsOfPokemon
    End

Route204North_AceTrainerF:
    NPCMessage Route204North_Text_CaptivateOnlyWorksAgainstTheOppositeGender
    End

Route204North_BagIsFull:
    Common_MessageBagIsFull
    CloseMessage
    ReleaseAll
    End

Route204North_ArrowSignpostFloaromaTown:
    ShowArrowSign Route204North_Text_Rt204FloaromaTown
    End

    .balign 4, 0
