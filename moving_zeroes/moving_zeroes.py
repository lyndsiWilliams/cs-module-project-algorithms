'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    # Check if the array exists
    if arr:
        # Loop through the array
        for i in arr:
            # If the value is zero...
            if i == 0:
                # Remove the value
                arr.remove(i)
                # Append it to the back of the array
                arr.append(i)
    
    # Return the properly-mutated array
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")