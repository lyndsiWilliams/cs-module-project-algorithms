'''
Input: an integer
Returns: an integer
'''
# With the cache, every n value is now only computed once then saved to the cache
# Cache reduced the runtim from O(3^n) to O(n)
# Space complexity was increased by a decent margin, though
def eating_cookies(n, cache):
    # Your code here

    # Check that input is negative
    if n < 0:
        # Can't eat negative cookies!
        return 0
    # Check if input is 0
    if n == 0:
        # Only 1 way to eat 0 cookies!
        return 1
    # Check the cache to see if it holds the answer this branch is looking for
    elif n in cache:
        return cache[n]
    # Recursively run through and add the return for each scenario
    # (Eating 1, 2, or 3 cookies)
    else:
        # Otherwise, n is not in the cache, so answer must be comuted the "normal" way
        # Once the answer is computer, save it in the cache
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
        return cache[n]

        
# import sys
# print(sys.getrecursionlimit())

        

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies, {})} ways for Cookie Monster to each {num_cookies} cookies")
