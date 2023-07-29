from ReadSchedule import refine_schedule_data 
from ReadMap import refine_map_data
import csv
# data = 
map_data = None
with open ("./Map_NAB.csv", 'r', encoding='utf-8-sig') as file :
    reader = csv.reader(file)
    map_data = list(reader)
var = refine_map_data(map_data)
for key, val in var.items() :
    print (str (key) + " ->")
    print (val)
# print((var[6101]))
# for i in var :
    # print(i)

# with open ("./TimeTable.csv", 'r') as file :
#     reader = csv.reader(file)
#     map_data = list(reader)
# var = refine_schedule_data(map_data)

# # print (take(5, var.items()))
# # 
# # print (var)
# for key,val in var.items() :
#     print (str(key) + " ->")
#     # print(val)
#     for c in val :
#         for r in c :
#             print((1 if r else 0), end=" ")
#         print()
# print (refine_schedule_data(map_data))