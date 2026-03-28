#include "macros/scrcmd.inc"
#include "res/text/bank/twinleaf_town_player_house_2f.h"
#include "res/field/events/events_twinleaf_town_player_house_2f.h"


    ScriptEntry TwinleafTownPlayerHouse2F_Wii
    ScriptEntry TwinleafTownPlayerHouse2F_PC
    ScriptEntry TwinleafTownPlayerHouse2F_OnFrame_ConcludeSpecialProgram
    ScriptEntry TwinleafTownPlayerHouse2F_ScrollingSign
    ScriptEntry TwinleafTownPlayerHouse2F_OnTransition
    ScriptEntry TwinleafTownPlayerHouse2F_TV
    ScriptEntryEnd

TwinleafTownPlayerHouse2F_OnTransition:
    GoToIfEq VAR_PLAYER_HOUSE_SPECIAL_PROGRAM_STATE, 0, TwinleafTownPlayerHouse2F_SetVolumeForTV
    End

TwinleafTownPlayerHouse2F_SetVolumeForTV:
    SetInitialVolumeForSequence SEQ_TV_HOUSOU, 50
    End

TwinleafTownPlayerHouse2F_OnFrame_ConcludeSpecialProgram:
    LockAll
    SetVar VAR_PLAYER_HOUSE_SPECIAL_PROGRAM_STATE, 1
    Message TwinleafTownPlayerHouse2F_Text_ThatConcludesOurSpecialProgram
    PlayFanfare SEQ_TV_END
    Message TwinleafTownPlayerHouse2F_Text_SeeYouNextWeek
    WaitFanfare
    CloseMessage
    PlayDefaultMusic
    ReleaseAll
    End

TwinleafTownPlayerHouse2F_Wii:
    EventMessage TwinleafTownPlayerHouse2F_Text_ItsAWii
    End

TwinleafTownPlayerHouse2F_PC:
    PlaySE SEQ_SE_CONFIRM
    LockAll
    BufferPlayerName 0
    Message TwinleafTownPlayerHouse2F_Text_PCPokemonBasics
    WaitButton
    CloseMessage
    ReleaseAll
    End

TwinleafTownPlayerHouse2F_ScrollingSign:
    ShowScrollingSign TwinleafTownPlayerHouse2F_Text_TheXButtonOpensTheMenu
    End

TwinleafTownPlayerHouse2F_TV:
    EventMessage TwinleafTownPlayerHouse2F_Text_MomBoughThisTVAsAGift
    End
