#include "evolution_lines.h"

#include <nitro.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "constants/narc.h"
#include "constants/species.h"

#include "heap.h"
#include "narc.h"
#include "species.h"

EvolutionGraph *EvolutionGraph_New(u32 heapID)
{
    EvolutionGraph *evolutionGraph = Heap_Alloc(heapID, sizeof(EvolutionGraph));
    memset(evolutionGraph, 0, sizeof(EvolutionGraph));
    return evolutionGraph;
}

void EvolutionGraph_Free(EvolutionGraph *graph)
{
    Heap_Free(graph);
}

void BuildEvolutionGraph(EvolutionGraph *graph, u32 heapID)
{
    for (int species = 0; species < MAX_SPECIES; ++species) {
        SpeciesEvolution *speciesEvolutions = NARC_AllocAndReadWholeMemberByIndexPair(NARC_INDEX_POKETOOL__PERSONAL__EVO, species, heapID);
        for (int i = 0; i < MAX_EVOLUTIONS; ++i) {
            u16 target = speciesEvolutions[i].targetSpecies;
            if (target == 0) {
                break;
            }

            graph->adj[species][graph->adjSize[species]++] = target;
            graph->adj[target][graph->adjSize[target]++] = species;
        }
        Heap_Free(speciesEvolutions);
    }
}

void GetEvolutionTree(EvolutionGraph *graph, u16 species, u16 outList[MAX_EVOLUTION_TREE_SIZE], u8 *outCount)
{
    u8 visited[MAX_SPECIES] = { FALSE };
    u16 queue[MAX_EVOLUTION_TREE_SIZE];
    u8 front = 0, back = 0;

    queue[back++] = species;
    visited[species] = TRUE;

    *outCount = 0;

    while (front < back) {
        u16 current = queue[front++];
        outList[(*outCount)++] = current;

        for (u8 i = 0; i < graph->adjSize[current]; ++i) {
            u16 neighbor = graph->adj[current][i];
            if (!visited[neighbor]) {
                visited[neighbor] = TRUE;
                queue[back++] = neighbor;
            }
        }
    }
}
