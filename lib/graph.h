#ifndef GRAPH_H
#define GRAPH_H

#include<stdlib.h>

typedef struct {
    size_t key;
    size_t *value;
} KV_ITEM;

typedef struct {
    size_t key;
    bool value;
} KV_BOOL;

void arr_put(size_t **item, size_t v);
size_t arr_get(size_t **item, size_t i);
void arr_free(size_t **item);
void hm_put(KV_ITEM **adj, size_t key, size_t *item);
void free_graph(KV_ITEM **adj);
size_t *dfs(KV_ITEM *adj, size_t *node, size_t node_n, size_t origin);
size_t *EulerPathByFleury(KV_ITEM *adj, size_t *node, size_t node_n);
size_t *HamiltonienPathByFleury(KV_ITEM *adj, size_t *node,size_t node_n);

#endif