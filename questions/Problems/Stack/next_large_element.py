#solution: https://www.geeksforgeeks.org/dsa/next-greater-element/
"""
Hint: use stack and iterate the array from. end to start while adding each element to stack
Input: arr[] = [1, 3, 2, 4]
Output: [3, 4, 4, -1]

res = []
when 4 stack is empty no next element so -1 i.e res[-1]
 add 4 to stack => stack = [4]
next point to 2 so 4>2 true hence 4 is answer i.e res[4,-1]
arr = point = 3 stack = [2,4]
3<2 No pop element
3<4 yes so 4 is answer add to result arr else -1
"""

#Brute force approach:

# Python implementation to find the next
#  greater element using two loops
def nextLargerElement(arr):
    n = len(arr)
    res = [-1] * n

    # Iterate through each element in the array
    for i in range(n):

        # Check for the next greater element
        # in the rest of the array
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                res[i] = arr[j]
                break

    return res

if __name__ == "__main__":
    arr = [6, 8, 0, 1, 3]

    res = nextLargerElement(arr)
    print(" ".join(map(str, res)))