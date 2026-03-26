#include "macros/scrcmd.inc"
#include "res/text/bank/twinleaf_town_player_house_2f.h"


    ScriptEntry _005D
    ScriptEntry _006E
    ScriptEntry _0041
    ScriptEntry _0082
    ScriptEntry _002A
    ScriptEntry _0097
    ScriptEntryEnd

_002A:
    GoToIfEq VAR_UNK_0x40F9, 0, _0039
    End

_0039:
    SetInitialVolumeForSequence SEQ_TV_HOUSOU, 50
    End

_0041:
    LockAll
    SetVar VAR_UNK_0x40F9, 1
    Message 0
    PlaySound SEQ_TV_END
    Message 1
    WaitSound
    CloseMessage
    PlayDefaultMusic
    ReleaseAll
    End

_005D:
    PlayFanfare SEQ_SE_CONFIRM
    LockAll
    Message 4
    WaitABXPadPress
    CloseMessage
    ReleaseAll
    End

_006E:
    PlayFanfare SEQ_SE_CONFIRM
    LockAll
    BufferPlayerName 0
    Message 5
    WaitABXPadPress
    CloseMessage
    ReleaseAll
    End

_0082:
    ShowScrollingSign 3
    End

_0097:
    PlayFanfare SEQ_SE_CONFIRM
    LockAll
    Message 2
    WaitABXPadPress
    CloseMessage
    ReleaseAll
    End
