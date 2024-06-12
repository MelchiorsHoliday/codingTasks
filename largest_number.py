# My solution to the problemis this
# each call of the function compares the first two indexes of the list, and removes the smaller one
# this leaves us with the largest number in the list
# at this point, the length of the list is 1, and the recursion ends 

def largest_number(list):
    # check length of list
    if len(list) == 1:
        return list[0]
    else:
        # compare 0 and 1 index of list
        if list[0] >= list[1]:
            list.pop(1)
        else:
            list.pop(0)
        # call function again
        return largest_number(list)
        
my_list = [10, 5, 777, 342, 3338, 2, 641, 19, 2, 0, 9]

print(largest_number(my_list))