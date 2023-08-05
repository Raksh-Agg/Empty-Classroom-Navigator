possibleForwardPaths = []
possibleBackwardPaths = []

# Applying DFS from the attending class hour to end of range.
def dfs_forward (pathLength, path, curr_hour, curr_room, dayToAttend, roomDistances, roomsOccupied, hourRangeFinal) :
    if curr_hour > hourRangeFinal :
        # print(path)
        possibleForwardPaths.append((pathLength, path))
        return
    for key, value in roomDistances[curr_room].items() :
        if value > 10 :
            break
        # print (key)
        if roomsOccupied[key][dayToAttend][curr_hour] == False :
            path.append(key)
            # print(path)
            dfs_forward(pathLength + roomDistances[curr_room][key], path[:], curr_hour+1, key, dayToAttend, roomDistances, roomsOccupied, hourRangeFinal)
            path.pop()

# Applying DFS from start of range to attend class hour.
def dfs_backward (pathLength, path, curr_hour, curr_room, dayToAttend, roomDistances, roomsOccupied, hourRangeStart) :
    if curr_hour < hourRangeStart :
        possibleBackwardPaths.append((pathLength, path))
        return
    for key, value in roomDistances[curr_room].items() :
        if value > 10 :
            break
        if roomsOccupied[key][dayToAttend][curr_hour] == False :
            path.append(key)
            dfs_backward(pathLength + roomDistances[curr_room][key], path[:], curr_hour-1, key, dayToAttend, roomDistances, roomsOccupied, hourRangeStart)
            path.pop()

# Function which gives final Path which should be followed based on all input variabless
def final_function (roomDistances, roomsOccupied, dayToAttend, roomToAttend, hourToAttend, hourRangeStart, hourRangeFinal) :
    # You need to make hourRange a 0 based thingy
    dfs_forward(0, [], hourToAttend+1, roomToAttend, dayToAttend, roomDistances, roomsOccupied, hourRangeFinal)
    dfs_backward(0, [], hourToAttend-1, roomToAttend, dayToAttend, roomDistances, roomsOccupied, hourRangeStart)
    possibleForwardPaths.sort(key=lambda x: x[0])
    possibleBackwardPaths.sort(key=lambda x: x[0])
    finalPathLength = possibleBackwardPaths[0][0]
    finalPathLength = finalPathLength + possibleForwardPaths[0][0]
    print(possibleBackwardPaths[0][1])
    print(possibleForwardPaths[0][1])
    finalPath = possibleBackwardPaths[0][1]
    finalPath.append(roomToAttend)
    finalPath = finalPath + possibleForwardPaths[0][1]
    
    return (finalPathLength, finalPath)



