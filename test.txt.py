import json
from datetime import datetime

courseList = ["COMP133", "COMP111", "COMP122"]

with open('jason.json') as f:
    data = json.load(f)

    unique_keys = []
    used_times = []
    used_days = []
    my_dict = {}

    for key in data.keys():
        course_code, course_type, course_number = key.split("-")
        for course in courseList:
            if course_code == course:
                my_dict.setdefault(course, {})
                my_dict[course][key] = data[key]
                print(str(key) + " " + str(data[key]))

    for course, course_data in my_dict.items():
        lectures = [k for k in course_data.keys() if "Lecture" in k]
        labs = [k for k in course_data.keys() if "Lab" in k]

        # Check labs against lectures
        for l in lectures:
            for lab in labs:
                if set(course_data[l].keys()) & set(course_data[lab].keys()) - {"Instructor"}:
                    unique_keys.append(l)
                    used_times.extend(list(set(course_data[l].keys()) & set(course_data[lab].keys()) - {"Instructor"}))
                    used_days.extend([day for day in set(course_data[l].keys()) & set(course_data[lab].keys()) - {"Instructor"} if day not in used_days])

        # Check labs against labs
        for l1 in labs:
            for l2 in labs:
                if l1 != l2 and set(course_data[l1].keys()) & set(course_data[l2].keys()) - {"Instructor"}:
                    unique_keys.append(l1)
                    used_times.extend(list(set(course_data[l1].keys()) & set(course_data[l2].keys()) - {"Instructor"}))
                    used_days.extend([day for day in set(course_data[l1].keys()) & set(course_data[l2].keys()) - {"Instructor"} if day not in used_days])

        # Check lectures against lectures
        for l1 in lectures:
            for l2 in lectures:
                if l1 != l2 and set(course_data[l1].keys()) & set(course_data[l2].keys()) - {"Instructor"}:
                    if l1 not in unique_keys:
                        unique_keys.append(l1)
                    used_times.extend(list(set(course_data[l1].keys()) & set(course_data[l2].keys()) - {"Instructor"}))
                    used_days.extend([day for day in set(course_data[l1].keys()) & set(course_data[l2].keys()) - {"Instructor"} if day not in used_days])

print(unique_keys)



    #for key, value in my_dict.items():
    #    day_time = set(value.keys()) - {"Instructor"}  # get the set of days and times
     #   if len(day_time) >= 2:  # check if there are 2 values in the set
      #      day, time = tuple(day_time)  # convert to tuple to extract day and time
       #     if time not in used_times or day not in used_days:
        #        unique_keys.append(key)
         #       used_times.append(time)
          #      used_days.append(day)

    #print(unique_keys)
    
    # Print out the list of dictionaries that match the criteria
   # for course in course_list_Lecture:
    #    keys_list = list(course.keys())
     #   second_key = keys_list[1]
      #  print("Lecture")
       # print(second_key + " and this is the time " + course[second_key])

    #for course in course_list_Lap:
     #   keys_list = list(course.keys())
      #  second_key = keys_list[1]
       # print("Lab")
        #print(second_key + " and this is the time " + course[second_key])





