#CURD

#Create/Add

assignments = []

next_id_number = 1

new_id = "HW" + str(next_id_number)
next_id_number +=1

print("Assignmnet key(primary key simulation)",new_id)

assignments.append(
    {
        "id":new_id,
        "title": "Intro to DB",
        "description" : "basics of database"
    })

new_id = "HW" + str(next_id_number)
next_id_number +=1

assignments.append(
    {
        "id": new_id,
        "title" : "Case study - ERD",
        "description" : "practice ER design"
    }
)

print(assignments)


## Read

# Query 1: Display all assignments data

#input

#prcoess

#output
for assignmnet in assignments:
    print(f"id: {assignmnet["id"]} title: {assignmnet['title']}")


# Query 2: find the assignmnet with assignmnet title : Intro to DB and display the assignmnet details

#input
...
#proccess 
#find an assignment
exists = False
found_assignmnet = None
for assignmnet in assignments:
    if assignmnet["title"] == "Intro to DB":
        exists = True
        found_assignmnet = assignmnet
        break

#output
#display the assignmnet information
if exists:
    print(found_assignmnet)
else:
    print("Not found!")