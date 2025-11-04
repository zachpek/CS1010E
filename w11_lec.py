#======================================================
# Linear Search / Sequential Search
#======================================================
def linear_search(L, val):
    # oh dearie me, running time can increase with length of list as it MIGHT have to search through more elements
    # so, linearly proportional to len(L)
    # so the time complexity is O(N), where N is the length of the list
    for x in L:
        if x == val:
            return True
    return False



#======================================================
# Game: Guess the Secret Number
#======================================================
import random

N = 100
SECRET_NUM = random.randint(1, N)  # 1 to N inclusive

# print("SECRET_NUM:", SECRET_NUM)

def check_guess(guess):
    if guess == SECRET_NUM:
        return "correct"
    elif guess < SECRET_NUM:
        return "too low"
    else:
        return "too high"

def guess_secret_num(start, end):
    if start == end:
        print("Guess:", start)
        return start
    else:
        guess = (start + end) // 2
        check = check_guess(guess)

        print("Guess:", guess)

        if check == "correct":
            return guess
        elif check == "too low":
            return guess_secret_num(guess + 1, end)
        else: # too high
            return guess_secret_num(start, guess - 1)

guess_secret_num(1, N)

# ok now i have to make sense of ^^

def power_of_two(n):
    # i think this proves my point
    i = 1
    while n > 2:
        n /= 2
        i += 1
    return i

# if problem size is N = 2 ** k, we get to size 1 after k steps
'''hence this algorithm has time complexity of log(N, 2)'''



#======================================================
# Binary Search (inefficient)
#======================================================
def binary_search(L, val):  # L is sorted in ascending order
    if not L:
        return False
    mid = len(L) // 2
    if L[mid] == val:
        return True
    elif val < L[mid]:
        '''terrible efficiency'''
        # because
        '''list slicing creates new lists'''
        # so gg need copy to new list, 
        return binary_search(L[:mid], val)  # go left half
    else:
        return binary_search(L[mid + 1:], val)  # go right half


#======================================================
# Binary Search (efficient) (using recursion)
'''yay no list creation, just passing of different indices into the search function'''
#======================================================
def binary_search(L, val):  # L is sorted in ascending order

    def search(low, high):
        if low > high:
            return False

        mid = (low + high) // 2

        if L[mid] == val:
            return True
        elif val < L[mid]:
            return search(low, mid - 1)  # go left half
        else:
            return search(mid + 1, high)  # go right half

    return search(0, len(L) - 1)

# keeps halving the list search space again
# i think is log n again

#======================================================
# Binary Search (efficient) (using loop)
#======================================================
def binary_search(L, val):  # L is sorted in ascending order
    low = 0
    high = len(L) - 1

    while low <= high:
        mid = (low + high) // 2

        if L[mid] == val:
            return True
        elif val < L[mid]:
            high = mid - 1  # go left half
        else:
            low = mid + 1  # go right half

    return False


# Testing
L = [2, 12, 23, 34, 45, 45, 56, 67, 78, 78, 89, 98]
binary_search(L, 2)  # True
binary_search(L, 45)  # True
binary_search(L, 98)  # True
binary_search(L, 99)  # False
binary_search(L, 46)  # False
binary_search(L, 1)   # False




#======================================================
# Selection Sort (return a new sorted list)
#======================================================
def selection_sort(L):  # L will not be modified
    Lcopy = L.copy()    # make a copy first
    sorted = []         # result list
    while Lcopy:
        smallest = min(Lcopy)
        Lcopy.remove(smallest)
        sorted.append(smallest)
    return sorted

# running time is O(N**2), N = len(L)
# while loop executed for every single element in the list L i.e., N times
    # and every iteration need to search through list for minimum: N times
    # remove also worse case search through list N times
    # so within the loop is time complexity of 2N
# so N * 2N = N ** 2
# ew quadratic


# Testing
L = [5, 4, 1, 6, 9, 7, 3, 8, 4, 2]
selection_sort(L)
# should return [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]


#======================================================
# Selection Sort (return a new sorted list) (with print statements)
#======================================================
def selection_sort(L):  # L will not be modified
    Lcopy = L.copy()    # make a copy first
    sorted = []         # result list
    print("Lcopy:", Lcopy)
    print("sorted:", sorted)

    while Lcopy:
        smallest = min(Lcopy)
        print("smallest:", smallest)
        Lcopy.remove(smallest)
        sorted.append(smallest)
        print("Lcopy:", Lcopy)
        print("sorted:", sorted)
    return sorted

# Testing
L = [4, 5, 1, 3]
selection_sort(L)
# should return [1, 3, 4, 5]



#======================================================
# Selection Sort (in-place)
#======================================================
def selection_sort(L):  # L will contain sorted result
    for i in range(len(L) - 1):
        # find location of smallest element in unsorted section
        min_idx = i
        for j in range(i + 1, len(L)):
            if L[j] < L[min_idx]:
                min_idx = j
        # place smallest element at position i
        L[i], L[min_idx] = L[min_idx], L[i]  # swap
    # no need to return L because result is in L

# Testing
L = [5, 4, 1, 6, 9, 7, 3, 8, 4, 2]
selection_sort(L)
L  # should be [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]




#======================================================
# Merge Sort (return a new sorted list) (inefficient merge)
#======================================================
def merge_sort(L):  # L will not be modified
    if len(L) < 2:
        return L.copy()
    mid = len(L) // 2
    left  = merge_sort(L[:mid])  # sort left half
    right = merge_sort(L[mid:])  # sort right half
    return merge(left, right)

def merge(L1, L2):
    result = []
    while L1 and L2:
        if L1[0] < L2[0]:
            result.append(L1.pop(0))
        else:
            result.append(L2.pop(0))
    result.extend(L1)
    result.extend(L2)
    return result

# Testing
L = [5, 4, 1, 6, 9, 7, 3, 8, 4, 2]
merge_sort(L)
# should return [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]

'''O(N^2 + M^2) where N is len(L1) ad M is len(L2)'''

#======================================================
# Merge Sort (return a new sorted list) (efficient merge)
#======================================================
def merge_sort(L):  # L will not be modified
    if len(L) < 2:
        return L.copy()
    mid = len(L) // 2
    left  = merge_sort(L[:mid])  # sort left half
    right = merge_sort(L[mid:])  # sort right half
    return merge(left, right)

def merge(L1, L2):
    result = []
    L1_idx = 0
    L2_idx = 0
    while L1_idx < len(L1) and L2_idx < len(L2):
        if L1[L1_idx] < L2[L2_idx]:
            result.append(L1[L1_idx])
            L1_idx += 1 # advance index instead of mutating list (via pop function)
        else:
            result.append(L2[L2_idx])
            L2_idx += 1
    result.extend(L1[L1_idx:])
    result.extend(L2[L2_idx:])
    return result

# Testing
L = [5, 4, 1, 6, 9, 7, 3, 8, 4, 2]
merge_sort(L)
# should return [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]




#======================================================
# Merge Sort (return sorted result in input list)
#======================================================
def merge_sort(L):  # L will contain sorted result
    def sort(low, high):
        if low < high:
            mid = (low + high) // 2
            sort(low, mid)
            sort(mid + 1, high)
            merge(L, low, mid, high)

    sort(0, len(L) - 1)
    # no need to return L because result is in L


def merge(L, low, mid, high):
    result = []
    left_idx = low
    right_idx = mid + 1

    while left_idx <= mid and right_idx <= high:
        if L[left_idx] <= L[right_idx]:
            result.append(L[left_idx])
            left_idx += 1
        else:
            result.append(L[right_idx])
            right_idx += 1

    # copy remaining elements of left half to result
    while left_idx <= mid:
        result.append(L[left_idx])
        left_idx += 1

    # copy remaining elements of right half to result
    while right_idx <= high:
        result.append(L[right_idx])
        right_idx += 1

    # copy merged result back to L
    L[low : high + 1] = result


# Testing
L = [5, 4, 1, 6, 9, 7, 3, 8, 4, 2]
merge_sort(L)
L  # should be [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]

