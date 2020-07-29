from graph import Graph
from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    queue = Queue()
    cur_node = starting_node
    cache = {}
    for node in ancestors:
        if node[1] not in cache:
            cache[node[1]] = set()
        cache[node[1]].add(node[0])

    if starting_node in cache:
        queue.enqueue(cache[cur_node])
    else:
        return -1

    while True:
        relations = queue.dequeue()
        cur_node = min(relations)
        if cur_node not in cache:
            return cur_node
        else:
            queue.enqueue(cache[cur_node])