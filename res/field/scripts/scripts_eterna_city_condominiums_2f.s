#include "macros/scrcmd.inc"
#include "res/text/bank/eterna_city_condominiums_2f.h"


    ScriptEntry EternaCityCondominiums2F_ExpertF
    ScriptEntry EternaCityCondominiums2F_Twin
    ScriptEntry EternaCityCondominiums2F_ExpertM
    ScriptEntryEnd

EternaCityCondominiums2F_ExpertF:
    NPCMessage EternaCityCondominiums2F_Text_IveHadThisTMRecycleForSuchALongTimeNow
    End

EternaCityCondominiums2F_BagIsFull:
    Common_MessageBagIsFull
    CloseMessage
    ReleaseAll
    End

EternaCityCondominiums2F_FolksLikeMeHaveALongHistoryWeCanLookBackOn:
    Message EternaCityCondominiums2F_Text_FolksLikeMeHaveALongHistoryWeCanLookBackOn
    WaitButton
    CloseMessage
    ReleaseAll
    End

EternaCityCondominiums2F_Twin:
    NPCMessage EternaCityCondominiums2F_Text_GardeniaOurGymLeaderGoesOutToEternaForestEverySoOften
    End

EternaCityCondominiums2F_ExpertM:
    NPCMessage EternaCityCondominiums2F_Text_TheMoveRecycleIsToBeUsedDuringBattle
    End

    .balign 4, 0
