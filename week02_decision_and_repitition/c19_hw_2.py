# c19   que 2:

## User se numbers maangte raho jab tak woh "stop" na likhe; phir total sum print karo.

total = 0
num = input("Enter a no. (or 'stop'): ")

while num.lower() != "stop":
    total = total + int(num)
    num = input ("Enter a n0. (or 'stop'): ")

    print("Total Sum =", total) 