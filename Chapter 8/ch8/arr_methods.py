import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185,
           168, 173, 183, 173, 173, 175, 178,
           183, 193, 178, 173, 174, 183, 183,
           180, 168, 180, 170, 178, 182, 180,
           183, 178, 182, 188, 175, 179, 183,
           193, 182, 183, 177, 185, 188, 188,
           182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51,
        49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 
        51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 
        54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 
        64, 46, 54, 47, 70]

heights_arr = np.array(heights)
heights_and_ages = heights + ages 
heights_and_ages_arr = np.array(heights_and_ages)
heights_and_ages_arr=heights_and_ages_arr.reshape((2,45))

print(heights_and_ages_arr.sum())
print("the sum of heights and ages are", heights_and_ages_arr.sum(axis=1))
# Obtain a list of minimum height and age
min_height_age=heights_and_ages_arr.min(axis=1)
print(min_height_age)
# Extract the minimum height only
min_height=min_height_age[0]
print(f"the minimum height is {min_height} cm")
# Obtain a list of maximu height and age
max_height_age=heights_and_ages_arr.max(axis=1)
print(max_height_age)
# Extract the maximum age only
max_age=max_height_age[1]
print(f"the maximum age is {max_age} years old")
# Find out who is the oldest president
oldest_president=heights_and_ages_arr[1,:].argmax()
print(f"the oldest president is number {oldest_president+1}")
# Print out the average height and age
print(f"the average height and age are {heights_and_ages_arr.mean(axis=1)}")

heights_and_ages_arr[:, 1].sum()
print(heights_and_ages_arr[:, 1])
print(heights_and_ages_arr[:, 1].sum())

print(heights_and_ages_arr.sum(axis = 1))

arr1 = np.array([[ 1, 2, 3], [2, 4, 6]])
print(arr1.min(axis=0))

print(arr1[:,0]*3)
print(arr1[0] * 3)
print(arr1[0,:]*3)





















