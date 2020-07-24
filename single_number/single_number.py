'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    # Create a set
    s = set() # O(1)

    # Loop through the array
    for i in arr: # O(n)
        # If this iteration is in the set already, remove it
        if i in s: # O(1)
            s.remove(i) # O(1)
        # Otherwise, it's a single value so add it
        else:
            s.add(i) # O(1)

    # Return the first value of the current set list
    # There should only be one element
    return list(s)[0] # O(1)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")