# que 18:

"""
### Project 18 — Grade Report (one function, many students)
- **EN:** Write `get_grade(marks)` returning `"A"/"B"/"C"/"D"`. Then loop over a dict of students `{"Asha": 92, "Rahul": 70, "Priya": 81}` and print each student's grade using the function.
- **हिंदी:** `get_grade(marks)` बनाओ जो `"A"/"B"/"C"/"D"` **return** करे। फिर students के dict `{"Asha": 92, "Rahul": 70, "Priya": 81}` पर loop चलाकर हर student का grade function से print करो।
- **Concepts:** `return`, `if/elif/else`, reusing a function in a loop, dict `.items()`
- **Hint:** `>= 90 → A`, `>= 75 → B`, `>= 60 → C`, else `D`.

"""

# step 1:
## "get_grade(marks)" banao jo ""A"/"B"/"C"/"D"". **return** kare. fir student ke dict "{"Asha": 92, "Rahul": 70, "Priya": 81}" par loop chalaker har student ka grade function se print karo.

# step 2:   Ramu = 50 >>> Grade D

# step 3:

# 1: def mai fun do or parameter lo.
# 2: if mai marks > 90 return mai "A" lo.
# 3: elif mai marks > 75 return mai "B" lo.
# 4: elif mai marks > 60 return mai "C" lo.
# 5: else: return mai "D".
# 6: var mai list mai list lo.
# 7: for mai key value do. iteams mai.
# 8: print mai f string mai key function or usme value.

# step 4:

def get_grade(marks):
    if marks > 90:
        return "A"

    elif marks > 75:
        return "B"

    elif marks > 60:
        return "C"

    else: 
        return "D"

students = {"Asha": 92, "Rahul": 70, "Priya": 81}
for name,marks in students.items():

    print(f"{name}: Grade {get_grade(marks)}")                 

# step 5:

"""
Asha: Grade A
Rahul: Grade C
Priya: Grade B

"""