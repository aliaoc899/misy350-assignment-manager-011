assignment = {
        "title":"Homework1: Intro to Database Design",
        "description":"Create an ER Model",
        "due_date": "2026-01-26",
        "is_published": False,
        "questions":[]
} #dictionary

if "title" in assignment:
    print(f"Title: {assignment["title"]}")

assignment["additional_files"] = "basics of database" #add a new key to the dict
assignment["is_published"] = True #updates the value of a key 