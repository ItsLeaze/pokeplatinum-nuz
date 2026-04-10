#include "macros/btlanimcmd.inc"

L_0:
    LoadParticleResource 0, thunder_punch_spa
    Func_FadeBg FADE_BG_TYPE_BASE, 1, 0, 12, BATTLE_COLOR_BLACK
    CreateEmitter 0, 0, EMITTER_CB_SET_POS_TO_DEFENDER
    CreateEmitter 0, 2, EMITTER_CB_SET_POS_TO_DEFENDER
    PlaySoundEffectR SEQ_SE_DP_W085C
    PlayDelayedSoundEffectR SEQ_SE_DP_W085C, 3
    PlayDelayedSoundEffectR SEQ_SE_DP_W085C, 6
    PlayDelayedSoundEffectR SEQ_SE_DP_W085C, 9
    Func_FadeBattlerSprite BATTLE_ANIM_DEFENDER, 0, 2, BATTLE_COLOR_LIGHT_YELLOW1, 14, 0
    WaitForAllEmitters
    UnloadParticleSystem 0
    Func_FadeBg FADE_BG_TYPE_BASE, 1, 12, 0, BATTLE_COLOR_BLACK
    WaitForAnimTasks
    End
