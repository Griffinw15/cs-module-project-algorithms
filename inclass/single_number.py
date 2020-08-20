'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # O(n^2) runtime 
    # is this the best we can do? 
    # how do we get rid of one of the for loops? 
    # when looping through the elements, let's count how many times 
    # they occur 
    # can we use list.count(number) and check if the count == 1
    # brute force solution: two nested loops 
    # loop through every element in the list 

    # is there a data structure that would help us? 
    # a dict helps us by allowing us to check for duplicate values 
    # sets are also an option
    # as we loop, save the fact that we saw this value 
    # if we see it again, then we remove them 
    # dictionaries 

    # as far as space complexity is concerned, worst case would 
    # if we have half of the elements in the set before we start
    # removing any of them: O((1/2) * n) space complexity 
    s = set() # O(1)

    for x in arr: # O(n)
        # loop through every element in the list 
        if x in s: # O(1)
            s.remove(x) # O(1)
        else:
            s.add(x) # O(1)

    # at this point we should only have one element in our set 
    return list(s)[0] # O(1)

# Space complexity: measures how memory-usage scales
# Any data structures that are passed into a function don't count towards space complexity
# space complexity only cares about any additional data structures that are initialized 
# during an algorithm's execution. 

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is { single_number(arr)}")