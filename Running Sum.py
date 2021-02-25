def runningSum(nums):
    sum = []
    currentSum = 0
    for i in nums:
        currentSum+=i
        sum.append(currentSum)
    return sum