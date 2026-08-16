# que 34:
## Ek sentence diya hai. word → count ki dict banao.
# Given: sentence = "the cat sat the cat"

# step 1:
# Ek sentence diya hai. word → count ki dict banao.

# step 2:   ex:  {apple, mamango, apple, mango,}  {'apple' = 2, 'mango='2}

# step 3:

# 1: sentance do.
# 2: words = sentence.split() gap deti hai.
# 3: count = [] kuch nhi hai.
# 4: for mai count[word] = 0, for mai count[word] += 1 do.
# 5: print mai count do.

# step 4:

sentence = "the cat sat the cat"

words = sentence.split()

count = {}

for word in words:
    count[word] = 0

for word in words:
    count[word] += 1

print("====================================")
print(count)        
print("====================================")

# step 5: 

#  Step      word       count                    
#  -           -          - 
#  1         the        {'the': 0}           
#  2         cat        {'the': 1, 'cat': 0} 
#  3         sat        {'the': 2, 'cat': 1, 'sat': 0} 
#  4         the        {'the': 1, 'cat': 1, 'sat': 1} 
#  5         cat        {'the': 2, 'cat': 2, 'sat': 1} 

# print {'the': 2, 'cat': 2, 'sat': 1}