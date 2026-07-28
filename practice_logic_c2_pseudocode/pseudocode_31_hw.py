# que 31:
## Ek list di hai. `min()` ke bina sabse chhota number dhoondho.
# Given: nums = [8, 3, 9, 1, 5]

# step 1:
# Ek list di hai. `min()` ke bina sabse chhota number dhoondho.

# step 2:   ex:  

# step 3:

# 1: nums ki list likho.
# 2: small = nums[0] bractect mai 0 nhi diya to error aatta hai to dena chahiye.
# 3: f0r mai nums ki jagh hum p bhi likh sakte hai.
# 4: if mai p < small  p list mai small no. dundo.
# 5: small = p 
# 6: print mai small likho. 



# step 4:

nums = [8, 3, 9, 1, 5]

small = nums[0]

for p in nums:
    if p < small:
        small = p
        print(small)



# step 5:

# step   nums       small    
# s1      8           -
# s2      8            8
# f-lp1   8            8
# if      8            8
# f-lp2   3            8
# if      3            3
# f-lp3   9            3
# if      9            3
# f-lp4   1            3
# if      1            1
# f-lp5   5            1
# if      5            1
# print(1)
