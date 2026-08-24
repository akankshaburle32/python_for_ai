# que 23:

"""
### Project 23 — Quiz Game with Scoring
- **EN:** Make a quiz. Store questions as a list of dicts (`question`, `answer`). Write `ask(question, answer)` that takes the user's input and returns `1` if correct else `0`. Loop all questions, add up the score with a `score` accumulator, then print a final result with a pass/fail message.
- **हिंदी:** एक quiz बनाओ। questions को dicts की list में रखो (`question`, `answer`)। `ask(question, answer)` बनाओ जो user का input लेकर सही होने पर `1` वरना `0` return करे। सभी questions पर loop चलाओ, `score` accumulator से जोड़ो, फिर pass/fail message के साथ final result print करो।
- **Concepts:** list of dicts, function returning a number, accumulator, `input()`
- **Hint:** `return 1 if user.strip().lower() == answer.lower() else 0`.

"""

# step 1:
## ek quiz banao. questions ko dicts ki list mai rakho (`question`, `answer`). "ask(question, answer)" banao jo user ka input lekar sahi hone par "1" varana "0" return kare. sabhi questions par loop chalao, "score" accumulator se jodo, fir pass/fail msg ke saath final result print karo.

# step 2:

# step 3:

# 1: quiz mai dict do que or ans vali 3.
# 2: def mai fun lo or usme para.
# 3: user mai input lo.
# 4: if mi user.lower() == 2para.lower() do. return mai 1 do.
# 5: else mai return 0 lo.
# 6: score mai 0 do.
# 7: for quiz ke badleme hum q likh sakte hai.
# 8: print mai score "/" len mai quiz
# 9: if score >= 2 print mai Pass or else mai fail

# step 4:

quiz = [
            {"questions": "Capital of India : ", "answer": "Delhi"},
            {"questions": "2 + 2 kitna hota hai? : ", "answer": "4"},
            {"questions": "Python kis type ki language hai? : ", "answer": "programming"}
        ]

def ask(question, answer):
    user = input(question)
    if user.lower() == answer.lower():
        return 1
    else: 
        return 0
        
score = 0
for q in quiz:
    score += ask(q["questions"], q["answer"])

print("Your Score:", score, "/", len(quiz))
if score >= 2:
    print("Pass")

else:
    print("Fail")    

# step 5:

"""
Capital of India : Dehli
2 + 2 kitna hota hai? : programming
Your Score: 2 / 3
Pass

"""