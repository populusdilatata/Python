#Problem You want to make a list of the largest or smallest N items 
#in a collection. 
#1.4.1

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))      # [42, 37, 23]
print(heapq.nsmallest(3, nums))     #  [-4, 1, 2]

#Sample usage
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heap = list(nums)
heapq.heapify(heap)
print(heap)                #[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
print(heapq.heappop(heap)) #-4
print(heapq.heappop(heap)) #1                             
print(heapq.heappop(heap)) #2

