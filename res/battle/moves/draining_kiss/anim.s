#include "macros/btlanimcmd.inc"

L_0:
    LoadParticleResource 0, lovely_kiss_spa
    LoadParticleResource 1, drain_punch_spa
    CreateEmitter 0, 0, EMITTER_CB_SET_POS_TO_DEFENDER
    CreateEmitter 0, 1, EMITTER_CB_SET_POS_TO_DEFENDER
    Delay 10
    Func_FadeBg FADE_BG_TYPE_BASE, 1, 0, 8, BATTLE_COLOR_LIGHT_RED
    PlaySoundEffectR SEQ_SE_DP_W213
    Delay 5
    Func_Shake 1, 0, 1, 2, BATTLE_ANIM_BATTLER_SPRITE_DEFENDER
    Delay 10
    CreateEmitter 1, 2, EMITTER_CB_GENERIC
    SetExtraParams 0, 2, 2, 0, 0, 0
    CreateEmitter 1, 1, EMITTER_CB_GENERIC
    SetExtraParams 0, 2, 2, 1, 16, 0
    SetExtraParams 2, 0, 0, 0, 0
    Delay 5
    PlayLoopedSoundEffectC SEQ_SE_DP_W152, 2, 16
    Func_FadeBattlerSprite BATTLE_ANIM_ATTACKER, 0, 1, BATTLE_COLOR_WHITE, 10, 0
    WaitForAllEmitters
    UnloadParticleSystem 0
    UnloadParticleSystem 1
    Func_FadeBg FADE_BG_TYPE_BASE, 1, 8, 0, BATTLE_COLOR_LIGHT_RED
    WaitForAnimTasks
    End
