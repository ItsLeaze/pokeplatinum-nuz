#include "scrcmd_game_corner_prize.h"

#include <nitro.h>
#include <string.h>

#include "generated/items.h"

#include "field_script_context.h"
#include "inlines.h"

typedef struct GameCornerPrize {
    u16 item;
    u16 price;
} GameCornerPrize;

BOOL ScrCmd_GetGameCornerPrizeData(ScriptContext *ctx)
{
    u16 index = ScriptContext_GetVar(ctx);
    u16 *item = ScriptContext_GetVarPointer(ctx);
    u16 *price = ScriptContext_GetVarPointer(ctx);

    static const GameCornerPrize sGameCornerPrizeData[] = {
        { ITEM_QUICK_CLAW, 5000 },
        { ITEM_FOCUS_BAND, 10000 },
        { ITEM_BRIGHTPOWDER, 15000 },
        { ITEM_SCOPE_LENS, 20000 }
    };

    *item = sGameCornerPrizeData[index].item;
    *price = sGameCornerPrizeData[index].price;

    return FALSE;
}
