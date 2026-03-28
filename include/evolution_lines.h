#ifndef POKEPLATINUM_EVOLUTION_LINES_H
#define POKEPLATINUM_EVOLUTION_LINES_H

#include <nitro.h>

#include "constants/species.h"

#include "struct_defs/species.h"

#include "species.h"

#define MAX_EVOLUTION_TREE_SIZE 8

typedef struct EvolutionGraph {
    u16 adj[MAX_SPECIES][MAX_EVOLUTIONS];
    u8 adjSize[MAX_SPECIES];
} EvolutionGraph;

EvolutionGraph *EvolutionGraph_New(u32 heapID);
void EvolutionGraph_Free(EvolutionGraph *graph);
void BuildEvolutionGraph(EvolutionGraph *graph, u32 heapID);
void GetEvolutionTree(EvolutionGraph *graph, u16 species, u16 outList[MAX_EVOLUTION_TREE_SIZE], u8 *outCount);

#endif // POKEPLATINUM_EVOLUTION_LINES_H
