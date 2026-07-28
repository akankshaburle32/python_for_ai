# c17    que 1:

## Teen numbers lo aur sabse bada print karo (`if/elif/else` se).

a = int (input ("Enter no. :"))
b = int (input ("Enter no. : "))
c = int (input ("Enter no. : "))

if a >= b and a >= c:
    print(f"Largest is {a}")

elif b >= c:
    print(f"Largest is {b}")

else:
    print(f"Largest is {c}")    