# Using the following array: [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
# Which searching algorithm would be appropriate to use on the given list?

# Implement this search algorithm to search for the number 9. Add a comment to explain why you think this algorithm was a good choice.
# ● Research and implement the Insertion sort on this array.
# ● Implement a searching algorithm you haven’t tried yet in this Task on the sorted array to find the number 9. Add a comment to explain where you would use this algorithm in the real world.

# ------
# Would use linear search
# I would use this method because the list is unordered and relatively short
my_list = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

def find_9(list):
    for index in range(len(list)):
        if list[index] == 9:
            return print(f"The number 9 can be found at index '{index}' of this list.")
        
find_9(my_list)

# I will call binary search on the data after sorting it.

# The merge-sort code is based on that provided by the course (Capetown University, 2014)
def merge_sort(items):
    n = len(items)
    temporary_storage = [None] * n
    size_of_subsections = 1
    while size_of_subsections < n:
        for i in range(0, n, size_of_subsections * 2):
            i1_start, i1_end = i, min(i + size_of_subsections, n)
            i2_start, i2_end = i1_end, min(i1_end + size_of_subsections, n)
            sections = (i1_start, i1_end), (i2_start, i2_end)
            merge(items, sections, temporary_storage)
        size_of_subsections *= 2
    return items

def merge(items, sections, temporary_storage):
    (start_1, end_1), (start_2, end_2) = sections
    i_1 = start_1
    i_2 = start_2
    i_t = 0
    while i_1 < end_1 and i_2 < end_2:
        if items[i_1] < items[i_2]:
            temporary_storage[i_t] = items[i_1]
            i_1 += 1
        else:
            temporary_storage[i_t] = items[i_2]
            i_2 += 1
        i_t += 1

    while i_1 < end_1:
        temporary_storage[i_t] = items[i_1]
        i_1 += 1
        i_t += 1

    while i_2 < end_2:
        temporary_storage[i_t] = items[i_2]
        i_2 += 1
        i_t += 1
    for i in range(i_t):
        items[start_1 + i] = temporary_storage[i]

print(f"Unsorted list: {my_list}")
my_list = merge_sort(my_list)
print(f"Merge-sorted list: {my_list}")

# Binary-search code based on Dalal, 2004, as provided by course Pdf: 
def binary_search(item, arr):
    low, high = 0, len(arr) - 1
    # Keep iterating until low and high cross
    # Returns None if item not found
    while high >= low:
        # Find midpoint
        mid = (low + high) // 2
        # If item is found at midpoint, return
        if arr[mid] == item:
            return mid
        # Else, if item at midpoint is less than item,
        # search the second half of the list
        elif arr[mid] < item:
            low = mid + 1
        # Else, search first half
        else:
            high = mid - 1
    return None

print(f"Index of '9' in sorted list: {binary_search(9, my_list)}")

# I would use binary search in a real-world situation when the database was already sorted or easily sortable, and memory efficiency was a concern. For example, if I was searching for the name of a marathon runner in a list of all participants, if the list was alphabetised or in order of assigned numbers.
