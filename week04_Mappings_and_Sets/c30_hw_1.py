## c30 hw que 1.

## 3 dicts ki list banao (naam, age) aur age ke hisaab se sort karke print karo.

students = [
                {"name" : "akanksha", "age" : 16},
                {"name" : "chakuli", "age" : 19},
                {"name" : "arti", "age" : 23},
]
s = students
for s in sorted(students, key= lambda s:s["age"]):
    print(s["name"], s["age"])