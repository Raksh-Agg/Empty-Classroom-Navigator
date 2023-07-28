def refine_schedule_data(schedule_data):
    roomOccupied = {}
    dayToRow = {'M': 0, 'T': 1, 'W': 2, 'Th': 3, 'F': 4, 'S': 5}
    for lecture in schedule_data:
        if len(lecture[8]) == 0 or lecture[8].isdigit() == False:
            continue
        lectureRoom = int(lecture[8])
        if lectureRoom < 6101 :
            continue
        elif lectureRoom > 6164 :
            continue
        elif lectureRoom < 6151 and lectureRoom > 6110 :
            continue
        lectureTimings = lecture[9]
        # print(roomOccupied)
        # if (len(roomOccupied[lectureRoom]) == 0) :
        if roomOccupied.__contains__(lectureRoom) == False :
            roomOccupied[lectureRoom] = [[False for _ in range(10)] for _ in range(6)]
        lectureTimingsParts = lectureTimings.split()
        ltpSize = len(lectureTimingsParts)
        indexForNum = 0
        indexForDay = 0
        print(lecture)
        while indexForDay < ltpSize and indexForNum < ltpSize :
            while lectureTimingsParts[indexForNum].isdigit() == False :
                indexForNum += 1
            if int(lectureTimingsParts[indexForNum]) > 10 :
                break
            while indexForDay < indexForNum :
                # print(int(lectureTimingsParts[indexForNum])-1)
                roomOccupied[lectureRoom][dayToRow[lectureTimingsParts[indexForDay]]][int(lectureTimingsParts[indexForNum])-1] = True
                indexForDay += 1
            indexForDay = indexForNum + 1
            indexForNum += 2
        # roomOccupied[lectureRoom] = 
    return roomOccupied
