# c18     que 3:
## Ek list `["red","green","blue"]` ko `enumerate` se number ke saath print karo.

colors = ["Red", "Green", "Blue", "Pink"]

for index, colors in enumerate(colors, start = 1):
    print(f"{index} : {colors}")