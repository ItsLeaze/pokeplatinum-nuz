#include "macros/scrcmd.inc"
#include "res/text/bank/route_211_east.h"
#include "res/field/events/events_route_211_east.h"


    ScriptEntry Route211East_AceTrainerM
    ScriptEntry Route211East_ArrowSignMtCoronet
    ScriptEntry Route211East_TrainerTips
    ScriptEntry Route211East_ArrowSignCelesticTown
    ScriptEntry Route211East_CameraPeople
    ScriptEntry Route211East_Gardenia
    ScriptEntryEnd

Route211East_AceTrainerM:
    NPCMessage Route211East_Text_TheyAreFilming
    End

Route211East_ArrowSignMtCoronet:
    ShowArrowSign Route211East_Text_SignMtCoronet
    End

Route211East_TrainerTips:
    ShowScrollingSign Route211East_Text_TrainerTipsCheckSupply
    End

Route211East_ArrowSignCelesticTown:
    ShowArrowSign Route211East_Text_SignCelesticTown
    End

Route211East_CameraPeople:
    NPCMessage Route211East_Text_WeAreFilming
    End

Route211East_Gardenia:
    PlaySE SEQ_SE_CONFIRM
    LockAll
    FacePlayer
    BufferRivalName 0
    Message Route211East_Text_Gardenia
    CloseMessage
    GetPlayerMapPos VAR_0x8004, VAR_0x8005
    GoToIfEq VAR_0x8005, 526, Route211East_GardeniaLeaveLeftThenDown
    GoTo Route211East_GardeniaLeaveDirectlyDown
    End

Route211East_GardeniaLeaveDirectlyDown:
    ApplyMovement LOCALID_GARDENIA, Route211East_Movement_GardeniaLeaveDirectlyDown
    WaitMovement
    GoTo Route211East_GardeniaLeft
    End

Route211East_GardeniaLeaveLeftThenDown:
    ApplyMovement LOCALID_GARDENIA, Route211East_Movement_GardeniaLeaveLeftThenDown
    WaitMovement
    GoTo Route211East_GardeniaLeft
    End

Route211East_GardeniaLeft:
    RemoveObject LOCALID_GARDENIA
    SetFlag FLAG_TALKED_TO_GARDENIA
    ReleaseAll
    End

    .balign 4, 0
Route211East_Movement_GardeniaLeaveDirectlyDown:
    WalkFastSouth 6
    WalkFastWest 10
    EndMovement

    .balign 4, 0
Route211East_Movement_GardeniaLeaveLeftThenDown:
    WalkFastWest 1
    WalkFastSouth 6
    WalkFastWest 10
    EndMovement

    .balign 4, 0
