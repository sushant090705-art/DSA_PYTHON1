nums = [1, 4, 3, 6, 5, 7, 8, 5, 1]

def selectionSort(nums):
    n = len(nums)

    for i in range(n):
        minIndex = i

        for j in range(i + 1, n):
            if nums[j] < nums[minIndex]:
                minIndex = j

        nums[i], nums[minIndex] = nums[minIndex], nums[i]

    return nums

print(selectionSort(nums))