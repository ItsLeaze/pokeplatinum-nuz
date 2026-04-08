#include "macros/btlcmd.inc"


_000:
    UpdateVar OPCODE_FLAG_ON, BTLVAR_SIDE_CONDITIONS_ATTACKER, SIDE_CONDITION_LUCKY_CHANT_INIT
    // The Lucky Chant shielded your team from critical hits!
    PrintMessage BattleStrings_Text_TheLuckyChantShieldedYourTeamFromCriticalHits, TAG_NONE_SIDE_CONSCIOUS, BTLSCR_ATTACKER
    Wait 
    WaitButtonABTime 30
    End 
