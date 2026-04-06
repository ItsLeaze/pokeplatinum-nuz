#include "macros/btlanimcmd.inc"

L_0:
    LoadParticleResource 0, submission_spa
    LoadParticleResource 1, comet_punch_spa
    Func_FadeBg FADE_BG_TYPE_BASE, 1, 0, 8, BATTLE_COLOR_LIGHT_RED
    Func_Submission 8, 10, BATTLE_ANIM_ATTACKER
    Func_Submission 8, 10, BATTLE_ANIM_DEFENDER
    CreateEmitter 0, 0, EMITTER_CB_SET_POS_TO_DEFENDER
    CreateEmitter 0, 1, EMITTER_CB_SET_POS_TO_DEFENDER
    PlayDelayedSoundEffectL SEQ_SE_DP_W104, 1
    PlayDelayedSoundEffectR SEQ_SE_DP_W025B, 10
    PlayDelayedSoundEffectL SEQ_SE_DP_W104, 10
    PlayDelayedSoundEffectR SEQ_SE_DP_W025B, 20
    PlayDelayedSoundEffectL SEQ_SE_DP_W104, 20
    PlayDelayedSoundEffectR SEQ_SE_DP_W025B, 30
    PlayDelayedSoundEffectL SEQ_SE_DP_W104, 30
    PlayDelayedSoundEffectR SEQ_SE_DP_W025B, 40
    PlayDelayedSoundEffectL SEQ_SE_DP_W104, 40
    PlayDelayedSoundEffectR SEQ_SE_DP_W025B, 50
    PlayDelayedSoundEffectL SEQ_SE_DP_W104, 50
    PlayDelayedSoundEffectR SEQ_SE_DP_W025B, 60
    PlayDelayedSoundEffectL SEQ_SE_DP_W104, 60
    PlayDelayedSoundEffectR SEQ_SE_DP_W025B, 70
    BeginLoop 5
    Delay 8
    CreateEmitter 1, 0, EMITTER_CB_SET_POS_TO_DEFENDER
    EndLoop
    WaitForAllEmitters
    UnloadParticleSystem 0
    UnloadParticleSystem 1
    Func_FadeBg FADE_BG_TYPE_BASE, 1, 8, 0, BATTLE_COLOR_LIGHT_RED
    WaitForAnimTasks
    End
