# que 33:
## Ek word diya hai. Har character ki frequency ki dict banao.
# Given: word = "banana"   →  {'b': 1, 'a': 3, 'n': 2}

# step 1:
# Ek word diya hai. Har character ki frequency ki dict banao.

# step 2: ex :  apple:  a : 1, p :2, l: 1, e:1.

# step 3: 

# 1:  words mai value likho 
# 2:counts mai {} likho quvki koi bhi count nhi hua hai.
# 3: for mai p ki value word likho.
# 4: if mai counts likho quvki vo vahi karga.
# 5: count + 1 karo count badega nhi to vahi rahega.
# 6: else mai count = 1 likho
# 7: print mai counts do.


# step 4:

word = "banana"
counts = {}
for p in word:
    if p in counts:
        counts[p] = counts[p] + 1
    else:
        counts[p] = 1
print(counts)

# step 5:

# step      words    count
# s1          b        -
# s2          b         {}
# f-lp1       b         {}
# if          b         {'b'=1}
# f-lp2       n         {'b'=1}     
# if          n         {'b'=1, 'n'=1}
# f-lp3       a         {'b'=1, 'n'=1}
# if          a         {'b'=1, 'n'=1, 'a'=1}
# f-lp4       n         {'b'=1, 'n'=1, 'a'=1}
# if          n         {'b'=1, 'n'=2, 'a'=1}
# f-lp5       a         {'b'=1,'n'=2, 'a'=1}
# if          a         {'b'=1, 'n'=2, 'a'=2}
# print({'b'=1, 'n'=2, 'a'=2})