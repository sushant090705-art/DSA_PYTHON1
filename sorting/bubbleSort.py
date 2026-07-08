arr = [4,6,32,2,55,6,3]
def bubble(arr):
    n=len(arr)
    for i in range (n-2,-1,-1):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr            
print(bubble(arr))
 