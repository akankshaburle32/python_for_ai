### 3 students ka naam aur 3 subjects ke marks rakho; har student ka total print karo. ###


students = [
                1.["Akanksha", 78, 86, 68],
                2.["Sakshi", 53, 69, 83],
                3.["Prachita", 63, 85, 96],
            ]

for s in students:
 total = s[1] + s[2] + s[3]
print (f"{s[0]}: {total}")