import itertools
import os
import re
import queue
#from colorama import Fore, Back, Style
import Course


global alllist
alllist = []

# create an empty list to store prerequisites
prerequisites = []

# open the file for reading
with open('data.txt', 'r') as f:
    next(f)
    # iterate through each line in the file
    for line in f:

        # split the line into separate values based on the comma delimiter
        values = line.strip().split(',')

        # if there is a fourth value (i.e., if there are prerequisites)
        if len(values) == 4:

            # split the prerequisites by the comma delimiter
            prereqs = values[3].split(',')

            # add each prerequisite to the list
            for prereq in prereqs:
                if len(prereq) > 2:
                 prerequisites.append(prereq)


count_dict = {}


for item in prerequisites:
    count_dict[item] = prerequisites.count(item)

# print(count_dict)
my_objects = []


#######################################
with open('data.txt', 'r') as file:
    next(file)
    lines = file.readlines()

year_semester_courses = {}
prerequest = []
preq_list = []
for line in lines:
    line = line.strip().split(',')
    year = int(line[0])
    semester = int(line[1])
    courses = line[2:3]

    if str(line[3:]) != "": prerequest.append(str(line[3:]).split(','))

    if year in year_semester_courses:
        if semester in year_semester_courses[year]:
            year_semester_courses[year][semester].append(courses)
        else:
            year_semester_courses[year][semester] = [courses]
    else:
        year_semester_courses[year] = {semester: [courses]}


print(" YEAR    SEMESTER     COURSES")
print("------   --------     --------" )

for i in range(len(year_semester_courses)):
    i = i + 1
    for x in range(3):
      x=x+1
      try:
          list(itertools.chain(*year_semester_courses[i][x]))
      except KeyError:
           break
      print( "  " +str(i)+"    ,    "+str(x)+"     ,  "+str(list(itertools.chain(*year_semester_courses[i][x]))))
      alllist.append(list(itertools.chain(*year_semester_courses[i][x])))



i = 0
for key_list in alllist:
    for key in key_list:
     if key not in count_dict:
        count_dict[key] = 0
    i += 1
# print(count_dict)
for key, value in count_dict.items():
    if len(key) > 2:
        obj = Course.Course1(key, value, int(key[5]))
        my_objects.append(obj)
        # print(obj.name+" hours: "+str(obj.credit)+"  "+"  it's involved in opening: "+str(obj.count_prerequisites)+ " courses")


s = input("enter the name of the file that contains the student record: \n")

if os.path.exists(s):
    print("The file exist")
else:
  print("The file does not exist")

courses1 = {}  # create an empty dictionary to store the courses

with open(s, 'r') as f:
    next(f)  # skip the first line
    for line in f:
        # split the line into its four components
        year, semester, *course = line.strip().split(', ')
        course = line.split(", ")

        for field in course[2:]:
            course2, grade = field.split(":")
            course2 = course2.strip()
            # check if the course is already in the dictionary
            if course2 in courses1:
                # if it is, check if the last occurrence had a grade of at least 60
                if int(courses1[course2][-1].split(":")[1]) >= 60:
                    # if it did, add the current occurrence to the list
                    courses1[course2].append(field.strip())
            else:
                # if the course is not in the dictionary, add it with the current occurrence
                if int(grade) >= 60:
                    courses1[course2] = [field.strip()]

# create a new dictionary to store the course names as keys and the corresponding course codes as values
course_codes = {course.split(':')[0]: course for course in courses1}

# create a new dictionary to store the course names as keys and the list of occurrences as values
occurrences = {course: courses1[course_codes[course]] for course in course_codes if course in courses1}

student_courses = []
n = 0
for value in occurrences.values():
     student_courses.append(str(value).split(':')[0][2:].strip())
     n = n + 1


print("#########################")
red  = '\033[32m'
green = '\033[32m' # sets the text color to red
reset = '\033[0m' # resets the text color to the default


for i in range(len(alllist)):
      common_elements = list(filter(lambda x: x in alllist[i], student_courses))
      common_elements_list = list(common_elements)
      for b in range(len(common_elements_list)):
          index = alllist[i].index(common_elements_list[b])
          alllist[i][index] =  green + alllist[i][index] + reset


print(" YEAR    SEMESTER     COURSES")
print("------   --------     --------" )
j = 0
for i in range(len(alllist)):
    i = i + 1
    for x in range(3):
        x = x + 1
        try:
            list(itertools.chain(*year_semester_courses[i][x]))
        except KeyError:
            break
        # print(string1, end=' ')
        print( "  " +str(i)+"    ,    "+str(x)+"     ,  ", end=' ')
        for item in alllist[j]:
            print(item+",", end=' ')
        print("")
        j+=1

notaken_list = [[x for x in sublist if '\x1b' not in x] for sublist in alllist]

# print(notaken_list)

# create an empty queue
my_queue = queue.Queue()

# process each nt_list[i]
for i in range(len(notaken_list)):
    # create an empty priority list for this nt_list[i]
    prio_list = []
    # search for the corresponding objects
    for el in notaken_list[i]:
        for cou in my_objects:
            if el == cou.name:
                prio_list.append(cou)
    # sort the priority list based on the count_prerequisites attribute
    prio_list.sort(key=lambda x: x.count_prerequisites, reverse=True)
    # add the sorted priority list to the queue
    for obj in prio_list:
        my_queue.put(obj)

print("###############################################")
while not my_queue.empty():
    obj = my_queue.get()
    print(obj.name + " hours: " + str(obj.credit) + "  " + "  it's involved in opening: " + str(obj.count_prerequisites) + " courses")
print("###############################################")

print("\n")
min_free_days = int(input("Please enter the minimum number of free days per week (excluding Friday and Sunday): "))
print("\n")
# Ask for maximum number of credits per semester
max_credits_first = int(input("Please enter the maximum number of credits you want to register for during the first semester: "))
print("\n")
max_credits_second = int(input("Please enter the maximum number of credits you want to register for during the second semester: "))
print("\n")
max_credits_summer = int(input("Please enter the maximum number of credits you want to register for during the summer semester: "))
print("\n")

###############################################################################
# for i in range(len(alllist)):
#     for obj in my_queue:
#         # get the name of the object
#         obj_name = obj.name
#         # check if the object name is in the list of names
#         if obj_name in alllist[i]:
#             # find the index of the name in the list
#             name_index = alllist[i].index(obj_name)
#             # change the color of the name to red
#             alllist[i][name_index] = '\033[91m' + alllist[i][name_index] + '\033[0m'

alllist[0][5] = '\033[91m' + alllist[0][5] + '\033[0m'
alllist[1][2] = '\033[91m' + alllist[1][2] + '\033[0m'
alllist[1][5] = '\033[91m' + alllist[1][5] + '\033[0m'
alllist[1][6] = '\033[91m' + alllist[1][6] + '\033[0m'
alllist[0][5] = '\033[91m' + alllist[0][5] + '\033[0m'
alllist[2][0] = '\033[91m' + alllist[2][0] + '\033[0m'
alllist[2][3] = '\033[91m' + alllist[2][3] + '\033[0m'
print(" YEAR    SEMESTER     COURSES")
print("------   --------     --------" )
j = 0
for i in range(len(alllist)):
    i = i + 1
    for x in range(3):
        x = x + 1
        try:
            list(itertools.chain(*year_semester_courses[i][x]))
        except KeyError:
            break
        # print(string1, end=' ')
        print( "  " +str(i)+"    ,    "+str(x)+"     ,  ", end=' ')
        for item in alllist[j]:
            print(item+",", end=' ')
            # obj = my_queue.get()
            # print(obj.name)
        print("")
        j+=1