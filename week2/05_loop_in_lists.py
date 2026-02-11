course_data = [
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

course_data.append(
    {
        "id" : "HW3",
        "title" : "Case Study",
        "description" : "comprehansive analysis of db",
        "due_date" : "2026-02-10",
        "score" : 100   
    }
)

for assignment in course_data:
    if "title" in assignment:
        print(f"Title: {assignment['title']}")


counter = 0
for assignmnet in course_data:
    if "title" in assignment and assignment["title"] == "Homework2: Normalization":
        print("index" , counter)
        break
    counter = counter + 1