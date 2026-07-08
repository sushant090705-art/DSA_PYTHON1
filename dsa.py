# # #count the digits
# # n=5873
# # num =n 
# # count = 0
# # while num>0:
# #       count+=1
# #       num=num//10
# # print(count)
    


# # reverse a number or checking palindrome

# # n=1111
# # num=n
# # result=0
# # while num>0:
# #     ld=num%10
# #     result=(result*10)+ld
# #     num=num//10
# # if n==result:
# #         print("palindrome")    
# # else:
# #         print("not palindrome")    


# #armstrong number
   

# # n=153
# # num=n
# # total=0
# # nod=len(str(n))
# # while num>0:
# #     ld=num%10
# #     total = total +(ld**nod)
# #     num=num//10
# # print(total)
# # if n==total:
# #     print("armstrong number:")
# # else:
# #     print("not armstrong") 



# #print factor

# num=270
# result=[]
# for i in range (1,num+1):
#     if num%i==0:
#         result.append(i)
# print(result)

# n=[2,4,5,10,4,5,1,3,6]
# m=[111,10,45,3,4,6,5,3]
# for num in m:
#     count=0
#     for x in n:
#         if x==num:
#             count+=1
#     print(count)      

# count = 0

# def func():
#     global count

#     if count == 4:
#         return

#     print("sushant")
#     count += 1
#     func()

# func()

# print numer 4 times using recursion

# def func(x,n):
#    if n==0:
#       return
#    print(x)
#    func(x,n-1)
# func(15,4)   
  

#print 1 to n
 

# def func(i,n):
#     if i>n:
#         return
#     print(i)
#     func(i+1,n)
# func(1,4) 

# def func(n):
#     if n <= 1:
#         return 1
#     return n + func(n-1)

# print(func(5))
    

# #factorial 
# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     return num*factorial(num-1)
# print(factorial(5))

#reverse an array


# arr = [4,3,5,6,3,5,6,6,4]

# def func(arr, left, right):
#     if left >= right:
#         return

#     arr[left], arr[right] = arr[right], arr[left]
#     func(arr, left + 1, right - 1)

# def reverseSubArray(arr, l, r):
#     func(arr, l - 1, r - 1)
#     return arr

# result = reverseSubArray(arr, 0, 8 )
# print(result)


#reverse string or checking palindrome
# s = "nitin"

# class Solution:

#     def solve(self, s, left, right):
#         if left >= right:
#             return True

#         if s[left] != s[right]:
#             return False

#         return self.solve(s, left + 1, right - 1)

#     def isPalindrome(self, s):
#         return self.solve(s, 0, len(s) - 1)

# obj = Solution()
# print(obj.isPalindrome(s))

#fibonacci series using recursion

# class Solution:
#     def func(self, num):
#         if num <= 1:
#             return num
#         return self.func(num - 1) + self.func(num - 2)

# obj = Solution()

# n = 10

# for i in range(n):
#     print(obj.func(i), end=" ")


 