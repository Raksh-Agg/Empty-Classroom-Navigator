from ReadSchedule import refine_schedule_data 
import csv
# data = 
with open ("./TimeTable.csv", 'r') as file :
    reader = csv.reader(file)
    map_data = list(reader)
var = refine_schedule_data(map_data)

# print (take(5, var.items()))
# 
# print (var)
for key,val in var.items() :
    print (str(key) + " ->")
    # print(val)
    for c in val :
        for r in c :
            print((1 if r else 0), end=" ")
        print()
# print (refine_schedule_data(map_data))