def TotalSales(nums):
    total = 0
    for i in range(len(nums)):
        total = total + nums[i]
    return total

#print(TotalSales([200,100,100,100]))
#print(TotalSales([800,500,400]))