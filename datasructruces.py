#third largestv number in list

# list2 = [1,2,3,5,52,68,98,75,14]

# first =second =third =0

# for i in list2:
#     if i > first:
#         third = second
#         second = first
#         first = i
#     if i > second and i != first:
#         third = second
#         second = i
#     elif i > third and i != second and i != first:
#         third = i
# print(third)

#second largestv number in list
# list1 = [1,2,3,5,52,68,98,75,14]

# first = second = 0

# for i in list1:
#     if i > first:
#         second = first
#         first = i
#     elif i > second and i != first:
#         second = i
# print(second)

# list1 = [[1,2,3],[4,5,6],[7,8,9]]
# list2 = []
# def nested_list(list1):
#     for i in list1:
#         if isinstance(i, list):
#             nested_list(i)
#         else:
#             list2.append(i)            
#     return list2
# print(nested_list([[1,2,3],[4,5,6],[7,8,9]]))


# list1 = [1,2,4,5,6]
# for i in range(1,len(list1)+1):
#     if i not in list1:
#         print(i)

# list1 = [0,1,0,3,12]

# list1 = [3,2,3,5,5,8,8,8]
# c=0
# res =0
# for i in list1:
#     if c<list1.count(i):
#         c = list1.count(i)
#         res = i
# print(res)
    
    
# arr = [1, 2, 3, 4]
# arr1 =[]
# for i in range(len(arr)):
#     res = 1
#     for j in arr:
#         if arr[i]!=j:
#             res = res * j
#     arr1.append(res)
# print(arr1)


# list1 =[3,3,5,5,8,8,8]
    # for j in range(i+1, len(arr)):
# list1=[1,2,3,4,5,6,7]
# k=3
# # → [5,6,7,1,2,3,4]
# for i in range(k):
#     temp = list1[0]
#     for j in range(len(list1)-1):
#         list1[j] = list1[j+1]
#     list1[-1] = temp
# print(list1)

# s = "abcabcbbabcd"
# left =0
# char_set =set()
# for i in s:
#     while i in char_set:
#         char_set.remove(i)
#         left+=1
#     char_set.add(i)
# print(char_set)
    
# Input="programming"
# Output=""

# for i in Input:
#     if i not in Output:
#         Output+=i
# print(Output)


# arr = [1,2,3,4,6]
# target = 6
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]+arr[j] == target:
#             print(arr[i],arr[j])

# arr = [1, 2, 3, 4, 6]
# target = 6

# arr.sort()  # Ensure the array is sorted for the two-pointer approach
# left, right = 0, len(arr) - 1

# while left < right:
#     current_sum = arr[left] + arr[right]
#     if current_sum == target:
#         print(arr[left], arr[right])
#         left += 1
#         right -= 1
#     elif current_sum < target:
#         left += 1
#     else:
#         right -= 1
        
# str1 = "abcabcbb" 
# # → longest substring without repeating
# s = set()
# for i in str1:
#     if i in s:
#         s.remove(i)  # Remove characters up to and including the repeated character
#     s.add(i)  # Add the current character to the set
# print(s)
    
        
# arr =[1,2,5,8,9,10]
# left = 0                                                                            
# right = len(arr)-1
# while left<right:
#     arr[left],arr[right] = arr[right],arr[left]
#     left+=1
#     right-=1
# print(arr)


# arr = [0,1,0,3,12] 
# → [1,3,12,0,0]
# left = 0
# right = len(arr)-1
# while left<right:
#     if arr[left] == 0:
#         arr[left],arr[right] = arr[right],arr[left]
#         right-=1
#     else:
#         left+=1
# print(arr)

arr =[3,4,5,688,7,8,9]
left =0
right = len(arr)-1
while left<right:
    if arr[left]>arr[right]:
        arr[left],arr[right] = arr[right],arr[left]
        right-=1
    else:
        left+=1
        
print(arr)
