'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    # Check if the array exists
    if arr:
        # Set a list for the count at the length of the current array
            # If you don't set the list as the length of the array (empty list),
            # It will cause the list index to be out of range
        count = [0 for i in range(len(arr))]
        # Set a variable for the single element to live
        single = None

        # Loop through the array and add to the count
            # This will look at each value and add 1 to the count
            # of that index for each instance of it
        for i in arr:
            count[i] += 1

        # Loop through the counted array
        for i in range(len(count)):
            # If there was only 1 instance of a number...
            if count[i] == 1:
                # That is the single number, return it
                single = i

    return single


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")