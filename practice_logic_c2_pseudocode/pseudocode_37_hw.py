# que 37:
## Do lists di hain. Dono mein common values print karo (sets).
# Given: a = [1, 2, 3, 4], b = [3, 4, 5, 6]

# step 1:
## Do lists di hain. Dono mein common values print karo (sets).

# step 2:

# step 3:

# 1: a = list do b = list do.
# 2: set1 set(a) set set(b).
# 3: common var lo set1 & set2.
# 4: print(common)

# step 4:

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

set1 = set(a)
set2 = set(b)

common = set1 & set2
print(common)

# step 5:

#  step     statement                   value
#   1	        a	                [1, 2, 3, 4]
#   2	        b	                [3, 4, 5, 6]
#   3	    set1 = set(a)	        {1, 2, 3, 4}
#   4	    set2 = set(b)	        {3, 4, 5, 6}
#   5	    common = set1 & set2	{3, 4}
#   6	    print(common)	        {3, 4}