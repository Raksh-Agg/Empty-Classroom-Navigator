

from functionality.ReadSchedule import refine_schedule_data 
from functionality.ReadMap import refine_map_data
from functionality.Navigator import dfs_forward, final_function
import csv
def the_apex (room, day, hour, stay_from, stay_to) :
    map_csv_file = None
    with open ("./Map_NAB.csv", 'r', encoding='utf-8-sig') as file :
        reader = csv.reader(file)
        map_csv_file = list(reader)
    schedule_csv_file = None
    with open ("./TimeTable.csv", 'r', encoding='utf-8-sig') as file :
        reader = csv.reader(file)
        schedule_csv_file = list(reader)
    room = int(room)
    day = int(day)
    room = int(room)
    stay_from = int(stay_from)
    stay_to = int(stay_to)
    hour = int(hour)
    refined_map = refine_map_data(map_csv_file)
    refined_schedule = refine_schedule_data(schedule_csv_file)
    for key in refined_map.keys() :
        if refined_schedule.__contains__(key) == False :
            refined_schedule[key] = [[False for _ in range(10)] for _ in range(6)]
    pathLength, path = final_function(refined_map, refined_schedule, day, room, hour, stay_from, stay_to-1)
    # print("Path Length is : " + str(pathLength))
    # print ("Path is -> ", end="")
    listToStr = " - ".join([str(elem) for elem in path])
    print (listToStr)
    timeStr = ""
    for i in range(stay_from+8, stay_to+9) :
        if i != 12 :
            timeStr += str(i%12)
        else :
            timeStr += str(i)
        if i != stay_to+8:
            timeStr = timeStr + "____"
    strList = [timeStr, listToStr]
    return strList
