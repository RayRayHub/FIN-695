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

print(heights_and_ages_arr[1, :] < 55)
print("number of presidents started presidency younger than 55 is", (heights_and_ages_arr[1, :] < 55).sum())
print("number of presidents started presidency at 51 is", (heights_and_ages_arr[1, :] == 51).sum())

print("number of presidents taller than 188cm is", (heights_and_ages_arr[0, :] > 188).sum())
print("number of presidents exactly 183cm is", (heights_and_ages_arr[0, :] == 183).sum())

