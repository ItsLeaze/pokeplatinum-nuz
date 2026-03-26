#include "type_icon.h"

#include <nitro.h>
#include <string.h>

#include "constants/narc.h"
#include "generated/move_classes.h"

#include "pch/global_pch.h"

#include "palette.h"
#include "sprite_system.h"

ALIGN_4 static const u32 sMoveTypeIconIndex[] = {
    0xEA, // NORMAL (0 to 18 are pokemon types)
    0xE1, // FIGHT
    0xE3, // FLYING
    0xEB, // POISON
    0xE5, // GROUND
    0xED, // ROCK
    0xE7, // BUG
    0xE4, // GHOST
    0xEE, // STEEL
    0xEC, // MYSTERY
    0xE2, // FIRE
    0xF1, // WATER
    0xE9, // GRASS
    0xDE, // ELECTRIC
    0xDF, // PSYCHIC
    0xE6, // ICE
    0xDD, // DRAGON
    0xE0, // DARK
    0x157, // FAIRY
    0xF0, // 19 to 22 are contest types
    0xDB,
    0xDC,
    0xE8,
    0xEF
};

ALIGN_4 static const u8 sMoveTypeIconPaletteIndex[] = {
    0x0, // NORMAL // 0 to 18 are pokemon types
    0x0, // FIGHT
    0x1, // FLYING
    0x1, // POISON
    0x0, // GROUND
    0x0, // ROCK
    0x2, // BUG
    0x1, // GHOST
    0x0, // STEEL
    0x2, // MYSTERY
    0x0, // FIRE
    0x1, // WATER
    0x2, // GRASS
    0x0, // ELECTRIC
    0x1, // PSYCHIC
    0x1, // ICE
    0x2, // DRAGON
    0x0, // DARK
    0x1, // FAIRY
    0x0, // 19 to 22 are contest types
    0x1,
    0x1,
    0x2,
    0x0
};

ALIGN_4 static const u32 sMoveCategoryIconIndex[] = {
    0xF4,
    0xF6,
    0xF5
};

ALIGN_4 static const u8 sMoveCategoryIconPaletteIndex[] = {
    0x0,
    0x1,
    0x0
};

u32 TypeIcon_GetChar(enum PokemonType moveType)
{
    GF_ASSERT(moveType < NELEMS(sMoveTypeIconIndex));
    return sMoveTypeIconIndex[moveType];
}

u32 TypeIcon_GetPlttSrc(void)
{
    return 74;
}

u32 TypeIcon_GetCell(void)
{
    return 242;
}

u32 TypeIcon_GetAnim(void)
{
    return 243;
}

u8 TypeIcon_GetPltt(enum PokemonType moveType)
{
    GF_ASSERT(moveType < NELEMS(sMoveTypeIconPaletteIndex));
    return sMoveTypeIconPaletteIndex[moveType];
}

enum NarcID TypeIcon_GetNARC(void)
{
    return NARC_INDEX_BATTLE__GRAPHIC__PL_BATT_OBJ;
}

void TypeIcon_LoadChar(SpriteSystem *spriteSys, SpriteManager *spriteMan, NNS_G2D_VRAM_TYPE vramType, enum PokemonType moveType, u32 resourceID)
{
    SpriteSystem_LoadCharResObj(spriteSys, spriteMan, TypeIcon_GetNARC(), TypeIcon_GetChar(moveType), TRUE, vramType, resourceID);
}

void TypeIcon_LoadPlttSrc(SpriteSystem *spriteSys, SpriteManager *spriteMan, NNS_G2D_VRAM_TYPE vramType, u32 resourceID)
{
    SpriteSystem_LoadPlttResObj(spriteSys, spriteMan, TypeIcon_GetNARC(), TypeIcon_GetPlttSrc(), FALSE, PLTT_3, vramType, resourceID);
}

void TypeIcon_LoadPltt(PaletteData *paletteData, enum PaletteBufferID bufferID, SpriteSystem *spriteSys, SpriteManager *spriteMan, NNS_G2D_VRAM_TYPE vramType, u32 resourceID)
{
    SpriteSystem_LoadPaletteBuffer(paletteData, bufferID, spriteSys, spriteMan, TypeIcon_GetNARC(), TypeIcon_GetPlttSrc(), FALSE, PLTT_3, vramType, resourceID);
}

void TypeIcon_LoadAnim(SpriteSystem *spriteSys, SpriteManager *spriteMan, u32 cellResourceID, u32 animResourceID)
{
    SpriteSystem_LoadCellResObj(spriteSys, spriteMan, TypeIcon_GetNARC(), TypeIcon_GetCell(), TRUE, cellResourceID);
    SpriteSystem_LoadAnimResObj(spriteSys, spriteMan, TypeIcon_GetNARC(), TypeIcon_GetAnim(), TRUE, animResourceID);
}

void TypeIcon_UnloadChar(SpriteManager *spriteMan, u32 resourceID)
{
    SpriteManager_UnloadCharObjById(spriteMan, resourceID);
}

void TypeIcon_UnloadPlttSrc(SpriteManager *spriteMan, u32 resourceID)
{
    SpriteManager_UnloadPlttObjById(spriteMan, resourceID);
}

void TypeIcon_UnloadAnim(SpriteManager *spriteMan, u32 cellResourceID, u32 animResourceID)
{
    SpriteManager_UnloadCellObjById(spriteMan, cellResourceID);
    SpriteManager_UnloadAnimObjById(spriteMan, animResourceID);
}

ManagedSprite *TypeIcon_NewTypeIconSprite(SpriteSystem *spriteSys, SpriteManager *spriteMan, enum PokemonType moveType, const SpriteTemplate *spriteTemplate)
{
    ManagedSprite *managedSprite;
    SpriteTemplate template;

    template = *spriteTemplate;
    template.plttIdx = TypeIcon_GetPltt(moveType);
    managedSprite = SpriteSystem_NewSprite(spriteSys, spriteMan, &template);

    return managedSprite;
}

void TypeIcon_DeleteSprite(ManagedSprite *managedSprite)
{
    Sprite_DeleteAndFreeResources(managedSprite);
}

u32 CategoryIcon_GetChar(enum MoveClass moveCat)
{
    GF_ASSERT(moveCat < NELEMS(sMoveCategoryIconIndex));
    return sMoveCategoryIconIndex[moveCat];
}

u8 CategoryIcon_GetPltt(enum MoveClass moveCat)
{
    GF_ASSERT(moveCat < NELEMS(sMoveCategoryIconPaletteIndex));
    return sMoveCategoryIconPaletteIndex[moveCat];
}

enum NarcID CategoryIcon_GetNARC(void)
{
    return NARC_INDEX_BATTLE__GRAPHIC__PL_BATT_OBJ;
}

void CategoryIcon_LoadChar(SpriteSystem *spriteSys, SpriteManager *spriteMan, NNS_G2D_VRAM_TYPE vramType, enum MoveClass moveCat, u32 resourceID)
{
    SpriteSystem_LoadCharResObj(spriteSys, spriteMan, CategoryIcon_GetNARC(), CategoryIcon_GetChar(moveCat), TRUE, vramType, resourceID);
}

void CategoryIcon_UnloadChar(SpriteManager *spriteMan, u32 resourceID)
{
    SpriteManager_UnloadCharObjById(spriteMan, resourceID);
}

void CategoryIcon_DeleteSprite(ManagedSprite *managedSprite)
{
    Sprite_DeleteAndFreeResources(managedSprite);
}
