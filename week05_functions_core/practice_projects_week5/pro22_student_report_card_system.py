# que 22:

"""
### Project 22 — Student Report Card System
- **EN:** Write `total(marks)`, `average(marks)`, and `grade(avg)` functions. Loop over a list of students (each a dict with `name` and a list of 3 subject marks) and print a full report line for each. At the end print the class topper.
- **हिंदी:** `total(marks)`, `average(marks)`, और `grade(avg)` functions बनाओ। students की list (हर एक dict जिसमें `name` और 3 subjects के marks की list हो) पर loop चलाकर हर student की पूरी report line print करो। आख़िर में class topper print करो।
- **Concepts:** functions on lists, loop over list of dicts, running max
- **Hint:** `total` = `sum(marks)`, `average` = `total / len`. Track topper with a max-average variable.

"""

# step 1:
## "total(marks)", "average(marks)" or "grade(avg)" fun banao. students ki list (har ek dict jisme 'name' or 3 sub ke marks ki list ho) par loop chalaker har studentv ki puri report line print karo. aakhirmmai class topper print karo.

# step 2:

# step 3:

# 1: def mai total fun lena ahi or usme para marks dena hai. return mai sum(marks).
# 2: def average ka fun banao or usme para marks do, return mai 1st fun / len(marks) ka divide kardo.
# 3: def mai grade fun mai avg do. if mai avg > 90.return "A" do. elif mai avg > 75 return "B". elif mai avg > 60 return "C" or else mai "D".
# 4: student mai dict lo or usme name or marks 3 sub ke.
# 5: ek variable lo = ""
# 6: topper_avg = 0
# 7: for mai student ki vajah s dijiye.
# 8: avg mai averange nikale sakte hai student ke marks ka.
# 9: if mai avg > topper do.
# 10: print mai avg or name nikalo.


# step 4:

def total(marks):
    return sum(marks)

def average(marks):
    return total(marks) / len(marks)

def grade(avg):
    if avg > 90:
        return "A"

    elif avg > 75:
        return "B"

    elif avg > 60:
        return "C"

    else:
        return "D"

students = [
                {"name": "Bhumi", "marks": (89, 67, 75)},
                {"name": "Renu", "marks": (54, 68, 97)},
                {"name": "Chaku", "marks": (96, 85, 93)}
            ]

topper_name = ""
topper_avg = 0

for s in students:
    avg = average(s["marks"])
    print(f"{s['name']:<6} | Total: {total(s['marks'])} | Avg: {avg:.2f} | Grade: {grade(avg)}")
    if avg > topper_avg:
        topper_avg = avg
        topper_name = s["name"]

print(f"\nClass Topper: {topper_name} ({topper_avg:.2f})")

# step 5:

"""
Bhumi | Total: 231 | Avg: 77.00 | Grade: B
Renu  | Total: 219 | Avg: 73.00 | Grade: C
Chaku | Total: 274 | Avg: 91.33 | Grade: A

Class Topper: Chaku (91.33)

"""