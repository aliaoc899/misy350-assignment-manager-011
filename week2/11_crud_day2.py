assignments = [
    {
        "id": "HW1",
        "title": "Homework 1: intro to database",
        "description": "learning the basics",
        "due_date" : "2026-01-26",
        "score": 100,
    },
    {
        "id": "HW2",
        "title": "Homework2: Normalization",
        "description": "learning to normalize",
        "due_date" : "2026-01-28",
        "score" : 100
    }
]

new_assignment_id_number = 3

#---- new id creation pattern
new_assignmnet_id = "HW" + str(new_assignment_id_number)
new_assignment_id_number += 1
#-------

#CRUD

#Create/add new assignment
assignments.append(
    {
        "id" : new_assignmnet_id,
        "title" : "Final Project: database design",
        "description" : "in this assignmnet, we are going to build a complete database",
        "due_date" : "2026-03-30",
        "score" : 100
    }
)

#Read
#Query 1: Display all assignments information

#input

#pull assignment data

#process

#output
for assignment in assignments:
    print(f"ID: {assignment["id"]}, Title: {assignment['title']}, Description: {assignment['description']} ")

#Query 2: Find an assignment with title : Homework2: Normalization and display the assignment info

#input
#pull assignment data
search_title = "Homework2: Normalization"

#process - Find the assignment
exists = False
assignmnet_details = None
for assignmnet in assignments:
    if assignment['title'] == search_title:
        exists = True
        assignmnet_details = assignmnet
        break



#output - display the assignment info if it exists
if exists:
    print(assignmnet_details)
else:
    print("Not Found!")

#Q3: Update the description of an assignment with an assignmnet id = HW1 and confim the update. 
# New description  = This assignmnet is about the basics

#input
search_assignment_id = "HW1"
new_description = "This assignmnet is about the basics"

#process = Update assignmnet Description by assignment ID
successful = False
for assignment in assignments:
    if assignment['id'] == search_assignment_id:
        assignment['description'] = new_description
        successful = True
        break


#output = Display Success/Failure of update activity
if successful:
    print("Assignment Description was updated")
else:
    print("Update was not successful")


#Delete
#Remove assignment with assignment id = HW1

index = 0
found = False

for assignmnet in assignments:
    if assignments['id'] == "HW1":
        found = True
        break
    index += 1

if found:
    del assignments[index]


