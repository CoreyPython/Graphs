"""
500 Rooms(Nodes)
Connections or passages between the room are the edges.
traversal_path = directions to traverse each room.
Visit each room once.
Need to have reverse directions

"""

from util import Queue, Stack

opposite_direction = {
    'n' : 's',
    's' : 'n',
    'e' : 'w',
    'w' : 'e'
}

def explore(player, path, graph = {}, trail = Stack()):
    room = player.current_room          # the starting and current room.
    if room.id not in graph.keys():     # checking to see if the room ID is part of the graph dictionary key value
        exits = room.get_exits()        # Getting the exits for the room.

        graph[room.id] = {direction: '?' for direction in exits}

        for direction in exits:
            if graph[room.id][direction] == '?':
                trail.push(direction)
                path.append(direction)
                player.travel(direction)
                explore(player, path, graph, trail)

    previous_step = trail.pop()
    if previous_step is None:
        return
    go_back = opposite_direction[previous_step]
    player.travel(go_back)
    path.append(go_back)
