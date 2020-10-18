# Input: List of students [{Name: grade}]
# Output: Avg grade for a student

# Code to check in main.py
# students = [{"Ann": 5}, {"Bob": 4}, {"Ann": 3}, {"Ann": 4}]
# print(avg_grade(students))

def avg_grade(list_of_maps):
    res_dict = {} # {"Name1" : [1, 2, 3], "Name2": [2, 2, 4]}
    # Group grade values by Name
    for map in list_of_maps: # map: {"Name": 2}
        for key in map:
            if key in res_dict.keys():
                res_dict[key].append(map[key])
            else:
                res_dict[key] = [map[key]]
    # Find Avg for a Name
    for key in res_dict:
        res_dict[key] = round(sum(res_dict[key])/len(res_dict[key]))
    return res_dict