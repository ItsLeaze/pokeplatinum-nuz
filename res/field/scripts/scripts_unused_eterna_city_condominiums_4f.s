#include "macros/scrcmd.inc"
#include "res/text/bank/unused_eterna_city_condominiums_4f.h"


    ScriptEntry EternaCityCondominiums4F_ExpertF
    ScriptEntryEnd

EternaCityCondominiums4F_ExpertF:
    PlaySE SEQ_SE_CONFIRM
    LockAll
    FacePlayer
    GoTo EternaCityCondominiums4F_FolksLikeMeHaveALongHistoryWeCanLookBackOn
    CloseMessage
    ReleaseAll
    End

EternaCityCondominiums4F_FolksLikeMeHaveALongHistoryWeCanLookBackOn:
    Message EternaCityCondominiums4F_Text_FolksLikeMeHaveALongHistoryWeCanLookBackOn
    WaitButton
    CloseMessage
    ReleaseAll
    End

EternaCityCondominiums4F_BagIsFull:
    Common_MessageBagIsFull
    CloseMessage
    ReleaseAll
    End
