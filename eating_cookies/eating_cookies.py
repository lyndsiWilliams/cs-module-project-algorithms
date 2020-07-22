'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here

    # Check that input is negative
    if n < 0:
        # Can't eat negative cookies!
        return 0
    # Check if input is 0
    if n == 0:
        # Only 1 way to eat 0 cookies!
        return 1
    # Recursively run through and add the return for each scenario
    # (Eating 1, 2, or 3 cookies)
    else:
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

        


        

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
