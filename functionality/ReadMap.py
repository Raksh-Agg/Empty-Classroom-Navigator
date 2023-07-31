from collections import deque


def refine_map_data(map_data):
    roomDistances = {}
    grid_data = map_data
    roomDistances = calculate_room_distances(map_data)
    for key, values in roomDistances.items() :
        if roomDistances[key].__contains__(key) : 
            del roomDistances[key][key]
        roomDistances[key][key] = -5
        roomDistances[key] = dict(sorted(values.items(), key=lambda x:x[1]))
    # Your code to refine map_data and create distance
    # distance = [...]  # Your processed data
    return roomDistances


# def bfs_distance(grid_data, start_room):
#     # Function to perform BFS and calculate distances from the start_room to all other rooms
#     rows, cols = len(grid_data), len(grid_data[0])
#     visited = [[False for _ in range(cols)] for _ in range(rows)]
#     queue = deque([(start_room, 0)])
#     distances = {}

#     while queue:
#         room, distance = queue.popleft()

#         if not visited[room[0]][room[1]]:
#             visited[room[0]][room[1]] = True
#             distances[room] = distance

#             # Add neighbors (adjacent rooms) to the queue
#             for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                 new_x, new_y = room[0] + dx, room[1] + dy
#                 if 0 <= new_x < rows and 0 <= new_y < cols and grid_data[new_x][new_y] != 'R' and not visited[new_x][new_y]:
#                     queue.append(((new_x, new_y), distance + 1))

#     return distances

def calculate_room_distances(grid_data):
    # Function to calculate distances between all rooms using BFS
    room_numbers = set()
    room_connections = {}

    for row in range(len(grid_data)):
        for col in range(len(grid_data[0])):
            if grid_data[row][col].isdigit() == True :
                this_room = int(grid_data[row][col])
                curr_connections = dfs(this_room, row, col, grid_data)
                if (room_connections.__contains__(this_room)) :
                    for key, value in curr_connections.items() :
                        if room_connections[this_room].__contains__(key) == False :
                            room_connections[this_room][key] = 100
                        room_connections[this_room][key] = min(room_connections[this_room][key], value)
                else :
                    room_connections[this_room] = curr_connections

                # room_connections[this_room] = 

    return room_connections


def dfs (room, curr_x, curr_y, grid_data) :
    pathQueue = deque([(curr_x, curr_y, 0)])
    # print (grid_data)
    rows = len(grid_data)
    # print (grid_data[0])
    cols = len(grid_data[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    distances = {}
    while pathQueue : 
        curr_x, curr_y, curr_dist = pathQueue.popleft()
        visited[curr_x][curr_y] = True
        for del_x, del_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = curr_x + del_x
            new_y = curr_y + del_y
            if 0 <= new_x < rows and 0 <= new_y < cols :
                if visited[new_x][new_y] == False :
                    visited[new_x][new_y] = True
                    if grid_data[new_x][new_y] == '' :
                        continue
                    elif grid_data[new_x][new_y].isdigit() == True :
                        new_room = int(grid_data[new_x][new_y])
                        if distances.__contains__(new_room) == False :
                            distances[new_room] = 100
                        distances[new_room] = min (distances[new_room], curr_dist + 1)

                    elif grid_data[new_x][new_y] == 'R' :
                        pathQueue.append((new_x, new_y, curr_dist+1))
    return distances
                    




